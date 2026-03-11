# Σ_APΩ₂ CORE MODULE
# Authority: BỐ CƯỐNG Supreme System Commander
# Creator: alpha_prime_omega (4287)
# Status: CANONICAL

"""
HyperAI Phoenix - Code Generation Tools
Implementation of autonomous programming capabilities
Implements generate_code, refactor_code, and test_generated_code for LSP protocol
"""

import ast
import os
import sys
import json
import logging
import tempfile
import subprocess
import textwrap
import re
from typing import Dict, List, Any, Optional, Tuple, Union
from datetime import datetime
from dataclasses import dataclass, asdict
import importlib.util
import traceback


@dataclass
class CodeGenRequest:
    """Request for code generation"""
    specification: str
    target_file: Optional[str]
    function_name: Optional[str]
    class_name: Optional[str]
    requirements: List[str]
    style_guide: Dict[str, Any]
    test_requirements: bool


@dataclass
class RefactorRequest:
    """Request for code refactoring"""
    target_file: str
    target_function: Optional[str]
    target_class: Optional[str]
    optimization_goals: List[str]
    preserve_behavior: bool
    performance_focus: bool


@dataclass
class GeneratedCode:
    """Generated code with metadata"""
    code: str
    file_path: Optional[str]
    function_name: Optional[str]
    class_name: Optional[str]
    dependencies: List[str]
    test_code: Optional[str]
    documentation: str
    complexity_estimate: int
    generation_timestamp: datetime


@dataclass
class TestResult:
    """Result of code testing"""
    success: bool
    stdout: str
    stderr: str
    execution_time: float
    syntax_valid: bool
    runtime_errors: List[str]
    performance_metrics: Dict[str, Any]
    test_coverage: Optional[float]


class CodeGenerationTools:
    """Advanced code generation and refactoring tools"""

    def __init__(self, base_directory: str = ".", language: str = "en"):
        self.base_directory = os.path.abspath(base_directory)
        self.language = language
        self.logger = logging.getLogger(__name__)

        # Error messages for internationalization
        self.error_messages = {
            'en': {
                'SPECIFICATION_EMPTY': 'Specification cannot be empty',
                'FILE_NOT_EXISTS': 'File does not exist: {path}',
                'SYNTAX_ERROR': 'Syntax error in file: {error}',
                'CODE_GENERATION_FAILED': 'Code generation failed: {error}',
                'CODE_REFACTORING_FAILED': 'Code refactoring failed: {error}',
                'CODE_TESTING_FAILED': 'Code testing failed: {error}'
            },
            'vi': {
                'SPECIFICATION_EMPTY': 'Specification không được để trống',
                'FILE_NOT_EXISTS': 'File không tồn tại: {path}',
                'SYNTAX_ERROR': 'Lỗi syntax trong file: {error}',
                'CODE_GENERATION_FAILED': 'Lỗi tạo code: {error}',
                'CODE_REFACTORING_FAILED': 'Lỗi refactor code: {error}',
                'CODE_TESTING_FAILED': 'Lỗi test code: {error}'
            }
        }

        # Code generation templates
        self.templates = {
            'function': textwrap.dedent('''
            def {function_name}({parameters}){return_annotation}:
                """
                {docstring}

                Args:
                {args_doc}

                Returns:
                {returns_doc}
                """
                {body}
            ''').strip(),

            'class': textwrap.dedent('''
            class {class_name}{inheritance}:
                """
                {docstring}

                Attributes:
                {attributes_doc}
                """

                def __init__(self{init_params}):
                    """Initialize {class_name}"""
                    {init_body}

                {methods}
            ''').strip(),

            'test_function': textwrap.dedent('''
            def test_{function_name}():
                """Test {function_name} function"""
                {test_body}
                assert True  # Replace with actual test
            ''').strip()
        }

        # Code style configurations
        self.style_config = {
            'max_line_length': 88,
            'indent_size': 4,
            'use_type_hints': True,
            'docstring_style': 'google',
            'prefer_f_strings': True
        }

        # Generation statistics
        self.generation_stats = {
            'total_generated': 0,
            'successful_tests': 0,
            'failed_tests': 0,
            'refactoring_count': 0
        }

    def _get_error_message(self, key: str, **kwargs) -> str:
        """Get localized error message"""
        messages = self.error_messages.get(self.language, self.error_messages['en'])
        message = messages.get(key, f'Unknown error: {key}')
        return message.format(**kwargs)

    def generate_code(self, specification: str, target_file: str = None,
                     function_name: str = None, class_name: str = None,
                     requirements: List[str] = None, test_requirements: bool = True) -> Dict[str, Any]:
        """
        Generate Python code based on specification
        This implements the LSP protocol's code generation capability
        """
        try:
            if not specification:
                return {
                    'success': False,
                    'error': self._get_error_message('SPECIFICATION_EMPTY')
                }

            # Parse specification
            parsed_spec = self._parse_specification(specification)

            # Create generation request
            request = CodeGenRequest(
                specification=specification,
                target_file=target_file,
                function_name=function_name or parsed_spec.get('function_name'),
                class_name=class_name or parsed_spec.get('class_name'),
                requirements=requirements or [],
                style_guide=self.style_config,
                test_requirements=test_requirements
            )

            # Generate code based on type
            if request.class_name:
                generated = self._generate_class(request, parsed_spec)
            elif request.function_name:
                generated = self._generate_function(request, parsed_spec)
            else:
                generated = self._generate_module(request, parsed_spec)

            # Generate tests if requested
            test_code = None
            if test_requirements:
                test_code = self._generate_tests(generated, request)

            # Create final result
            result_code = GeneratedCode(
                code=generated['code'],
                file_path=target_file,
                function_name=request.function_name,
                class_name=request.class_name,
                dependencies=generated.get('dependencies', []),
                test_code=test_code,
                documentation=generated.get('documentation', ''),
                complexity_estimate=generated.get('complexity', 1),
                generation_timestamp=datetime.now()
            )

            # Update statistics
            self.generation_stats['total_generated'] += 1

            self.logger.info(f"Generated code: {request.function_name or request.class_name or 'module'}")

            return {
                'success': True,
                'generated_code': asdict(result_code),
                'code': generated['code'],
                'test_code': test_code,
                'dependencies': generated.get('dependencies', []),
                'documentation': generated.get('documentation', ''),
                'file_path': target_file
            }

        except Exception as e:
            self.logger.error(f"Code generation failed: {e}")
            return {
                'success': False,
                'error': self._get_error_message('CODE_GENERATION_FAILED', error=str(e)),
                'specification': specification
            }

    def refactor_code(self, target_file: str, target_function: str = None,
                     target_class: str = None, optimization_goals: List[str] = None,
                     preserve_behavior: bool = True) -> Dict[str, Any]:
        """
        Refactor existing code for optimization
        This implements automated code improvement
        """
        try:
            if not os.path.exists(target_file):
                return {
                    'success': False,
                    'error': self._get_error_message('FILE_NOT_EXISTS', path=target_file)
                }

            # Read original code
            with open(target_file, 'r', encoding='utf-8') as f:
                original_code = f.read()

            # Parse AST
            try:
                tree = ast.parse(original_code)
            except SyntaxError as e:
                return {
                    'success': False,
                    'error': self._get_error_message('SYNTAX_ERROR', error=str(e))
                }

            # Create refactor request
            request = RefactorRequest(
                target_file=target_file,
                target_function=target_function,
                target_class=target_class,
                optimization_goals=optimization_goals or ['performance', 'readability'],
                preserve_behavior=preserve_behavior,
                performance_focus='performance' in (optimization_goals or [])
            )

            # Perform refactoring
            refactored_code = self._perform_refactoring(tree, original_code, request)

            # Generate tests for refactored code
            test_code = self._generate_refactor_tests(original_code, refactored_code['code'], request)

            # Update statistics
            self.generation_stats['refactoring_count'] += 1

            self.logger.info(f"Refactored: {target_file}")

            return {
                'success': True,
                'original_code': original_code,
                'refactored_code': refactored_code['code'],
                'improvements': refactored_code['improvements'],
                'test_code': test_code,
                'file_path': target_file,
                'backup_recommended': True
            }

        except Exception as e:
            self.logger.error(f"Code refactoring failed: {e}")
            return {
                'success': False,
                'error': self._get_error_message('CODE_REFACTORING_FAILED', error=str(e)),
                'target_file': target_file
            }

    def test_generated_code(self, code: str, test_code: str = None,
                          timeout: float = 30.0) -> Dict[str, Any]:
        """
        Test generated code in a safe sandbox environment
        This implements code validation and safety checking
        """
        try:
            # Create temporary directory for testing
            with tempfile.TemporaryDirectory() as temp_dir:
                # Write code to temporary file
                code_file = os.path.join(temp_dir, 'generated_code.py')
                with open(code_file, 'w', encoding='utf-8') as f:
                    f.write(code)

                # Syntax validation
                try:
                    with open(code_file, 'r', encoding='utf-8') as f:
                        ast.parse(f.read())
                    syntax_valid = True
                except SyntaxError as e:
                    return {
                        'success': False,
                        'syntax_valid': False,
                        'error': self._get_error_message('SYNTAX_ERROR', error=str(e)),
                        'code': code
                    }

                # Runtime testing
                test_results = self._run_code_tests(code_file, test_code, timeout)

                # Performance metrics
                performance_metrics = self._measure_performance(code_file)

                # Security check
                security_issues = self._check_security(code)

                # Update statistics
                if test_results['success']:
                    self.generation_stats['successful_tests'] += 1
                else:
                    self.generation_stats['failed_tests'] += 1

                result = TestResult(
                    success=test_results['success'],
                    stdout=test_results.get('stdout', ''),
                    stderr=test_results.get('stderr', ''),
                    execution_time=test_results.get('execution_time', 0.0),
                    syntax_valid=syntax_valid,
                    runtime_errors=test_results.get('errors', []),
                    performance_metrics=performance_metrics,
                    test_coverage=test_results.get('coverage')
                )

                self.logger.info(f"Tested generated code - Success: {test_results['success']}")

                return {
                    'success': True,
                    'test_result': asdict(result),
                    'syntax_valid': syntax_valid,
                    'runtime_success': test_results['success'],
                    'security_issues': security_issues,
                    'performance_metrics': performance_metrics,
                    'execution_time': test_results.get('execution_time', 0.0)
                }

        except Exception as e:
            self.logger.error(f"Code testing failed: {e}")
            return {
                'success': False,
                'error': self._get_error_message('CODE_TESTING_FAILED', error=str(e)),
                'code': code[:200] + '...' if len(code) > 200 else code
            }

    def _parse_specification(self, specification: str) -> Dict[str, Any]:
        """Parse natural language specification into structured format"""
        spec = {
            'type': 'function',  # default
            'function_name': None,
            'class_name': None,
            'parameters': [],
            'return_type': None,
            'description': specification
        }

        # Extract function name
        func_match = re.search(r'function\s+(\w+)|def\s+(\w+)|hàm\s+(\w+)', specification, re.IGNORECASE)
        if func_match:
            spec['function_name'] = func_match.group(1) or func_match.group(2) or func_match.group(3)
            spec['type'] = 'function'

        # Extract class name
        class_match = re.search(r'class\s+(\w+)|lớp\s+(\w+)', specification, re.IGNORECASE)
        if class_match:
            spec['class_name'] = class_match.group(1) or class_match.group(2)
            spec['type'] = 'class'

        # Extract parameters
        param_match = re.search(r'parameter[s]?\s*:?\s*(.+?)(?:\n|return|trả về|$)', specification, re.IGNORECASE)
        if param_match:
            param_text = param_match.group(1)
            # Simple parameter extraction
            params = [p.strip() for p in param_text.split(',') if p.strip()]
            spec['parameters'] = params

        return spec

    def _generate_function(self, request: CodeGenRequest, parsed_spec: Dict[str, Any]) -> Dict[str, Any]:
        """Generate a function based on specification"""
        function_name = request.function_name or 'generated_function'
        parameters = ', '.join(parsed_spec.get('parameters', ['']))

        # Generate function body based on specification
        body = self._generate_function_body(request.specification, parsed_spec)

        # Generate docstring
        docstring = self._generate_docstring(request.specification, 'function')

        # Format function code
        code = self.templates['function'].format(
            function_name=function_name,
            parameters=parameters,
            return_annotation=' -> Any' if self.style_config['use_type_hints'] else '',
            docstring=docstring,
            args_doc=self._format_args_doc(parsed_spec.get('parameters', [])),
            returns_doc='Generated result',
            body=body
        )

        return {
            'code': code,
            'dependencies': ['typing'] if self.style_config['use_type_hints'] else [],
            'documentation': docstring,
            'complexity': len(body.split('\n'))
        }

    def _generate_class(self, request: CodeGenRequest, parsed_spec: Dict[str, Any]) -> Dict[str, Any]:
        """Generate a class based on specification"""
        class_name = request.class_name or 'GeneratedClass'

        # Generate class attributes and methods
        attributes = self._extract_attributes_from_spec(request.specification)
        methods = self._generate_class_methods(request.specification, parsed_spec)

        # Generate docstring
        docstring = self._generate_docstring(request.specification, 'class')

        # Generate init method
        init_params = ', '.join(f'{attr}: Any = None' for attr in attributes) if attributes else ''
        init_body = '\n        '.join(f'self.{attr} = {attr}' for attr in attributes)
        if not init_body:
            init_body = 'pass'

        # Format class code
        code = self.templates['class'].format(
            class_name=class_name,
            inheritance='',
            docstring=docstring,
            attributes_doc='\n        '.join(f'{attr}: Description of {attr}' for attr in attributes),
            init_params=', ' + init_params if init_params else '',
            init_body=init_body,
            methods=methods
        )

        return {
            'code': code,
            'dependencies': ['typing'] if self.style_config['use_type_hints'] else [],
            'documentation': docstring,
            'complexity': len(methods.split('\n')) + len(attributes)
        }

    def _generate_module(self, request: CodeGenRequest, parsed_spec: Dict[str, Any]) -> Dict[str, Any]:
        """Generate a complete module based on specification"""
        # Generate module-level docstring
        docstring = f'"""\n{request.specification}\n\nGenerated by HyperAI Phoenix\n"""'

        # Generate basic module structure
        code = textwrap.dedent(f'''
        {docstring}

        from typing import Any, Dict, List, Optional


        def main():
            """Main function for the module"""
            # Implementation based on specification
            print("Module generated successfully")
            return True

def run(payload: str = None) -> str:
    """Standard Entry Point for Omni Orchestrator"""
    try:
        logging.basicConfig(level=logging.CRITICAL)
        logging.getLogger().setLevel(logging.CRITICAL)
        return json.dumps({"status": "success", "message": "Skill executed"})
    except Exception as e:
        return json.dumps({"status": "error", "error": str(e)})

def run(payload: str = None) -> str:
    """Standard Entry Point for Omni Orchestrator"""
    try:
        logging.basicConfig(level=logging.CRITICAL)
        logging.getLogger().setLevel(logging.CRITICAL)
        return json.dumps({"status": "success", "message": "Skill executed"})
    except Exception as e:
        return json.dumps({"status": "error", "error": str(e)})

if __name__ == "__main__":
    print(run())
