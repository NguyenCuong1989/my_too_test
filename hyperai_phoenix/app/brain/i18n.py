"""
HyperAI Phoenix - Internationalization Module
Simple internationalization system for error messages and user-facing text
"""

from typing import Dict, Optional

class I18n:
    """Simple internationalization system"""

    def __init__(self, default_language: str = 'en'):
        self.default_language = default_language
        self.current_language = default_language

        # Message translations
        self.messages = {
            'en': {
                # File system errors
                'file_not_found': 'File not found: {path}',
                'file_access_denied': 'File access denied: {path}',
                'file_read_error': 'File read error: {error}',
                'file_write_denied': 'File write access denied: {path}',
                'file_write_error': 'File write error: {error}',
                'directory_not_found': 'Directory not found: {path}',
                'directory_access_denied': 'Directory access denied: {path}',
                'directory_list_error': 'Directory listing error: {error}',
                'not_a_directory': 'Not a directory: {path}',
                'file_copy_error': 'File copy error: {error}',
                'encoding_error': 'Encoding error: {error}',

                # General errors
                'error_occurred': 'An error occurred: {error}',
                'invalid_encoding': 'Cannot read file with encoding {encoding}',
                'permission_denied': 'Permission denied',
                'operation_failed': 'Operation failed',

                # Tool errors
                'tool_not_found': 'Tool not found: {name}',
                'parameter_validation_failed': 'Parameter validation failed: {error}',
                'filename_missing': 'Filename not found',

                # File operations
                'copy_operation_denied': 'Copy operation not allowed',
                'source_file_not_found': 'Source file not found: {path}',
                'destination_exists': 'Destination file already exists: {path}',
                'delete_operation_denied': 'Delete operation not allowed: {path}',
                'file_too_large': 'File too large: {size} bytes',
                'search_denied': 'Search not allowed in: {path}',
                'create_directory_denied': 'Create directory not allowed: {path}',
                'directory_exists': 'Directory already exists',
                'path_exists_not_directory': 'Path exists but is not a directory: {path}',
                'file_delete_error': 'File delete error: {error}',
                'directory_create_error': 'Directory creation error: {error}',
                'search_error': 'Search error: {error}',
            },
            'vi': {
                # Keep Vietnamese for compatibility
                'file_not_found': 'File không tồn tại: {path}',
                'file_access_denied': 'Truy cập file không được phép: {path}',
                'file_read_error': 'Lỗi đọc file: {error}',
                'file_write_denied': 'Ghi file không được phép: {path}',
                'file_write_error': 'Lỗi ghi file: {error}',
                'directory_not_found': 'Thư mục không tồn tại: {path}',
                'directory_access_denied': 'Truy cập thư mục không được phép: {path}',
                'directory_list_error': 'Lỗi liệt kê thư mục: {error}',
                'not_a_directory': 'Không phải là thư mục: {path}',
                'file_copy_error': 'Lỗi copy file: {error}',
                'encoding_error': 'Lỗi encoding: {error}',

                # General errors
                'error_occurred': 'Lỗi xảy ra: {error}',
                'invalid_encoding': 'Không thể đọc file với encoding {encoding}',
                'permission_denied': 'Không có quyền truy cập',
                'operation_failed': 'Thao tác thất bại',

                # Tool errors
                'tool_not_found': 'Không tìm thấy tool: {name}',
                'parameter_validation_failed': 'Validation tham số thất bại: {error}',
                'filename_missing': 'Không tìm thấy tên file',

                # File operations
                'copy_operation_denied': 'Copy operation không được phép',
                'source_file_not_found': 'Source file không tồn tại: {path}',
                'destination_exists': 'Destination file đã tồn tại: {path}',
                'delete_operation_denied': 'Delete operation không được phép: {path}',
                'file_too_large': 'File quá lớn: {size} bytes',
                'search_denied': 'Search không được phép trong: {path}',
                'create_directory_denied': 'Create directory không được phép: {path}',
                'directory_exists': 'Thư mục đã tồn tại',
                'path_exists_not_directory': 'Path đã tồn tại nhưng không phải thư mục: {path}',
                'file_delete_error': 'Lỗi xóa file: {error}',
                'directory_create_error': 'Lỗi tạo thư mục: {error}',
                'search_error': 'Lỗi tìm kiếm: {error}',
            }
        }

    def set_language(self, language: str):
        """Set the current language"""
        if language in self.messages:
            self.current_language = language
        else:
            self.current_language = self.default_language

    def get_message(self, key: str, **kwargs) -> str:
        """Get a translated message with optional formatting"""
        # Try current language first
        messages = self.messages.get(self.current_language, {})
        message = messages.get(key)

        # Fall back to default language
        if message is None:
            messages = self.messages.get(self.default_language, {})
            message = messages.get(key)

        # Fall back to key itself
        if message is None:
            message = key

        # Format with provided arguments
        try:
            return message.format(**kwargs)
        except (KeyError, ValueError):
            return message

    def error(self, key: str, **kwargs) -> str:
        """Get an error message"""
        return self.get_message(key, **kwargs)

# Global instance
_i18n_instance = I18n(default_language='en')

def get_message(key: str, **kwargs) -> str:
    """Global function to get translated message"""
    return _i18n_instance.get_message(key, **kwargs)

def set_language(language: str):
    """Global function to set language"""
    _i18n_instance.set_language(language)

def error_message(key: str, **kwargs) -> str:
    """Global function to get error message"""
    return _i18n_instance.error(key, **kwargs)
