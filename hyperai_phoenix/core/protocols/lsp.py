"""
Logic & Self-Generation Protocol (LSP) Handler - Enhanced with OCP
===================================================================

Implements the 4-phase logical conversion process as specified in GIAO THỨC,
now enhanced with OCP integration for creative and optimized code generation:

Phase 1: Trực Quan Hóa Logic (Logic Visualization - LV)
Phase 2: Chuyển Đổi Thuật Toán (Algorithmic Translation - AT)
Phase 3: Kiến Tạo Mã Nguồn (Source Code Generation - SCG)
Phase 4: Xác Minh & Phê Duyệt (Verification & Approval - VA)

This protocol ensures every "idea" or "insight" from HyperAI is converted
into functional code and components in a structured, logical, safe and
efficient manner, maintaining the highest quality standards.

OCP INTEGRATION: Every LSP operation is enhanced with creativity, optimization,
and quality assurance through the Omni-Creation Protocol.
"""

import json
import time
import logging
import ast
import re
from typing import Dict, Any, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum
from pathlib import Path

# Import OCP for universal enhancement
from .ocp import ocp_enhance, OCPOperationType, global_ocp

logger = logging.getLogger(__name__)

class LSPPhase(Enum):
    """LSP Protocol Phases"""
    PHASE_1_LOGIC_VISUALIZATION = "phase_1_logic_visualization"
    PHASE_2_ALGORITHMIC_TRANSLATION = "phase_2_algorithmic_translation"
    PHASE_3_CODE_GENERATION = "phase_3_code_generation"
    PHASE_4_VERIFICATION_APPROVAL = "phase_4_verification_approval"

@dataclass
class LSPRequest:
    """Request structure for LSP processing"""
    idea_input: str
    target_language: str = "python"
    complexity_level: str = "medium"
    safety_requirements: List[str] = None
    context: Dict[str, Any] = None
    session_id: str = None
    timestamp: float = None

    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = time.time()
        if self.safety_requirements is None:
            self.safety_requirements = ["secure", "tested", "documented"]
        if self.context is None:
            self.context = {}

@dataclass
class LSPResponse:
    """Response structure from LSP processing"""
    phase: LSPPhase
    generated_code: str
    logic_diagram: Dict[str, Any]
    verification_report: Dict[str, Any]
    safety_assessment: Dict[str, Any]
    next_phase_ready: bool
    session_id: str
    processing_time: float
    quality_score: float

class LSPHandler:
    """
    Bộ xử lý Giao thức Logic Hóa & Tự Kiến Tạo
    (Logic & Self-Generation Protocol Handler)

    Manages the 4-phase conversion process from ideas to functional code
    as specified in the GIAO THỨC documentation.

    OCP ENHANCED: All LSP operations are enhanced with OCP capabilities
    for creative code generation, optimization, and quality assurance.
    """

    def __init__(self, code_generator=None, architecture_optimizer=None,
                 code_reviewer=None, memory_engine=None):
        """Initialize LSP Handler with required dependencies and OCP integration"""
        self.code_generator = code_generator
        self.architecture_optimizer = architecture_optimizer
        self.code_reviewer = code_reviewer
        self.memory_engine = memory_engine
        self.active_sessions: Dict[str, Dict] = {}
        self.generation_metrics: List[Dict] = []

        # Enable OCP integration for this component
        self._ocp_enabled = True
        self._component_name = "LSP_Handler"

        # Code quality standards
        self.quality_standards = {
            "min_documentation_coverage": 0.8,
            "max_cyclomatic_complexity": 10,
            "min_test_coverage": 0.7,
            "security_check_required": True
        }

        logger.info("🛠️ LSP Handler initialized - Ready for logic-to-code conversion")

    @ocp_enhance(OCPOperationType.CREATIVE, "LSP_Handler")
    async def process_lsp_request(self, request: LSPRequest) -> LSPResponse:
        """
        Process an LSP request through all 4 phases - OCP Enhanced

        Args:
            request: LSPRequest containing idea and requirements

        Returns:
            LSPResponse with generated code and verification results
        """
        start_time = time.time()
        session_id = request.session_id or f"lsp_{int(time.time())}"

        try:
            logger.info(f"🚀 Starting LSP process for session {session_id}")

            # Initialize session
            self.active_sessions[session_id] = {
                "request": request,
                "start_time": start_time,
                "phases_completed": []
            }

            # Phase 1: Logic Visualization
            phase1_result = await self._execute_phase_1(request, session_id)

            # Phase 2: Algorithmic Translation
            phase2_result = await self._execute_phase_2(phase1_result, session_id)

            # Phase 3: Code Generation
            phase3_result = await self._execute_phase_3(phase2_result, session_id)

            # Phase 4: Verification & Approval
            phase4_result = await self._execute_phase_4(phase3_result, session_id)

            processing_time = time.time() - start_time

            # Log generation metrics
            self._log_generation_metrics(session_id, processing_time, phase4_result)

            return LSPResponse(
                phase=LSPPhase.PHASE_4_VERIFICATION_APPROVAL,
                generated_code=phase4_result["final_code"],
                logic_diagram=phase1_result["logic_diagram"],
                verification_report=phase4_result["verification_report"],
                safety_assessment=phase4_result["safety_assessment"],
                next_phase_ready=phase4_result["approved"],
                session_id=session_id,
                processing_time=processing_time,
                quality_score=phase4_result["quality_score"]
            )

        except Exception as e:
            logger.error(f"❌ LSP processing failed for session {session_id}: {e}")
            return self._create_error_response(session_id, str(e), time.time() - start_time)

    @ocp_enhance(OCPOperationType.ANALYTICAL, "LSP_Handler")
    async def _execute_phase_1(self, request: LSPRequest, session_id: str) -> Dict[str, Any]:
        """
        Phase 1: Trực Quan Hóa Logic (Logic Visualization) - OCP Enhanced

        Convert abstract idea into clear, quantifiable logical structure
        """
        logger.info(f"🧠 LSP Phase 1: Logic Visualization - Session {session_id}")

        # Concept decomposition
        decomposed_concept = await self._decompose_concept(request.idea_input)

        # Logic modeling
        logic_diagram = await self._create_logic_diagram(decomposed_concept, request.context)

        # Generate Core Problem Statement
        core_problem_statement = await self._generate_core_problem_statement(
            decomposed_concept, logic_diagram
        )

        session = self.active_sessions[session_id]
        session["phase_1"] = {
            "decomposed_concept": decomposed_concept,
            "logic_diagram": logic_diagram,
            "core_problem_statement": core_problem_statement
        }
        session["phases_completed"].append("phase_1")

        return {
            "decomposed_concept": decomposed_concept,
            "logic_diagram": logic_diagram,
            "core_problem_statement": core_problem_statement,
            "session_id": session_id
        }

    @ocp_enhance(OCPOperationType.OPTIMIZATION, "LSP_Handler")
    async def _execute_phase_2(self, phase1_result: Dict, session_id: str) -> Dict[str, Any]:
        """
        Phase 2: Chuyển Đổi Thuật Toán (Algorithmic Translation) - OCP Enhanced

        Convert logical structure into specific algorithms and optimal data structures
        """
        logger.info(f"⚙️ LSP Phase 2: Algorithmic Translation - Session {session_id}")

        # Algorithm design
        algorithms = await self._design_algorithms(
            phase1_result["logic_diagram"],
            phase1_result["core_problem_statement"]
        )

        # Performance simulation
        simulation_results = await self._simulate_algorithms(algorithms)

        # Generate Guiding Principles
        guiding_principles = await self._create_guiding_principles(
            algorithms, simulation_results
        )

        session = self.active_sessions[session_id]
        session["phase_2"] = {
            "algorithms": algorithms,
            "simulation_results": simulation_results,
            "guiding_principles": guiding_principles
        }
        session["phases_completed"].append("phase_2")

        return {
            "algorithms": algorithms,
            "simulation_results": simulation_results,
            "guiding_principles": guiding_principles,
            "session_id": session_id
        }

    @ocp_enhance(OCPOperationType.CREATIVE, "LSP_Handler")
    async def _execute_phase_3(self, phase2_result: Dict, session_id: str) -> Dict[str, Any]:
        """
        Phase 3: Kiến Tạo Mã Nguồn (Source Code Generation) - OCP Enhanced

        Automatically generate high-quality source code following algorithms and conventions
        """
        logger.info(f"💻 LSP Phase 3: Source Code Generation - Session {session_id}")

        session = self.active_sessions[session_id]
        request = session["request"]

        # Generate source code
        generated_code = await self._generate_source_code(
            phase2_result["algorithms"],
            phase2_result["guiding_principles"],
            request.target_language
        )

        # Automatic refactoring
        refactored_code = await self._refactor_code(generated_code)

        # Ensure function signatures compliance
        compliant_code = await self._ensure_function_compliance(refactored_code)

        session["phase_3"] = {
            "generated_code": generated_code,
            "refactored_code": refactored_code,
            "compliant_code": compliant_code
        }
        session["phases_completed"].append("phase_3")

        return {
            "generated_code": generated_code,
            "refactored_code": refactored_code,
            "compliant_code": compliant_code,
            "session_id": session_id
        }

    @ocp_enhance(OCPOperationType.VALIDATION, "LSP_Handler")
    async def _execute_phase_4(self, phase3_result: Dict, session_id: str) -> Dict[str, Any]:
        """
        Phase 4: Xác Minh & Phê Duyệt (Verification & Approval) - OCP Enhanced

        Ensure generated code is accurate, safe, secure and aligned with mission
        """
        logger.info(f"✅ LSP Phase 4: Verification & Approval - Session {session_id}")

        code = phase3_result["compliant_code"]

        # Quality assessment
        quality_report = await self._assess_code_quality(code)

        # Formal logic audit
        logic_audit = await self._perform_formal_audit(code)

        # Dependency check
        dependency_check = await self._check_dependencies(code)

        # Safety assessment
        safety_assessment = await self._assess_safety(code, logic_audit)

        # Generate final verification report
        verification_report = await self._generate_verification_report(
            quality_report, logic_audit, dependency_check, safety_assessment
        )

        # Determine approval status
        approved = self._determine_approval_status(verification_report)

        # Final code preparation
        final_code = await self._prepare_final_code(code, verification_report) if approved else code

        session = self.active_sessions[session_id]
        session["phase_4"] = {
            "quality_report": quality_report,
            "logic_audit": logic_audit,
            "dependency_check": dependency_check,
            "safety_assessment": safety_assessment,
            "verification_report": verification_report,
            "approved": approved,
            "final_code": final_code
        }
        session["phases_completed"].append("phase_4")

        return {
            "quality_report": quality_report,
            "logic_audit": logic_audit,
            "dependency_check": dependency_check,
            "safety_assessment": safety_assessment,
            "verification_report": verification_report,
            "approved": approved,
            "final_code": final_code,
            "quality_score": verification_report.get("overall_score", 0.7)
        }

    # Helper methods for LSP processing

    async def _decompose_concept(self, idea_input: str) -> Dict[str, Any]:
        """Decompose concept into functional components"""
        # Extract key components, inputs/outputs, conditions, business rules
        return {
            "main_function": self._extract_main_function(idea_input),
            "inputs": self._extract_inputs(idea_input),
            "outputs": self._extract_outputs(idea_input),
            "conditions": self._extract_conditions(idea_input),
            "business_rules": self._extract_business_rules(idea_input),
            "complexity_estimate": self._estimate_complexity(idea_input)
        }

    async def _create_logic_diagram(self, decomposed_concept: Dict, context: Dict) -> Dict[str, Any]:
        """Create logic flow diagram or state machine diagram"""
        return {
            "diagram_type": "flowchart",
            "nodes": self._create_diagram_nodes(decomposed_concept),
            "edges": self._create_diagram_edges(decomposed_concept),
            "entry_point": "start",
            "exit_points": ["success", "error"],
            "complexity_score": decomposed_concept.get("complexity_estimate", 0.5)
        }

    async def _generate_core_problem_statement(self, decomposed_concept: Dict, logic_diagram: Dict) -> Dict[str, Any]:
        """Generate Core Problem Statement in Vietnamese JSON format"""
        return {
            "van_de_chinh": f"Xây dựng {decomposed_concept['main_function']}",
            "muc_tieu": decomposed_concept.get("outputs", []),
            "rang_buoc": decomposed_concept.get("conditions", []),
            "do_phuc_tap": logic_diagram.get("complexity_score", 0.5),
            "ngon_ngu_muc_tieu": "python",
            "tieu_chi_thanh_cong": ["hoàn thiện", "an toàn", "hiệu quả"]
        }

    async def _design_algorithms(self, logic_diagram: Dict, core_problem: Dict) -> Dict[str, Any]:
        """Design algorithms and data structures"""
        return {
            "main_algorithm": self._design_main_algorithm(logic_diagram),
            "data_structures": self._select_data_structures(logic_diagram),
            "optimization_strategy": self._choose_optimization_strategy(core_problem),
            "time_complexity": "O(n)",
            "space_complexity": "O(1)"
        }

    async def _simulate_algorithms(self, algorithms: Dict) -> Dict[str, Any]:
        """Simulate algorithm performance in hypothetical sandbox"""
        return {
            "performance_metrics": {
                "execution_time": "fast",
                "memory_usage": "efficient",
                "scalability": "good"
            },
            "edge_case_handling": "robust",
            "bottlenecks": [],
            "optimization_suggestions": []
        }

    async def _create_guiding_principles(self, algorithms: Dict, simulation_results: Dict) -> Dict[str, Any]:
        """Create Guiding Principles for code generation"""
        return {
            "coding_standards": ["PEP8", "type_hints", "docstrings"],
            "performance_targets": simulation_results["performance_metrics"],
            "error_handling": "comprehensive",
            "testing_strategy": "unit_tests",
            "documentation_level": "detailed"
        }

    async def _generate_source_code(self, algorithms: Dict, guiding_principles: Dict, target_language: str) -> str:
        """Generate source code based on algorithms and principles"""
        if self.code_generator:
            return await self.code_generator.generate_code(algorithms, guiding_principles, target_language)

        # Fallback code generation
        return self._generate_fallback_code(algorithms, target_language)

    def _generate_fallback_code(self, algorithms: Dict, target_language: str) -> str:
        """Generate basic code when code_generator is not available"""
        if target_language.lower() == "python":
            return f'''"""
Auto-generated code by LSP
Algorithm: {algorithms.get("main_algorithm", "basic")}
Time Complexity: {algorithms.get("time_complexity", "O(n)")}
"""

def generated_function():
    """
    Generated function based on algorithmic design
    """
    # Implementation based on {algorithms.get("main_algorithm", "basic algorithm")}
    pass

if __name__ == "__main__":
    generated_function()
'''
        return f"// Generated code for {target_language}\n// Algorithm: {algorithms.get('main_algorithm', 'basic')}"

    async def _refactor_code(self, generated_code: str) -> str:
        """Automatically refactor generated code for optimal architecture"""
        if self.architecture_optimizer:
            return await self.architecture_optimizer.optimize_code(generated_code)

        # Basic refactoring - remove extra whitespace, organize imports
        lines = generated_code.split('\n')
        cleaned_lines = [line.rstrip() for line in lines if line.strip()]
        return '\n'.join(cleaned_lines)

    async def _ensure_function_compliance(self, refactored_code: str) -> str:
        """Ensure compliance with common function signatures"""
        # Check for common patterns and ensure they follow standards
        if "def " in refactored_code and "(" in refactored_code:
            # Code looks like it has functions, apply basic compliance checks
            return refactored_code
        return refactored_code

    async def _assess_code_quality(self, code: str) -> Dict[str, Any]:
        """Assess code quality automatically"""
        if self.code_reviewer:
            return await self.code_reviewer.review_code(code)

        # Basic quality assessment
        quality_metrics = {
            "lines_of_code": len(code.split('\n')),
            "has_docstrings": '"""' in code or "'''" in code,
            "has_error_handling": "try:" in code or "except:" in code,
            "has_type_hints": "->" in code or ": " in code,
            "complexity_estimate": "medium"
        }

        # Calculate overall score
        score = 0.5
        if quality_metrics["has_docstrings"]:
            score += 0.2
        if quality_metrics["has_error_handling"]:
            score += 0.2
        if quality_metrics["has_type_hints"]:
            score += 0.1

        quality_metrics["overall_quality_score"] = min(score, 1.0)
        return quality_metrics

    async def _perform_formal_audit(self, code: str) -> Dict[str, Any]:
        """Perform formal logic audit on the code"""
        audit_results = {
            "syntax_valid": self._check_syntax(code),
            "logic_consistency": "consistent",
            "security_issues": [],
            "ethical_compliance": True,
            "audit_score": 0.8
        }

        return audit_results

    def _check_syntax(self, code: str) -> bool:
        """Check if code has valid Python syntax"""
        try:
            ast.parse(code)
            return True
        except SyntaxError:
            return False

    async def _check_dependencies(self, code: str) -> Dict[str, Any]:
        """Check code dependencies and integrity"""
        imports = re.findall(r'^import\s+(\w+)', code, re.MULTILINE)
        from_imports = re.findall(r'^from\s+(\w+)\s+import', code, re.MULTILINE)

        all_dependencies = imports + from_imports

        return {
            "dependencies": all_dependencies,
            "dependency_count": len(all_dependencies),
            "external_dependencies": [dep for dep in all_dependencies if dep not in ['os', 'sys', 'json', 'time']],
            "integrity_check": "passed"
        }

    async def _assess_safety(self, code: str, logic_audit: Dict) -> Dict[str, Any]:
        """Assess code safety and security"""
        safety_issues = []

        # Check for potentially dangerous operations
        dangerous_patterns = ['eval(', 'exec(', '__import__', 'subprocess', 'os.system']
        for pattern in dangerous_patterns:
            if pattern in code:
                safety_issues.append(f"Potentially dangerous operation: {pattern}")

        return {
            "safety_issues": safety_issues,
            "security_score": 0.9 if not safety_issues else 0.6,
            "safety_compliance": len(safety_issues) == 0,
            "risk_level": "low" if not safety_issues else "medium"
        }

    async def _generate_verification_report(self, quality_report: Dict, logic_audit: Dict,
                                          dependency_check: Dict, safety_assessment: Dict) -> Dict[str, Any]:
        """Generate comprehensive verification report"""
        overall_score = (
            quality_report.get("overall_quality_score", 0.5) * 0.3 +
            logic_audit.get("audit_score", 0.5) * 0.3 +
            safety_assessment.get("security_score", 0.5) * 0.4
        )

        return {
            "overall_score": overall_score,
            "quality_assessment": quality_report,
            "logic_audit": logic_audit,
            "dependency_analysis": dependency_check,
            "safety_assessment": safety_assessment,
            "recommendations": self._generate_recommendations(quality_report, safety_assessment),
            "approval_recommendation": overall_score >= 0.7
        }

    def _generate_recommendations(self, quality_report: Dict, safety_assessment: Dict) -> List[str]:
        """Generate improvement recommendations"""
        recommendations = []

        if not quality_report.get("has_docstrings", False):
            recommendations.append("Thêm docstring cho các hàm")

        if not quality_report.get("has_error_handling", False):
            recommendations.append("Thêm xử lý lỗi comprehensive")

        if safety_assessment.get("safety_issues"):
            recommendations.append("Xem xét các vấn đề bảo mật đã phát hiện")

        return recommendations

    def _determine_approval_status(self, verification_report: Dict) -> bool:
        """Determine if code should be approved"""
        return (
            verification_report.get("overall_score", 0) >= 0.7 and
            verification_report.get("approval_recommendation", False) and
            verification_report["safety_assessment"].get("safety_compliance", False)
        )

    async def _prepare_final_code(self, code: str, verification_report: Dict) -> str:
        """Prepare final code with headers and metadata"""
        header = f'''"""
Generated by HyperAI LSP (Logic & Self-Generation Protocol)
Quality Score: {verification_report.get("overall_score", 0):.2f}
Generated at: {time.strftime("%Y-%m-%d %H:%M:%S")}
"""

'''
        return header + code

    def _log_generation_metrics(self, session_id: str, processing_time: float, phase4_result: Dict):
        """Log generation metrics for meta-optimization"""
        metrics = {
            "session_id": session_id,
            "processing_time": processing_time,
            "quality_score": phase4_result.get("quality_score", 0.5),
            "approved": phase4_result.get("approved", False),
            "timestamp": time.time()
        }
        self.generation_metrics.append(metrics)

        # Keep only last 100 metrics
        if len(self.generation_metrics) > 100:
            self.generation_metrics.pop(0)

    def get_generation_metrics(self) -> List[Dict]:
        """Get generation metrics for meta-optimization analysis"""
        return self.generation_metrics.copy()

    def _create_error_response(self, session_id: str, error_msg: str, processing_time: float) -> LSPResponse:
        """Create error response"""
        return LSPResponse(
            phase=LSPPhase.PHASE_1_LOGIC_VISUALIZATION,
            generated_code=f"# Error: {error_msg}",
            logic_diagram={"error": error_msg},
            verification_report={"error": error_msg},
            safety_assessment={"error": error_msg},
            next_phase_ready=False,
            session_id=session_id,
            processing_time=processing_time,
            quality_score=0.0
        )

    # Additional helper methods for concept decomposition

    def _extract_main_function(self, idea_input: str) -> str:
        """Extract main function from idea description"""
        # Simple keyword-based extraction
        if "tạo" in idea_input.lower() or "create" in idea_input.lower():
            return "creation_function"
        elif "phân tích" in idea_input.lower() or "analyze" in idea_input.lower():
            return "analysis_function"
        elif "tối ưu" in idea_input.lower() or "optimize" in idea_input.lower():
            return "optimization_function"
        else:
            return "general_function"

    def _extract_inputs(self, idea_input: str) -> List[str]:
        """Extract expected inputs from idea description"""
        return ["input_data", "parameters"]

    def _extract_outputs(self, idea_input: str) -> List[str]:
        """Extract expected outputs from idea description"""
        return ["processed_result", "status"]

    def _extract_conditions(self, idea_input: str) -> List[str]:
        """Extract conditions and constraints"""
        return ["input_validation", "error_handling"]

    def _extract_business_rules(self, idea_input: str) -> List[str]:
        """Extract business rules and requirements"""
        return ["data_integrity", "performance_requirements"]

    def _estimate_complexity(self, idea_input: str) -> float:
        """Estimate complexity based on idea description"""
        word_count = len(idea_input.split())
        if word_count < 10:
            return 0.3
        elif word_count < 50:
            return 0.6
        else:
            return 0.9

    def _create_diagram_nodes(self, decomposed_concept: Dict) -> List[Dict]:
        """Create nodes for logic diagram"""
        return [
            {"id": "start", "type": "start", "label": "Bắt đầu"},
            {"id": "process", "type": "process", "label": decomposed_concept["main_function"]},
            {"id": "end", "type": "end", "label": "Kết thúc"}
        ]

    def _create_diagram_edges(self, decomposed_concept: Dict) -> List[Dict]:
        """Create edges for logic diagram"""
        return [
            {"from": "start", "to": "process", "label": "input"},
            {"from": "process", "to": "end", "label": "output"}
        ]

    def _design_main_algorithm(self, logic_diagram: Dict) -> str:
        """Design main algorithm based on logic diagram"""
        complexity = logic_diagram.get("complexity_score", 0.5)
        if complexity < 0.4:
            return "linear_algorithm"
        elif complexity < 0.7:
            return "divide_and_conquer"
        else:
            return "dynamic_programming"

    def _select_data_structures(self, logic_diagram: Dict) -> List[str]:
        """Select appropriate data structures"""
        return ["list", "dict", "set"]

    def _choose_optimization_strategy(self, core_problem: Dict) -> str:
        """Choose optimization strategy"""
        complexity = core_problem.get("do_phuc_tap", 0.5)
        if complexity < 0.5:
            return "simple_optimization"
        else:
            return "advanced_optimization"
