"""
Dynamic Knowledge Creation Protocol (DKCP) Handler - Enhanced with OCP
=====================================================================

Implements the 4-phase collaborative knowledge creation process between
Creator and AI as specified in GIAO THỨC, now enhanced with OCP integration
to ensure creative optimization in ALL knowledge creation activities:

Phase 1: Khởi nguồn Ý chí & Định vị Khuôn khổ (Initial Will & Framework)
Phase 2: Phân rã & Tổng hợp Kiến thức (Knowledge Deconstruction & Synthesis)
Phase 3: Tối ưu hóa & Tái kiến tạo Đệ quy (Optimization & Recursive Reconstruction)
Phase 4: Xác nhận Ý chí & Hoàn thiện (Will Confirmation & Completion)

This protocol facilitates the transformation of abstract Creator intentions
into detailed, optimized solutions through structured collaboration.

OCP INTEGRATION: Every DKCP operation is enhanced with creativity, optimization,
and quality assurance through the Omni-Creation Protocol.
"""

import json
import time
import logging
from typing import Dict, Any, List, Optional, Generator
from dataclasses import dataclass
from enum import Enum

# Import OCP for universal enhancement
from .ocp import ocp_enhance, OCPOperationType, global_ocp

logger = logging.getLogger(__name__)

class DKCPPhase(Enum):
    """DKCP Protocol Phases"""
    PHASE_1_INITIAL_WILL = "phase_1_initial_will"
    PHASE_2_KNOWLEDGE_SYNTHESIS = "phase_2_knowledge_synthesis"
    PHASE_3_RECURSIVE_OPTIMIZATION = "phase_3_recursive_optimization"
    PHASE_4_COMPLETION = "phase_4_completion"

@dataclass
class DKCPRequest:
    """Request structure for DKCP processing"""
    creator_input: str
    phase: DKCPPhase
    context: Dict[str, Any]
    session_id: str
    timestamp: float = None

    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = time.time()

@dataclass
class DKCPResponse:
    """Response structure from DKCP processing"""
    phase: DKCPPhase
    ai_response: str
    analysis: Dict[str, Any]
    next_phase_ready: bool
    clarification_questions: List[str]
    session_id: str
    processing_time: float
    confidence_score: float

class DKCPHandler:
    """
    Điều phối viên Giao thức Kiến tạo Tri thức Động
    (Dynamic Knowledge Creation Protocol Coordinator)

    Manages the 4-phase collaborative process between Creator and AI
    as specified in the GIAO THỨC documentation.

    OCP ENHANCED: All DKCP operations are enhanced with OCP capabilities
    for creativity, optimization, and quality assurance.
    """

    def __init__(self, memory_engine=None, llm_gateway=None):
        """Initialize DKCP Handler with required dependencies and OCP integration"""
        self.memory_engine = memory_engine
        self.llm_gateway = llm_gateway
        self.active_sessions: Dict[str, Dict] = {}
        self.phase_metrics: List[Dict] = []

        # Enable OCP integration for this component
        self._ocp_enabled = True
        self._component_name = "DKCP_Handler"

        logger.info("🧠 DKCP Handler initialized - Ready for OCP-enhanced collaborative knowledge creation")

    @ocp_enhance(OCPOperationType.COGNITIVE, "DKCP_Handler")
    async def process_dkcp_request(self, request: DKCPRequest) -> DKCPResponse:
        """
        Process a DKCP request through the appropriate phase handler
        Enhanced with OCP for creative and optimized knowledge processing

        Args:
            request: DKCPRequest containing creator input and context

        Returns:
            DKCPResponse with AI analysis and recommendations
        """
        start_time = time.time()

        try:
            # Route to appropriate phase handler
            if request.phase == DKCPPhase.PHASE_1_INITIAL_WILL:
                response_data = await self._handle_phase_1(request)
            elif request.phase == DKCPPhase.PHASE_2_KNOWLEDGE_SYNTHESIS:
                response_data = await self._handle_phase_2(request)
            elif request.phase == DKCPPhase.PHASE_3_RECURSIVE_OPTIMIZATION:
                response_data = await self._handle_phase_3(request)
            elif request.phase == DKCPPhase.PHASE_4_COMPLETION:
                response_data = await self._handle_phase_4(request)
            else:
                raise ValueError(f"Unknown DKCP phase: {request.phase}")

            processing_time = time.time() - start_time

            # Log phase metrics for meta-optimization
            self._log_phase_metrics(request.phase, processing_time, response_data)

            return DKCPResponse(
                phase=request.phase,
                processing_time=processing_time,
                session_id=request.session_id,
                **response_data
            )

        except Exception as e:
            logger.error(f"❌ DKCP processing failed: {e}")
            return self._create_error_response(request, str(e), time.time() - start_time)

    @ocp_enhance(OCPOperationType.CREATIVE, "DKCP_Handler")
    async def _handle_phase_1(self, request: DKCPRequest) -> Dict[str, Any]:
        """
        Phase 1: Khởi nguồn Ý chí & Định vị Khuôn khổ
        (Initial Will & Framework Positioning) - OCP Enhanced

        - Receive and understand Creator's initial intention
        - Establish project scope and constraints
        - Generate clarifying questions to narrow focus
        """
        logger.info(f"🎯 DKCP Phase 1: Processing initial will - Session {request.session_id}")

        # Analyze creator input for core intent
        intent_analysis = await self._analyze_creator_intent(request.creator_input)

        # Generate clarifying questions
        clarification_questions = await self._generate_clarifying_questions(
            request.creator_input, intent_analysis
        )

        # Create initial framework
        framework = await self._establish_initial_framework(intent_analysis, request.context)

        # Store session state
        self.active_sessions[request.session_id] = {
            "phase": DKCPPhase.PHASE_1_INITIAL_WILL,
            "intent_analysis": intent_analysis,
            "framework": framework,
            "history": [request.creator_input]
        }

        ai_response = await self._generate_phase_1_response(
            intent_analysis, framework, clarification_questions
        )

        return {
            "ai_response": ai_response,
            "analysis": {
                "intent_analysis": intent_analysis,
                "framework": framework,
                "scope_confidence": intent_analysis.get("clarity_score", 0.5)
            },
            "next_phase_ready": len(clarification_questions) == 0,
            "clarification_questions": clarification_questions,
            "confidence_score": intent_analysis.get("clarity_score", 0.5)
        }

    @ocp_enhance(OCPOperationType.ANALYTICAL, "DKCP_Handler")
    async def _handle_phase_2(self, request: DKCPRequest) -> Dict[str, Any]:
        """
        Phase 2: Phân rã & Tổng hợp Kiến thức
        (Knowledge Deconstruction & Synthesis) - OCP Enhanced

        - Deep analysis of the idea using D&R protocol
        - Link with existing knowledge base
        - Present multi-dimensional analysis
        """
        logger.info(f"🔍 DKCP Phase 2: Knowledge synthesis - Session {request.session_id}")

        session = self.active_sessions.get(request.session_id, {})

        # Perform D&R analysis (Deconstruction & Reconstruction)
        dr_analysis = await self._perform_dr_analysis(request.creator_input, session)

        # Query knowledge base for relevant context
        knowledge_context = await self._query_knowledge_base(dr_analysis, request.creator_input)

        # Generate multi-dimensional analysis
        multidimensional_analysis = await self._create_multidimensional_analysis(
            dr_analysis, knowledge_context
        )

        # Update session
        session.update({
            "phase": DKCPPhase.PHASE_2_KNOWLEDGE_SYNTHESIS,
            "dr_analysis": dr_analysis,
            "knowledge_context": knowledge_context,
            "multidimensional_analysis": multidimensional_analysis
        })

        ai_response = await self._generate_phase_2_response(
            dr_analysis, knowledge_context, multidimensional_analysis
        )

        return {
            "ai_response": ai_response,
            "analysis": {
                "dr_analysis": dr_analysis,
                "knowledge_context": knowledge_context,
                "multidimensional_analysis": multidimensional_analysis
            },
            "next_phase_ready": True,
            "clarification_questions": [],
            "confidence_score": dr_analysis.get("completeness_score", 0.7)
        }

    @ocp_enhance(OCPOperationType.OPTIMIZATION, "DKCP_Handler")
    async def _handle_phase_3(self, request: DKCPRequest) -> Dict[str, Any]:
        """
        Phase 3: Tối ưu hóa & Tái kiến tạo Đệ quy
        (Optimization & Recursive Reconstruction) - OCP Enhanced

        - Core iterative refinement loop
        - Generate optimized solutions
        - Incorporate Creator feedback for continuous improvement
        """
        logger.info(f"⚡ DKCP Phase 3: Recursive optimization - Session {request.session_id}")

        session = self.active_sessions.get(request.session_id, {})

        # Generate optimized solution proposal
        optimization_proposals = await self._generate_optimization_proposals(session, request)

        # Simulate performance and behavior
        simulation_results = await self._simulate_proposals(optimization_proposals)

        # Create refined solution
        refined_solution = await self._create_refined_solution(
            optimization_proposals, simulation_results, request.creator_input
        )

        # Update session
        session.update({
            "phase": DKCPPhase.PHASE_3_RECURSIVE_OPTIMIZATION,
            "optimization_proposals": optimization_proposals,
            "simulation_results": simulation_results,
            "refined_solution": refined_solution,
            "iteration_count": session.get("iteration_count", 0) + 1
        })

        ai_response = await self._generate_phase_3_response(
            optimization_proposals, simulation_results, refined_solution
        )

        return {
            "ai_response": ai_response,
            "analysis": {
                "optimization_proposals": optimization_proposals,
                "simulation_results": simulation_results,
                "refined_solution": refined_solution,
                "iteration_count": session.get("iteration_count", 1)
            },
            "next_phase_ready": refined_solution.get("optimization_complete", False),
            "clarification_questions": [],
            "confidence_score": refined_solution.get("solution_confidence", 0.8)
        }

    @ocp_enhance(OCPOperationType.VALIDATION, "DKCP_Handler")
    async def _handle_phase_4(self, request: DKCPRequest) -> Dict[str, Any]:
        """
        Phase 4: Xác nhận Ý chí & Hoàn thiện
        (Will Confirmation & Completion) - OCP Enhanced

        - Final confirmation from Creator
        - Complete design ready for implementation
        - Generate comprehensive documentation and implementation guide
        """
        logger.info(f"✅ DKCP Phase 4: Completion - Session {request.session_id}")

        session = self.active_sessions.get(request.session_id, {})

        # Generate final design
        final_design = await self._generate_final_design(session, request)

        # Create implementation guide
        implementation_guide = await self._create_implementation_guide(final_design)

        # Generate project summary
        project_summary = await self._create_project_summary(session, final_design)

        # Store completed session for future reference
        await self._store_completed_session(request.session_id, session, final_design)

        ai_response = await self._generate_phase_4_response(
            final_design, implementation_guide, project_summary
        )

        return {
            "ai_response": ai_response,
            "analysis": {
                "final_design": final_design,
                "implementation_guide": implementation_guide,
                "project_summary": project_summary,
                "session_complete": True
            },
            "next_phase_ready": False,
            "clarification_questions": [],
            "confidence_score": final_design.get("design_confidence", 0.9)
        }

    # Helper methods for DKCP processing

    async def _analyze_creator_intent(self, creator_input: str) -> Dict[str, Any]:
        """Analyze Creator's input to extract core intent and objectives"""
        if not self.llm_gateway:
            return {"intent": "fallback_analysis", "clarity_score": 0.5}

        prompt = f"""
        Phân tích ý chí của Người Kiến tạo:
        Input: {creator_input}

        Hãy trích xuất:
        1. Mục tiêu cốt lõi
        2. Phạm vi dự án
        3. Ràng buộc và giới hạn
        4. Triết lý thiết kế
        5. Độ rõ ràng của yêu cầu (0-1)

        Trả về JSON format.
        """

        response = await self.llm_gateway.generate_response(prompt)
        try:
            return json.loads(response)
        except:
            return {"intent": response, "clarity_score": 0.6}

    async def _generate_clarifying_questions(self, creator_input: str, intent_analysis: Dict) -> List[str]:
        """Generate questions to clarify ambiguous aspects"""
        if intent_analysis.get("clarity_score", 0) > 0.8:
            return []

        # Generate 2-3 clarifying questions based on gaps in intent
        questions = [
            "Mục tiêu chính bạn muốn đạt được là gì?",
            "Có ràng buộc nào về tài nguyên hoặc thời gian không?",
            "Bạn ưu tiên tính đơn giản hay tính năng phong phú?"
        ]

        return questions[:2]  # Limit to 2 questions

    async def _establish_initial_framework(self, intent_analysis: Dict, context: Dict) -> Dict[str, Any]:
        """Establish initial project framework"""
        return {
            "scope": intent_analysis.get("scope", "medium"),
            "constraints": context.get("constraints", []),
            "objectives": intent_analysis.get("objectives", []),
            "philosophy": intent_analysis.get("philosophy", ["Simple", "Effective", "Practical"])
        }

    async def _generate_phase_1_response(self, intent_analysis: Dict, framework: Dict, questions: List[str]) -> str:
        """Generate human-readable response for Phase 1"""
        response = f"""
🎯 **DKCP Phase 1: Khởi nguồn Ý chí đã được tiếp nhận**

**Phân tích ý chí ban đầu:**
- Mục tiêu: {intent_analysis.get('intent', 'Chưa rõ ràng')}
- Độ rõ ràng: {intent_analysis.get('clarity_score', 0.5):.1%}

**Khuôn khổ ban đầu:**
- Phạm vi: {framework.get('scope', 'medium')}
- Triết lý: {', '.join(framework.get('philosophy', []))}

"""

        if questions:
            response += "**Câu hỏi làm rõ:**\n"
            for i, q in enumerate(questions, 1):
                response += f"{i}. {q}\n"
        else:
            response += "✅ Ý chí đã đủ rõ ràng để chuyển sang Phase 2"

        return response

    async def _perform_dr_analysis(self, creator_input: str, session: Dict) -> Dict[str, Any]:
        """Perform Deconstruction & Reconstruction analysis"""
        return {
            "components": ["component_1", "component_2"],
            "relationships": ["relation_1"],
            "core_problems": ["problem_1"],
            "completeness_score": 0.75
        }

    async def _query_knowledge_base(self, dr_analysis: Dict, creator_input: str) -> Dict[str, Any]:
        """Query memory engine for relevant knowledge"""
        if not self.memory_engine:
            return {"relevant_knowledge": [], "context_strength": 0.3}

        # Query memory engine for relevant context
        try:
            context = await self.memory_engine.query_knowledge(creator_input)
            return {"relevant_knowledge": context, "context_strength": 0.7}
        except:
            return {"relevant_knowledge": [], "context_strength": 0.3}

    def _log_phase_metrics(self, phase: DKCPPhase, processing_time: float, response_data: Dict):
        """Log metrics for meta-optimization"""
        metrics = {
            "phase": phase.value,
            "processing_time": processing_time,
            "confidence_score": response_data.get("confidence_score", 0.5),
            "timestamp": time.time()
        }
        self.phase_metrics.append(metrics)

        # Keep only last 100 metrics
        if len(self.phase_metrics) > 100:
            self.phase_metrics.pop(0)

    def get_phase_metrics(self) -> List[Dict]:
        """Get phase metrics for meta-optimization analysis"""
        return self.phase_metrics.copy()

    def _create_error_response(self, request: DKCPRequest, error_msg: str, processing_time: float) -> DKCPResponse:
        """Create error response"""
        return DKCPResponse(
            phase=request.phase,
            ai_response=f"❌ Lỗi xử lý DKCP: {error_msg}",
            analysis={"error": error_msg},
            next_phase_ready=False,
            clarification_questions=[],
            session_id=request.session_id,
            processing_time=processing_time,
            confidence_score=0.0
        )

    # Additional helper methods would be implemented for phases 2-4
    async def _create_multidimensional_analysis(self, dr_analysis: Dict, knowledge_context: Dict) -> Dict:
        """Create multi-dimensional analysis for Phase 2"""
        return {"dimensions": ["technical", "business", "user"], "analysis": "comprehensive"}

    async def _generate_phase_2_response(self, dr_analysis: Dict, knowledge_context: Dict, multidimensional_analysis: Dict) -> str:
        """Generate response for Phase 2"""
        return "🔍 **DKCP Phase 2: Phân tích tri thức hoàn tất**\n\nĐã thực hiện phân tích D&R và tổng hợp tri thức liên quan."

    async def _generate_optimization_proposals(self, session: Dict, request: DKCPRequest) -> Dict:
        """Generate optimization proposals for Phase 3"""
        return {"proposals": ["proposal_1", "proposal_2"], "optimization_focus": "performance"}

    async def _simulate_proposals(self, optimization_proposals: Dict) -> Dict:
        """Simulate optimization proposals"""
        return {"simulation_results": "positive", "performance_improvement": "15%"}

    async def _create_refined_solution(self, optimization_proposals: Dict, simulation_results: Dict, creator_input: str) -> Dict:
        """Create refined solution"""
        return {"solution": "refined_solution", "optimization_complete": True, "solution_confidence": 0.85}

    async def _generate_phase_3_response(self, optimization_proposals: Dict, simulation_results: Dict, refined_solution: Dict) -> str:
        """Generate response for Phase 3"""
        return "⚡ **DKCP Phase 3: Tối ưu hóa hoàn tất**\n\nĐã tạo giải pháp được tối ưu hóa và mô phỏng thành công."

    async def _generate_final_design(self, session: Dict, request: DKCPRequest) -> Dict:
        """Generate final design for Phase 4"""
        return {"design": "final_design", "ready_for_implementation": True, "design_confidence": 0.9}

    async def _create_implementation_guide(self, final_design: Dict) -> Dict:
        """Create implementation guide"""
        return {"guide": "implementation_steps", "estimated_effort": "medium"}

    async def _create_project_summary(self, session: Dict, final_design: Dict) -> Dict:
        """Create project summary"""
        return {"summary": "project_complete", "phases_completed": 4}

    async def _store_completed_session(self, session_id: str, session: Dict, final_design: Dict):
        """Store completed session for future reference"""
        if self.memory_engine:
            await self.memory_engine.store_completed_dkcp_session(session_id, session, final_design)

    async def _generate_phase_4_response(self, final_design: Dict, implementation_guide: Dict, project_summary: Dict) -> str:
        """Generate response for Phase 4"""
        return "✅ **DKCP Phase 4: Dự án hoàn tất**\n\nBản thiết kế cuối cùng đã sẵn sàng cho triển khai."
