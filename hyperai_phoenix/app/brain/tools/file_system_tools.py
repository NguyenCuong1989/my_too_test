"""
HyperAI Phoenix - File System Tools
Specialized file system operations with safety checks and internationalization support
"""

import os
import shutil
import glob
import mimetypes
from datetime import datetime
from typing import Dict, List, Any, Optional
import json
import logging
from ..i18n import error_message

class FileSystemTools:
    """Enhanced file system operations for HyperAI Phoenix"""

    def __init__(self, base_directory: str = ".", safe_mode: bool = True):
        self.base_directory = os.path.abspath(base_directory)
        self.safe_mode = safe_mode
        self.logger = logging.getLogger(__name__)

        # Define safe directories for file operations
        self.safe_directories = [
            self.base_directory,
            os.path.join(self.base_directory, "data"),
            os.path.join(self.base_directory, "hyperai_phoenix"),
            os.path.join(self.base_directory, "logs"),
            os.path.join(self.base_directory, "temp")
        ]

        # File operation history
        self.operation_history = []

    def _is_safe_path(self, filepath: str) -> bool:
        """Check if the file path is within safe directories"""
        if not self.safe_mode:
            return True

        abs_path = os.path.abspath(filepath)

        # Check if path is within safe directories
        for safe_dir in self.safe_directories:
            if abs_path.startswith(safe_dir):
                return True

        return False

    def _log_operation(self, operation: str, filepath: str, success: bool, details: str = None):
        """Log file operation"""
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'operation': operation,
            'filepath': filepath,
            'success': success,
            'details': details
        }

        self.operation_history.append(log_entry)

        # Keep history size manageable
        if len(self.operation_history) > 100:
            self.operation_history = self.operation_history[-80:]

        level = logging.INFO if success else logging.ERROR
        self.logger.log(level, f"File operation: {operation} on {filepath} - {'Success' if success else 'Failed'}")

    def read_file(self, filepath: str, encoding: str = "utf-8") -> Dict[str, Any]:
        """Read file with enhanced error handling and metadata"""
        try:
            if not self._is_safe_path(filepath):
                error_msg = error_message('file_access_denied', path=filepath)
                self._log_operation("read", filepath, False, error_msg)
                return {'success': False, 'error': error_msg}

            if not os.path.exists(filepath):
                error_msg = error_message('file_not_found', path=filepath)
                self._log_operation("read", filepath, False, error_msg)
                return {'success': False, 'error': error_msg}

            # Get file metadata
            file_stats = os.stat(filepath)
            file_size = file_stats.st_size

            # Check if file is too large (default 10MB limit)
            if file_size > 10 * 1024 * 1024:
                error_msg = error_message('file_too_large', size=file_size)
                self._log_operation("read", filepath, False, error_msg)
                return {'success': False, 'error': error_msg}

            with open(filepath, 'r', encoding=encoding) as f:
                content = f.read()

            # Detect file type
            mime_type, _ = mimetypes.guess_type(filepath)

            result = {
                'success': True,
                'content': content,
                'filepath': filepath,
                'size_bytes': file_size,
                'encoding': encoding,
                'mime_type': mime_type,
                'modified_time': datetime.fromtimestamp(file_stats.st_mtime).isoformat(),
                'line_count': content.count('\n') + 1 if content else 0
            }

            self._log_operation("read", filepath, True, f"Read {file_size} bytes")
            return result

        except UnicodeDecodeError as e:
            error_msg = error_message('encoding_error', error=str(e))
            self._log_operation("read", filepath, False, error_msg)
            return {'success': False, 'error': error_msg}
        except PermissionError:
            error_msg = error_message('file_access_denied', path=filepath)
            self._log_operation("read", filepath, False, error_msg)
            return {'success': False, 'error': error_msg}
        except Exception as e:
            error_msg = error_message('file_read_error', error=str(e))
            self._log_operation("read", filepath, False, error_msg)
            return {'success': False, 'error': error_msg}

    def write_file(self, filepath: str, content: str, encoding: str = "utf-8",
                   append: bool = False, backup: bool = True) -> Dict[str, Any]:
        """Write file with backup and safety checks"""
        try:
            if not self._is_safe_path(filepath):
                error_msg = error_message('file_write_denied', path=filepath)
                self._log_operation("write", filepath, False, error_msg)
                return {'success': False, 'error': error_msg}

            # Create directory if it doesn't exist
            directory = os.path.dirname(filepath)
            if directory and not os.path.exists(directory):
                os.makedirs(directory, exist_ok=True)

            # Create backup if file exists and backup is enabled
            backup_path = None
            if backup and os.path.exists(filepath) and not append:
                backup_path = f"{filepath}.backup.{datetime.now().strftime('%Y%m%d_%H%M%S')}"
                shutil.copy2(filepath, backup_path)

            # Write file
            mode = 'a' if append else 'w'
            with open(filepath, mode, encoding=encoding) as f:
                f.write(content)

            # Get file size after writing
            file_size = os.path.getsize(filepath)

            result = {
                'success': True,
                'filepath': filepath,
                'bytes_written': len(content.encode(encoding)),
                'total_file_size': file_size,
                'mode': 'appended' if append else 'written',
                'encoding': encoding,
                'backup_created': backup_path
            }

            operation = "append" if append else "write"
            self._log_operation(operation, filepath, True, f"Wrote {len(content)} characters")
            return result

        except PermissionError:
            error_msg = error_message('file_write_denied', path=filepath)
            self._log_operation("write", filepath, False, error_msg)
            return {'success': False, 'error': error_msg}
        except Exception as e:
            error_msg = error_message('file_write_error', error=str(e))
            self._log_operation("write", filepath, False, error_msg)
            return {'success': False, 'error': error_msg}

    def list_directory(self, directory: str, pattern: str = None,
                      recursive: bool = False, include_hidden: bool = False) -> Dict[str, Any]:
        """List directory contents with detailed information"""
        try:
            if not self._is_safe_path(directory):
                error_msg = error_message('directory_access_denied', path=directory)
                self._log_operation("list", directory, False, error_msg)
                return {'success': False, 'error': error_msg}

            if not os.path.exists(directory):
                error_msg = error_message('directory_not_found', path=directory)
                self._log_operation("list", directory, False, error_msg)
                return {'success': False, 'error': error_msg}

            if not os.path.isdir(directory):
                error_msg = error_message('not_a_directory', path=directory)
                self._log_operation("list", directory, False, error_msg)
                return {'success': False, 'error': error_msg}

            files = []
            directories = []

            if recursive:
                for root, dirs, filenames in os.walk(directory):
                    # Filter hidden directories if not included
                    if not include_hidden:
                        dirs[:] = [d for d in dirs if not d.startswith('.')]

                    for dirname in dirs:
                        if include_hidden or not dirname.startswith('.'):
                            dir_path = os.path.join(root, dirname)
                            if pattern is None or glob.fnmatch.fnmatch(dirname, pattern):
                                directories.append(self._get_item_info(dir_path, is_directory=True))

                    for filename in filenames:
                        if include_hidden or not filename.startswith('.'):
                            file_path = os.path.join(root, filename)
                            if pattern is None or glob.fnmatch.fnmatch(filename, pattern):
                                files.append(self._get_item_info(file_path, is_directory=False))
            else:
                for item in os.listdir(directory):
                    if not include_hidden and item.startswith('.'):
                        continue

                    item_path = os.path.join(directory, item)

                    if pattern and not glob.fnmatch.fnmatch(item, pattern):
                        continue

                    if os.path.isdir(item_path):
                        directories.append(self._get_item_info(item_path, is_directory=True))
                    else:
                        files.append(self._get_item_info(item_path, is_directory=False))

            result = {
                'success': True,
                'directory': directory,
                'files': sorted(files, key=lambda x: x['name']),
                'directories': sorted(directories, key=lambda x: x['name']),
                'total_files': len(files),
                'total_directories': len(directories),
                'pattern': pattern,
                'recursive': recursive,
                'include_hidden': include_hidden
            }

            self._log_operation("list", directory, True, f"Listed {len(files)} files, {len(directories)} directories")
            return result

        except PermissionError:
            error_msg = error_message('directory_access_denied', path=directory)
            self._log_operation("list", directory, False, error_msg)
            return {'success': False, 'error': error_msg}
        except Exception as e:
            error_msg = error_message('directory_list_error', error=str(e))
            self._log_operation("list", directory, False, error_msg)
            return {'success': False, 'error': error_msg}

    def _get_item_info(self, item_path: str, is_directory: bool) -> Dict[str, Any]:
        """Get detailed information about a file or directory"""
        try:
            stats = os.stat(item_path)

            info = {
                'name': os.path.basename(item_path),
                'path': item_path,
                'type': 'directory' if is_directory else 'file',
                'size_bytes': stats.st_size,
                'modified_time': datetime.fromtimestamp(stats.st_mtime).isoformat(),
                'created_time': datetime.fromtimestamp(stats.st_ctime).isoformat(),
                'permissions': oct(stats.st_mode)[-3:]
            }

            if not is_directory:
                mime_type, encoding = mimetypes.guess_type(item_path)
                info.update({
                    'mime_type': mime_type,
                    'encoding': encoding,
                    'extension': os.path.splitext(item_path)[1]
                })

            return info

        except (OSError, ValueError):
            return {
                'name': os.path.basename(item_path),
                'path': item_path,
                'type': 'directory' if is_directory else 'file',
                'error': 'Could not get file information'
            }

    def copy_file(self, source: str, destination: str, overwrite: bool = False) -> Dict[str, Any]:
        """Copy file with safety checks"""
        try:
            if not self._is_safe_path(source) or not self._is_safe_path(destination):
                error_msg = error_message('copy_operation_denied')
                self._log_operation("copy", f"{source} -> {destination}", False, error_msg)
                return {'success': False, 'error': error_msg}

            if not os.path.exists(source):
                error_msg = error_message('source_file_not_found', path=source)
                self._log_operation("copy", source, False, error_msg)
                return {'success': False, 'error': error_msg}

            if os.path.exists(destination) and not overwrite:
                error_msg = error_message('destination_exists', path=destination)
                self._log_operation("copy", destination, False, error_msg)
                return {'success': False, 'error': error_msg}

            # Create destination directory if needed
            dest_dir = os.path.dirname(destination)
            if dest_dir and not os.path.exists(dest_dir):
                os.makedirs(dest_dir, exist_ok=True)

            # Copy file
            shutil.copy2(source, destination)

            # Verify copy
            source_size = os.path.getsize(source)
            dest_size = os.path.getsize(destination)

            result = {
                'success': True,
                'source': source,
                'destination': destination,
                'size_bytes': dest_size,
                'verified': source_size == dest_size
            }

            self._log_operation("copy", f"{source} -> {destination}", True, f"Copied {source_size} bytes")
            return result

        except PermissionError:
            error_msg = error_message('permission_denied')
            self._log_operation("copy", f"{source} -> {destination}", False, error_msg)
            return {'success': False, 'error': error_msg}
        except Exception as e:
            error_msg = error_message('file_copy_error', error=str(e))
            self._log_operation("copy", f"{source} -> {destination}", False, error_msg)
            return {'success': False, 'error': error_msg}

    def delete_file(self, filepath: str, confirm: bool = False) -> Dict[str, Any]:
        """Delete file with safety confirmation"""
        try:
            if not self._is_safe_path(filepath):
                error_msg = error_message('delete_operation_denied', path=filepath)
                self._log_operation("delete", filepath, False, error_msg)
                return {'success': False, 'error': error_msg}

            if not os.path.exists(filepath):
                error_msg = error_message('file_not_found', path=filepath)
                self._log_operation("delete", filepath, False, error_msg)
                return {'success': False, 'error': error_msg}

            if self.safe_mode and not confirm:
                error_msg = "Cần xác nhận để xóa file trong safe mode"
                self._log_operation("delete", filepath, False, error_msg)
                return {
                    'success': False,
                    'error': error_msg,
                    'requires_confirmation': True
                }

            # Get file size before deletion
            file_size = os.path.getsize(filepath)

            # Delete file
            os.remove(filepath)

            result = {
                'success': True,
                'filepath': filepath,
                'size_bytes': file_size,
                'deleted': True
            }

            self._log_operation("delete", filepath, True, f"Deleted {file_size} bytes")
            return result

        except PermissionError:
            error_msg = f"Không có quyền xóa file: {filepath}"
            self._log_operation("delete", filepath, False, error_msg)
            return {'success': False, 'error': error_msg}
        except Exception as e:
            error_msg = error_message('file_delete_error', error=str(e))
            self._log_operation("delete", filepath, False, error_msg)
            return {'success': False, 'error': error_msg}

    def create_directory(self, directory: str, parents: bool = True) -> Dict[str, Any]:
        """Create directory with parent creation option"""
        try:
            if not self._is_safe_path(directory):
                error_msg = error_message('create_directory_denied', path=directory)
                self._log_operation("mkdir", directory, False, error_msg)
                return {'success': False, 'error': error_msg}

            if os.path.exists(directory):
                if os.path.isdir(directory):
                    result = {
                        'success': True,
                        'directory': directory,
                        'existed': True,
                        'message': error_message('directory_exists')
                    }
                    self._log_operation("mkdir", directory, True, "Directory already exists")
                    return result
                else:
                    error_msg = error_message('path_exists_not_directory', path=directory)
                    self._log_operation("mkdir", directory, False, error_msg)
                    return {'success': False, 'error': error_msg}

            # Create directory
            os.makedirs(directory, exist_ok=parents)

            result = {
                'success': True,
                'directory': directory,
                'created': True,
                'parents_created': parents
            }

            self._log_operation("mkdir", directory, True, "Directory created")
            return result

        except PermissionError:
            error_msg = error_message('permission_denied')
            self._log_operation("mkdir", directory, False, error_msg)
            return {'success': False, 'error': error_msg}
        except Exception as e:
            error_msg = error_message('directory_create_error', error=str(e))
            self._log_operation("mkdir", directory, False, error_msg)
            return {'success': False, 'error': error_msg}

    def search_files(self, directory: str, pattern: str, content_search: str = None,
                    recursive: bool = True, case_sensitive: bool = False) -> Dict[str, Any]:
        """Search for files by name pattern and optionally by content"""
        try:
            if not self._is_safe_path(directory):
                error_msg = error_message('search_denied', path=directory)
                self._log_operation("search", directory, False, error_msg)
                return {'success': False, 'error': error_msg}

            if not os.path.exists(directory):
                error_msg = error_message('directory_not_found', path=directory)
                self._log_operation("search", directory, False, error_msg)
                return {'success': False, 'error': error_msg}

            matches = []
            search_pattern = pattern if case_sensitive else pattern.lower()

            if recursive:
                for root, dirs, files in os.walk(directory):
                    # Filter hidden directories
                    dirs[:] = [d for d in dirs if not d.startswith('.')]

                    for filename in files:
                        if filename.startswith('.'):
                            continue

                        check_name = filename if case_sensitive else filename.lower()

                        if glob.fnmatch.fnmatch(check_name, search_pattern):
                            file_path = os.path.join(root, filename)
                            match_info = self._get_item_info(file_path, is_directory=False)

                            # Content search if specified
                            if content_search:
                                content_match = self._search_file_content(file_path, content_search, case_sensitive)
                                match_info['content_matches'] = content_match
                                if not content_match['found']:
                                    continue

                            matches.append(match_info)

            else:
                for filename in os.listdir(directory):
                    if filename.startswith('.'):
                        continue

                    file_path = os.path.join(directory, filename)
                    if not os.path.isfile(file_path):
                        continue

                    check_name = filename if case_sensitive else filename.lower()

                    if glob.fnmatch.fnmatch(check_name, search_pattern):
                        match_info = self._get_item_info(file_path, is_directory=False)

                        # Content search if specified
                        if content_search:
                            content_match = self._search_file_content(file_path, content_search, case_sensitive)
                            match_info['content_matches'] = content_match
                            if not content_match['found']:
                                continue

                        matches.append(match_info)

            result = {
                'success': True,
                'directory': directory,
                'pattern': pattern,
                'content_search': content_search,
                'case_sensitive': case_sensitive,
                'recursive': recursive,
                'matches': matches,
                'total_found': len(matches)
            }

            self._log_operation("search", directory, True, f"Found {len(matches)} matches")
            return result

        except Exception as e:
            error_msg = error_message('search_error', error=str(e))
            self._log_operation("search", directory, False, error_msg)
            return {'success': False, 'error': error_msg}

    def _search_file_content(self, filepath: str, search_term: str, case_sensitive: bool = False) -> Dict[str, Any]:
        """Search for content within a file"""
        try:
            # Skip binary files
            mime_type, _ = mimetypes.guess_type(filepath)
            if mime_type and not mime_type.startswith('text/'):
                return {'found': False, 'reason': 'binary_file'}

            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            search_content = content if case_sensitive else content.lower()
            search_pattern = search_term if case_sensitive else search_term.lower()

            if search_pattern in search_content:
                # Find line numbers
                lines = content.split('\n')
                matching_lines = []

                for i, line in enumerate(lines, 1):
                    check_line = line if case_sensitive else line.lower()
                    if search_pattern in check_line:
                        matching_lines.append({
                            'line_number': i,
                            'content': line.strip(),
                            'position': check_line.find(search_pattern)
                        })

                return {
                    'found': True,
                    'occurrences': len(matching_lines),
                    'matching_lines': matching_lines[:10]  # Limit to first 10 matches
                }
            else:
                return {'found': False, 'reason': 'not_found'}

        except Exception as e:
            return {'found': False, 'reason': f'error: {str(e)}'}

    def get_operation_history(self, limit: int = 50) -> List[Dict[str, Any]]:
        """Get recent file operation history"""
        return self.operation_history[-limit:] if self.operation_history else []

    def get_statistics(self) -> Dict[str, Any]:
        """Get file operation statistics"""
        if not self.operation_history:
            return {'total_operations': 0}

        operations = {}
        success_count = 0

        for entry in self.operation_history:
            op_type = entry['operation']
            operations[op_type] = operations.get(op_type, 0) + 1
            if entry['success']:
                success_count += 1

        return {
            'total_operations': len(self.operation_history),
            'success_rate': success_count / len(self.operation_history),
            'operations_by_type': operations,
            'safe_mode': self.safe_mode,
            'safe_directories': self.safe_directories
        }

# Global file system tools instance
file_tools = FileSystemTools()

if __name__ == "__main__":
    # Test the file system tools
    fs_tools = FileSystemTools(safe_mode=True)

    # Test write
    result = fs_tools.write_file("test_hyperai.txt", "Hello from HyperAI Phoenix!\nĐây là test tiếng Việt.")
    print(f"Write result: {result}")

    # Test read
    result = fs_tools.read_file("test_hyperai.txt")
    print(f"Read result: {result['content'] if result['success'] else result['error']}")

    # Test list directory
    result = fs_tools.list_directory(".", pattern="*.txt")
    print(f"Directory listing: {len(result['files']) if result['success'] else result['error']} files found")

    # Test search
    result = fs_tools.search_files(".", "*.txt", content_search="HyperAI")
    print(f"Search result: {result['total_found']} matches")

    # Test copy
    result = fs_tools.copy_file("test_hyperai.txt", "test_hyperai_copy.txt")
    print(f"Copy result: {result['success']}")

    # Get statistics
    stats = fs_tools.get_statistics()
    print(f"Statistics: {stats['total_operations']} operations, {stats['success_rate']:.2%} success rate")

    # Clean up test files
    fs_tools.delete_file("test_hyperai.txt", confirm=True)
    fs_tools.delete_file("test_hyperai_copy.txt", confirm=True)
