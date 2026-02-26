"""
HyperAI Phoenix - Code Analysis Tools
Implementation of self-awareness capabilities through code introspection
Implements analyze_code_file and analyze_project_structure for D&R protocol
"""

import ast
import os
import sys
import json
import logging
from typing import Dict, List, Any, Optional, Tuple, Set
from datetime import datetime
from dataclasses import dataclass, asdict
import importlib.util
import inspect
import re


@dataclass
class CodeComplexity:
    """Code complexity metrics"""
    cyclomatic_complexity: int
    cognitive_complexity: int
    lines_of_code: int
    lines_of_comments: int
    maintainability_index: float


@dataclass
class ClassInfo:
    """Information about a class"""
    name: str
    methods: List[str]
    attributes: List[str]
    inheritance: List[str]
    lines_of_code: int
    complexity: int
    docstring: Optional[str]


@dataclass
class FunctionInfo:
    """Information about a function"""
    name: str
    parameters: List[str]
    return_type: Optional[str]
    lines_of_code: int
    complexity: int
    docstring: Optional[str]
    is_async: bool


@dataclass
class FileAnalysis:
    """Complete analysis of a single file"""
    file_path: str
    imports: List[str]
    dependencies: List[str]
    classes: Dict[str, ClassInfo]
    functions: Dict[str, FunctionInfo]
    global_variables: List[str]
    complexity: CodeComplexity
    quality_issues: List[str]
    suggestions: List[str]
    analysis_timestamp: datetime
    encoding: str
    syntax_valid: bool


@dataclass
class ProjectStructure:
    """Complete project structure analysis"""
    project_root: str
    total_files: int
    python_files: int
    total_lines: int
    file_analyses: Dict[str, FileAnalysis]
    dependency_graph: Dict[str, List[str]]
    package_structure: Dict[str, Any]
    architecture_patterns: List[str]
    potential_issues: List[str]
    improvement_opportunities: List[str]
    analysis_timestamp: datetime


class CodeAnalysisTools:
    """Advanced code analysis tools for self-awareness"""

    def __init__(self, base_directory: str = ".", language: str = "en"):
        self.base_directory = os.path.abspath(base_directory)
        self.language = language
        self.logger = logging.getLogger(__name__)

        # Error messages for internationalization
        self.error_messages = {
            'en': {
                'FILE_NOT_EXISTS': 'File does not exist: {path}',
                'NOT_PYTHON_FILE': 'Not a Python file: {path}',
                'SYNTAX_ERROR': 'Syntax error: {error}',
                'ANALYSIS_FAILED': 'Analysis failed: {error}',
                'PROJECT_NOT_EXISTS': 'Project path does not exist: {path}',
                'NO_PYTHON_FILES': 'No Python files found in: {path}',
                'PROJECT_ANALYSIS_FAILED': 'Project analysis failed: {error}'
            },
            'vi': {
                'FILE_NOT_EXISTS': 'File không tồn tại: {path}',
                'NOT_PYTHON_FILE': 'Không phải file Python: {path}',
                'SYNTAX_ERROR': 'Lỗi syntax: {error}',
                'ANALYSIS_FAILED': 'Lỗi phân tích: {error}',
                'PROJECT_NOT_EXISTS': 'Project path không tồn tại: {path}',
                'NO_PYTHON_FILES': 'Không tìm thấy file Python trong: {path}',
                'PROJECT_ANALYSIS_FAILED': 'Lỗi phân tích project: {error}'
            }
        }

        # Analysis cache to avoid re-analyzing unchanged files
        self.analysis_cache = {}

        # Code quality thresholds
        self.complexity_thresholds = {
            'function_max_complexity': 10,
            'class_max_complexity': 20,
            'file_max_complexity': 50,
            'max_function_lines': 50,
            'max_class_lines': 200
        }

    def _get_error_message(self, key: str, **kwargs) -> str:
        """Get localized error message"""
        messages = self.error_messages.get(self.language, self.error_messages['en'])
        message = messages.get(key, f'Unknown error: {key}')
        return message.format(**kwargs)

    def analyze_code_file(self, file_path: str) -> Dict[str, Any]:
        """
        Analyze a single Python file and return structured information
        This implements the D&R protocol's "Deconstruct" phase for code files
        """
        try:
            if not os.path.exists(file_path):
                return {
                    'success': False,
                    'error': self._get_error_message('FILE_NOT_EXISTS', path=file_path),
                    'file_path': file_path
                }

            if not file_path.endswith('.py'):
                return {
                    'success': False,
                    'error': self._get_error_message('NOT_PYTHON_FILE', path=file_path),
                    'file_path': file_path
                }

            # Read file content
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Parse AST
            try:
                tree = ast.parse(content)
                syntax_valid = True
            except SyntaxError as e:
                return {
                    'success': False,
                    'error': self._get_error_message('SYNTAX_ERROR', error=str(e)),
                    'file_path': file_path,
                    'syntax_valid': False
                }

            # Perform comprehensive analysis
            analysis = self._analyze_ast(tree, content, file_path)

            # Calculate complexity metrics
            complexity = self._calculate_complexity(tree, content)

            # Identify quality issues
            quality_issues = self._identify_quality_issues(analysis, complexity)

            # Generate improvement suggestions
            suggestions = self._generate_suggestions(analysis, complexity, quality_issues)

            file_analysis = FileAnalysis(
                file_path=file_path,
                imports=analysis['imports'],
                dependencies=analysis['dependencies'],
                classes=analysis['classes'],
                functions=analysis['functions'],
                global_variables=analysis['global_variables'],
                complexity=complexity,
                quality_issues=quality_issues,
                suggestions=suggestions,
                analysis_timestamp=datetime.now(),
                encoding='utf-8',
                syntax_valid=syntax_valid
            )

            # Cache the analysis
            self.analysis_cache[file_path] = file_analysis

            result = {
                'success': True,
                'file_path': file_path,
                'analysis': asdict(file_analysis),
                'complexity_score': complexity.cyclomatic_complexity,
                'dependencies': analysis['dependencies'],
                'defined_classes': {name: {
                    'methods': cls.methods,
                    'lines_of_code': cls.lines_of_code
                } for name, cls in analysis['classes'].items()},
                'quality_issues': quality_issues
            }

            self.logger.info(f"Analyzed file: {file_path} - Complexity: {complexity.cyclomatic_complexity}")
            return result

        except Exception as e:
            self.logger.error(f"Code analysis failed for {file_path}: {e}")
            return {
                'success': False,
                'error': self._get_error_message('ANALYSIS_FAILED', error=str(e)),
                'file_path': file_path
            }

    def analyze_project_structure(self, project_path: str = None) -> Dict[str, Any]:
        """
        Analyze entire project structure and dependencies
        This provides comprehensive self-awareness at the architecture level
        """
        try:
            if project_path is None:
                project_path = self.base_directory

            if not os.path.exists(project_path):
                return {
                    'success': False,
                    'error': self._get_error_message('PROJECT_NOT_EXISTS', path=project_path)
                }

            # Scan for Python files
            python_files = self._find_python_files(project_path)

            if not python_files:
                return {
                    'success': False,
                    'error': self._get_error_message('NO_PYTHON_FILES', path=project_path)
                }

            # Analyze each file
            file_analyses = {}
            total_lines = 0

            for file_path in python_files:
                analysis_result = self.analyze_code_file(file_path)
                if analysis_result['success']:
                    file_analyses[file_path] = analysis_result['analysis']
                    total_lines += analysis_result['analysis']['complexity']['lines_of_code']

            # Build dependency graph
            dependency_graph = self._build_dependency_graph(file_analyses)

            # Analyze package structure
            package_structure = self._analyze_package_structure(project_path, python_files)

            # Identify architecture patterns
            architecture_patterns = self._identify_architecture_patterns(file_analyses, package_structure)

            # Identify potential issues
            potential_issues = self._identify_project_issues(file_analyses, dependency_graph)

            # Generate improvement opportunities
            improvement_opportunities = self._generate_project_improvements(
                file_analyses, dependency_graph, architecture_patterns
            )

            project_analysis = ProjectStructure(
                project_root=project_path,
                total_files=len(python_files),
                python_files=len(python_files),
                total_lines=total_lines,
                file_analyses=file_analyses,
                dependency_graph=dependency_graph,
                package_structure=package_structure,
                architecture_patterns=architecture_patterns,
                potential_issues=potential_issues,
                improvement_opportunities=improvement_opportunities,
                analysis_timestamp=datetime.now()
            )

            result = {
                'success': True,
                'project_path': project_path,
                'analysis': asdict(project_analysis),
                'summary': {
                    'total_files': len(python_files),
                    'total_lines': total_lines,
                    'avg_complexity': sum(
                        fa['complexity']['cyclomatic_complexity']
                        for fa in file_analyses.values()
                    ) / len(file_analyses) if file_analyses else 0,
                    'architecture_patterns': architecture_patterns,
                    'critical_issues': len(potential_issues)
                }
            }

            self.logger.info(f"Analyzed project: {project_path} - {len(python_files)} files, {total_lines} lines")
            return result

        except Exception as e:
            self.logger.error(f"Project analysis failed for {project_path}: {e}")
            return {
                'success': False,
                'error': self._get_error_message('PROJECT_ANALYSIS_FAILED', error=str(e)),
                'project_path': project_path
            }

    def _analyze_ast(self, tree: ast.AST, content: str, file_path: str) -> Dict[str, Any]:
        """Analyze AST and extract structured information"""
        analysis = {
            'imports': [],
            'dependencies': [],
            'classes': {},
            'functions': {},
            'global_variables': []
        }

        lines = content.split('\n')

        # First pass: collect classes
        class_methods = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                class_info = self._extract_class_info(node, lines)
                analysis['classes'][node.name] = class_info
                # Remember all method names to exclude from top-level functions
                class_methods.update(class_info.methods)

        # Second pass: collect everything else
        for node in ast.walk(tree):
            # Import analysis
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                import_info = self._extract_import_info(node)
                analysis['imports'].extend(import_info['imports'])
                analysis['dependencies'].extend(import_info['dependencies'])

            # Function analysis (only top-level functions, not methods)
            elif isinstance(node, ast.FunctionDef):
                if node.name not in class_methods:
                    function_info = self._extract_function_info(node, lines)
                    analysis['functions'][node.name] = function_info

            # Global variable analysis
            elif isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        analysis['global_variables'].append(target.id)

        # Remove duplicates
        analysis['dependencies'] = list(set(analysis['dependencies']))
        analysis['global_variables'] = list(set(analysis['global_variables']))

        return analysis

    def _extract_import_info(self, node: ast.AST) -> Dict[str, List[str]]:
        """Extract import information from AST node"""
        imports = []
        dependencies = []

        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(alias.name)
                dependencies.append(alias.name.split('.')[0])
        elif isinstance(node, ast.ImportFrom):
            module = node.module or ''
            for alias in node.names:
                imports.append(f"{module}.{alias.name}" if module else alias.name)
            if module:
                dependencies.append(module.split('.')[0])

        return {'imports': imports, 'dependencies': dependencies}

    def _extract_class_info(self, node: ast.ClassDef, lines: List[str]) -> ClassInfo:
        """Extract class information from AST node"""
        methods = []
        attributes = []

        # Extract inheritance - handle different base types safely
        inheritance = []
        for base in node.bases:
            if isinstance(base, ast.Name):
                inheritance.append(base.id)
            elif isinstance(base, ast.Attribute):
                # Improved handling for attribute-based inheritance
                value = []
                current = base
                while isinstance(current, ast.Attribute):
                    value.insert(0, current.attr)
                    current = current.value
                if isinstance(current, ast.Name):
                    value.insert(0, current.id)
                inheritance.append(".".join(value))
            elif isinstance(base, ast.Subscript):
                # Improved handling for subscript-based inheritance (e.g., Generic[T])
                base_name = base.value.id if isinstance(base.value, ast.Name) else str(type(base.value).__name__)
                subscript = ast.dump(base.slice)  # Provide detailed subscript info
                inheritance.append(f"{base_name}[{subscript}]")
            else:
                # Fallback for other node types
                inheritance.append(f"<{type(base).__name__}>")

        # Extract methods and attributes
        for item in node.body:
            if isinstance(item, ast.FunctionDef):
                methods.append(item.name)
            elif isinstance(item, ast.Assign):
                for target in item.targets:
                    if isinstance(target, ast.Name):
                        attributes.append(target.id)

        # Calculate lines of code
        start_line = node.lineno
        end_line = node.end_lineno or node.lineno
        lines_of_code = end_line - start_line + 1

        # Extract docstring
        docstring = None
        if (node.body and
            isinstance(node.body[0], ast.Expr) and
            isinstance(node.body[0].value, ast.Constant) and
            isinstance(node.body[0].value.value, str)):
            docstring = node.body[0].value.value

        return ClassInfo(
            name=node.name,
            methods=methods,
            attributes=attributes,
            inheritance=inheritance,
            lines_of_code=lines_of_code,
            complexity=len(methods) + len(attributes),
            docstring=docstring
        )

    def _extract_function_info(self, node: ast.FunctionDef, lines: List[str]) -> FunctionInfo:
        """Extract function information from AST node"""
        # Extract parameters
        parameters = []
        for arg in node.args.args:
            parameters.append(arg.arg)

        # Extract return type annotation
        return_type = None
        if node.returns:
            return_type = ast.unparse(node.returns) if hasattr(ast, 'unparse') else str(node.returns)

        # Calculate lines of code
        start_line = node.lineno
        end_line = node.end_lineno or node.lineno
        lines_of_code = end_line - start_line + 1

        # Extract docstring
        docstring = None
        if (node.body and
            isinstance(node.body[0], ast.Expr) and
            isinstance(node.body[0].value, ast.Constant) and
            isinstance(node.body[0].value.value, str)):
            docstring = node.body[0].value.value

        # Calculate cyclomatic complexity (simplified)
        complexity = 1  # Base complexity
        for child in ast.walk(node):
            if isinstance(child, (ast.If, ast.While, ast.For, ast.Try, ast.With)):
                complexity += 1
            elif isinstance(child, ast.BoolOp):
                complexity += len(child.values) - 1

        return FunctionInfo(
            name=node.name,
            parameters=parameters,
            return_type=return_type,
            lines_of_code=lines_of_code,
            complexity=complexity,
            docstring=docstring,
            is_async=isinstance(node, ast.AsyncFunctionDef)
        )

    def _calculate_complexity(self, tree: ast.AST, content: str) -> CodeComplexity:
        """Calculate code complexity metrics"""
        lines = content.split('\n')
        lines_of_code = len([line for line in lines if line.strip() and not line.strip().startswith('#')])
        lines_of_comments = len([line for line in lines if line.strip().startswith('#')])

        # Calculate cyclomatic complexity
        cyclomatic_complexity = 1  # Base complexity
        for node in ast.walk(tree):
            if isinstance(node, (ast.If, ast.While, ast.For, ast.Try, ast.With, ast.FunctionDef, ast.ClassDef)):
                cyclomatic_complexity += 1
            elif isinstance(node, ast.BoolOp):
                cyclomatic_complexity += len(node.values) - 1

        # Cognitive complexity (simplified approximation)
        cognitive_complexity = cyclomatic_complexity

        # Maintainability index (simplified)
        if lines_of_code > 0:
            maintainability_index = max(0, 171 - 5.2 * math.log(lines_of_code) - 0.23 * cyclomatic_complexity - 16.2 * math.log(lines_of_code + lines_of_comments))
        else:
            maintainability_index = 100.0

        return CodeComplexity(
            cyclomatic_complexity=cyclomatic_complexity,
            cognitive_complexity=cognitive_complexity,
            lines_of_code=lines_of_code,
            lines_of_comments=lines_of_comments,
            maintainability_index=maintainability_index
        )

    def _identify_quality_issues(self, analysis: Dict[str, Any], complexity: CodeComplexity) -> List[str]:
        """Identify code quality issues"""
        issues = []

        # Complexity issues
        if complexity.cyclomatic_complexity > self.complexity_thresholds['file_max_complexity']:
            issues.append(f"High file complexity: {complexity.cyclomatic_complexity}")

        # Function complexity issues
        for name, func in analysis['functions'].items():
            if func.complexity > self.complexity_thresholds['function_max_complexity']:
                issues.append(f"High function complexity in {name}: {func.complexity}")
            if func.lines_of_code > self.complexity_thresholds['max_function_lines']:
                issues.append(f"Long function {name}: {func.lines_of_code} lines")

        # Class complexity issues
        for name, cls in analysis['classes'].items():
            if cls.complexity > self.complexity_thresholds['class_max_complexity']:
                issues.append(f"High class complexity in {name}: {cls.complexity}")
            if cls.lines_of_code > self.complexity_thresholds['max_class_lines']:
                issues.append(f"Large class {name}: {cls.lines_of_code} lines")

        # Documentation issues
        for name, func in analysis['functions'].items():
            if not func.docstring:
                issues.append(f"Missing docstring in function {name}")

        for name, cls in analysis['classes'].items():
            if not cls.docstring:
                issues.append(f"Missing docstring in class {name}")

        return issues

    def _generate_suggestions(self, analysis: Dict[str, Any], complexity: CodeComplexity, quality_issues: List[str]) -> List[str]:
        """Generate improvement suggestions"""
        suggestions = []

        if complexity.cyclomatic_complexity > 20:
            suggestions.append("Consider breaking down complex logic into smaller functions")

        if len(analysis['functions']) > 20:
            suggestions.append("Consider organizing functions into classes or modules")

        if len(quality_issues) > 5:
            suggestions.append("Focus on addressing documentation and complexity issues")

        return suggestions

    def _find_python_files(self, directory: str) -> List[str]:
        """Find all Python files in directory"""
        python_files = []
        for root, dirs, files in os.walk(directory):
            # Skip common non-source directories
            dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__', '.pytest_cache', 'node_modules']]

            for file in files:
                if file.endswith('.py'):
                    python_files.append(os.path.join(root, file))

        return python_files

    def _build_dependency_graph(self, file_analyses: Dict[str, Any]) -> Dict[str, List[str]]:
        """Build dependency graph between files"""
        dependency_graph = {}

        for file_path, analysis in file_analyses.items():
            dependencies = []
            for dep in analysis['dependencies']:
                # Find files that might provide this dependency
                for other_file in file_analyses:
                    if dep in os.path.basename(other_file) or dep in other_file:
                        dependencies.append(other_file)

            dependency_graph[file_path] = dependencies

        return dependency_graph

    def _analyze_package_structure(self, project_path: str, python_files: List[str]) -> Dict[str, Any]:
        """Analyze package structure"""
        packages = {}

        for file_path in python_files:
            rel_path = os.path.relpath(file_path, project_path)
            parts = rel_path.split(os.sep)

            # Build package hierarchy
            current = packages
            for part in parts[:-1]:  # Exclude filename
                if part not in current:
                    current[part] = {}
                current = current[part]

        return packages

    def _identify_architecture_patterns(self, file_analyses: Dict[str, Any], package_structure: Dict[str, Any]) -> List[str]:
        """Identify architecture patterns"""
        patterns = []

        # Check for common patterns
        if any('controller' in path.lower() for path in file_analyses.keys()):
            patterns.append("MVC Pattern")

        if any('model' in path.lower() for path in file_analyses.keys()):
            patterns.append("Model-based Architecture")

        if any('service' in path.lower() for path in file_analyses.keys()):
            patterns.append("Service Layer Pattern")

        return patterns

    def _identify_project_issues(self, file_analyses: Dict[str, Any], dependency_graph: Dict[str, List[str]]) -> List[str]:
        """Identify project-level issues"""
        issues = []

        # Check for circular dependencies
        for file_path, deps in dependency_graph.items():
            for dep in deps:
                if file_path in dependency_graph.get(dep, []):
                    issues.append(f"Circular dependency: {file_path} <-> {dep}")

        # Check for missing documentation
        undocumented_files = 0
        for file_path, analysis in file_analyses.items():
            if not analysis.get('functions') and not analysis.get('classes'):
                continue
            has_docs = any(f.get('docstring') for f in analysis.get('functions', {}).values())
            has_docs = has_docs or any(c.get('docstring') for c in analysis.get('classes', {}).values())
            if not has_docs:
                undocumented_files += 1

        if undocumented_files > len(file_analyses) * 0.5:
            issues.append("More than 50% of files lack documentation")

        return issues

    def _generate_project_improvements(self, file_analyses: Dict[str, Any], dependency_graph: Dict[str, List[str]], architecture_patterns: List[str]) -> List[str]:
        """Generate project improvement opportunities"""
        improvements = []

        # Suggest documentation improvements
        if len(architecture_patterns) == 0:
            improvements.append("Consider implementing a clear architectural pattern")

        # Suggest dependency management
        max_deps = max(len(deps) for deps in dependency_graph.values()) if dependency_graph else 0
        if max_deps > 10:
            improvements.append("Consider reducing file dependencies for better modularity")

        # Suggest testing
        test_files = [f for f in file_analyses.keys() if 'test' in f.lower()]
        source_files = [f for f in file_analyses.keys() if 'test' not in f.lower()]
        if len(test_files) < len(source_files) * 0.5:
            improvements.append("Consider adding more test files for better coverage")

        return improvements


# Import math for maintainability index calculation
try:
    import math
except ImportError:
    # Fallback if math is not available
    class MockMath:
        @staticmethod
        def log(x):
            return 1.0 if x > 0 else 0.0
    math = MockMath()
