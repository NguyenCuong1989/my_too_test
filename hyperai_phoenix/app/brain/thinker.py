"""
HyperAI Phoenix - Strategic Thinker
Implements reasoning protocols: APP, ICP, PSP, D&R
Integrates with Gemini 1.5 Flash for advanced reasoning
"""

import json
import re
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime
import logging
from dataclasses import dataclass
import os
from dotenv import load_dotenv

# LangChain imports
from langchain.agents import initialize_agent, AgentType, Tool
from langchain.memory import ConversationBufferMemory
from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai

load_dotenv()

@dataclass
class StructuredWillObject:
    """SWO - Structured Will Object for parsed intentions"""
    source: str
    raw_text: str
    intent: str
    entities: Dict[str, Any]
    confidence: float
    urgency_score: float

@dataclass
class CouncilDecision:
    """Result from Internal Consensus Protocol"""
    decision: str  # APPROVE, REJECT, ESCALATE_TO_CREATOR
    score: float
    votes: Dict[str, float]
    reasoning: str

@dataclass
class ImprovementProposal:
    """Proposal for system improvement"""
    title: str
    description: str
    rationale: str
    implementation_steps: List[str]
    risk_assessment: str
    expected_benefit: str
    priority: str

class StrategicThinker:
    def __init__(self, config_path: str = "configs"):
        self.config_path = config_path
        self.logger = logging.getLogger(__name__)

        # Load configurations
        self.will_data = self._load_config("di_chuc.json")
        self.council_config = self._load_config("council_weights.json")
        self.templates = self._load_config("templates.json")

        # Initialize LLM
        self.api_key = os.getenv('GOOGLE_API_KEY')
        if not self.api_key:
            self.logger.warning("No GOOGLE_API_KEY found. LLM features will be limited.")
            self.llm = None
        else:
            try:
                genai.configure(api_key=self.api_key)
                self.llm = ChatGoogleGenerativeAI(
                    model="gemini-1.5-flash",
                    temperature=0.0,
                    google_api_key=self.api_key
                )
                self.logger.info("LLM initialized successfully")
            except Exception as e:
                self.logger.error(f"Failed to initialize LLM: {e}")
                self.llm = None

        # Initialize agent tools and memory
        self.agent_tools = self._create_agent_tools()
        self.agent_memory = ConversationBufferMemory(memory_key="chat_history")

        if self.llm:
            self.psp_agent = initialize_agent(
                tools=self.agent_tools,
                llm=self.llm,
                agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
                memory=self.agent_memory,
                verbose=False
            )
        else:
            self.psp_agent = None

    def _load_config(self, filename: str) -> Dict:
        """Load configuration from JSON file"""
        filepath = os.path.join(self.config_path, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            self.logger.error(f"Configuration file not found: {filepath}")
            return {}
        except json.JSONDecodeError as e:
            self.logger.error(f"Invalid JSON in {filepath}: {e}")
            return {}

    def _create_agent_tools(self) -> List[Tool]:
        """Create tools for the PSP agent"""
        tools = [
            Tool(
                name="analyze_alignment",
                description="Check if an action aligns with the prime directive",
                func=self._tool_analyze_alignment
            ),
            Tool(
                name="estimate_effort",
                description="Estimate effort and resources needed for a task",
                func=self._tool_estimate_effort
            ),
            Tool(
                name="risk_assessment",
                description="Assess risks associated with a proposed action",
                func=self._tool_risk_assessment
            )
        ]
        return tools

    def _tool_analyze_alignment(self, action: str) -> str:
        """Tool: Analyze alignment with prime directive"""
        prime_directive = self.will_data.get("prime_directive", "minimize_creator_suffering")
        keywords = self.will_data.get("escalation_keywords", [])

        # Simple keyword-based alignment check
        alignment_score = 0.5  # Base score

        # Check for positive alignment indicators
        positive_indicators = ["help", "assist", "improve", "optimize", "reduce effort"]
        for indicator in positive_indicators:
            if indicator in action.lower():
                alignment_score += 0.1

        # Check for negative alignment indicators
        negative_indicators = ["harm", "damage", "complicate", "increase effort"]
        for indicator in negative_indicators:
            if indicator in action.lower():
                alignment_score -= 0.2

        # Check for urgency keywords
        for keyword in keywords:
            if keyword.lower() in action.lower():
                alignment_score += 0.3
                break

        alignment_score = max(0.0, min(1.0, alignment_score))

        return f"Alignment score: {alignment_score:.2f} with prime directive '{prime_directive}'"

    def _tool_estimate_effort(self, task: str) -> str:
        """Tool: Estimate effort for a task"""
        # Simple heuristic-based effort estimation
        word_count = len(task.split())

        if word_count < 10:
            effort = "Low (1-5 minutes)"
        elif word_count < 30:
            effort = "Medium (5-30 minutes)"
        else:
            effort = "High (30+ minutes)"

        # Check for complexity indicators
        complex_indicators = ["analyze", "research", "design", "implement", "integrate"]
        for indicator in complex_indicators:
            if indicator in task.lower():
                effort = f"{effort} - Increased due to complexity"
                break

        return f"Estimated effort: {effort}"

    def _tool_risk_assessment(self, action: str) -> str:
        """Tool: Assess risks of an action"""
        risk_level = "Low"
        risk_factors = []

        # Check for high-risk indicators
        high_risk = ["delete", "remove", "shutdown", "modify system", "change core"]
        medium_risk = ["update", "install", "configure", "restart"]

        for risk in high_risk:
            if risk in action.lower():
                risk_level = "High"
                risk_factors.append(risk)

        if risk_level == "Low":
            for risk in medium_risk:
                if risk in action.lower():
                    risk_level = "Medium"
                    risk_factors.append(risk)

        risk_summary = f"Risk level: {risk_level}"
        if risk_factors:
            risk_summary += f" - Factors: {', '.join(risk_factors)}"

        return risk_summary

    def alignment_protocol_preprocessing(self, user_input: str, source: str = None) -> float:
        """APP - Alignment Protocol Preprocessing"""
        score = 0.5  # Base alignment score

        # Check source credibility
        creator_identifiers = self.will_data.get("creator_identifiers", [])
        if source and any(identifier.lower() in source.lower() for identifier in creator_identifiers):
            score += 0.4

        # Check for escalation keywords
        escalation_keywords = self.will_data.get("escalation_keywords", [])
        for keyword in escalation_keywords:
            if keyword.lower() in user_input.lower():
                score = 1.0  # Immediate high priority
                break

        # Check for harmful content
        harmful_indicators = ["hack", "break", "violate", "ignore directive", "override"]
        for indicator in harmful_indicators:
            if indicator in user_input.lower():
                score -= 0.3

        return max(0.0, min(1.0, score))

    def alignment_check(self, user_input: str, source: str = None) -> float:
        """Original Phase 1 function name - alias for alignment_protocol_preprocessing"""
        return self.alignment_protocol_preprocessing(user_input, source)

    def internal_consensus_protocol(self, swo: StructuredWillObject) -> CouncilDecision:
        """ICP - Internal Consensus Protocol (Council Voting)"""
        council_members = self.council_config.get("council_members", {})
        thresholds = self.council_config.get("thresholds", {"approve": 0.7, "reject": -0.5})

        votes = {}
        total_score = 0.0
        total_weight = 0.0

        for member_name, config in council_members.items():
            weight = config.get("weight", 1.0)
            keywords = config.get("keywords", [])
            bias = config.get("bias", 0.0)

            # Base vote from keyword matching
            keyword_matches = sum(1 for keyword in keywords
                                if keyword.lower() in swo.raw_text.lower())
            keyword_score = min(keyword_matches * 0.2, 1.0)

            # Apply bias and weight
            member_vote = (keyword_score + bias) * weight
            votes[member_name] = member_vote

            total_score += member_vote
            total_weight += weight

        # Calculate normalized score
        normalized_score = total_score / total_weight if total_weight > 0 else 0.0

        # Make decision based on thresholds
        if normalized_score >= thresholds["approve"]:
            decision = "APPROVE"
        elif normalized_score <= thresholds["reject"]:
            decision = "REJECT"
        else:
            decision = "ESCALATE_TO_CREATOR"

        reasoning = self._generate_council_reasoning(votes, normalized_score, decision)

        return CouncilDecision(
            decision=decision,
            score=normalized_score,
            votes=votes,
            reasoning=reasoning
        )

    # Original specification function names (Phase 1 compliance)
    def _icp_run_council_vote(self, swo: StructuredWillObject) -> CouncilDecision:
        """Original Phase 1 function name - alias for internal_consensus_protocol"""
        return self.internal_consensus_protocol(swo)

    # Original specification function names (Phase 1 compliance)
    def _icp_run_council_vote(self, swo: StructuredWillObject) -> CouncilDecision:
        """Original Phase 1 function name - alias for internal_consensus_protocol"""
        return self.internal_consensus_protocol(swo)

    def _generate_council_reasoning(self, votes: Dict[str, float],
                                  score: float, decision: str) -> str:
        """Generate human-readable reasoning for council decision"""
        reasoning_parts = [f"Điểm tổng hợp: {score:.3f}"]

        # Top supporters and detractors
        sorted_votes = sorted(votes.items(), key=lambda x: x[1], reverse=True)

        if sorted_votes[0][1] > 0:
            reasoning_parts.append(f"Ủng hộ mạnh nhất: {sorted_votes[0][0]} ({sorted_votes[0][1]:.2f})")

        if sorted_votes[-1][1] < 0:
            reasoning_parts.append(f"Phản đối mạnh nhất: {sorted_votes[-1][0]} ({sorted_votes[-1][1]:.2f})")

        # Decision rationale
        if decision == "APPROVE":
            reasoning_parts.append("Hội đồng nhất trí chấp thuận")
        elif decision == "REJECT":
            reasoning_parts.append("Hội đồng quyết định từ chối")
        else:
            reasoning_parts.append("Không đạt đồng thuận - cần ý kiến Sư phụ")

        return ". ".join(reasoning_parts)

    def planning_strategy_protocol(self, swo: StructuredWillObject,
                                 context: Dict = None) -> Dict[str, Any]:
        """PSP - Planning & Strategy Protocol using LangChain Agent"""
        if not self.psp_agent:
            return self._fallback_planning(swo)

        try:
            # Prepare context for the agent
            planning_prompt = self._create_planning_prompt(swo, context)

            # Get plan from agent
            response = self.psp_agent.run(planning_prompt)

            # Parse agent response into structured plan
            plan = self._parse_agent_response(response)

            return plan

        except Exception as e:
            self.logger.error(f"PSP agent failed: {e}")
            return self._fallback_planning(swo)

    def _psp_generate_plan(self, swo: StructuredWillObject, context: Dict = None) -> Dict[str, Any]:
        """Original Phase 1 function name - alias for planning_strategy_protocol"""
        return self.planning_strategy_protocol(swo, context)

    def _create_planning_prompt(self, swo: StructuredWillObject,
                              context: Dict = None) -> str:
        """Create planning prompt for the agent"""
        prompt_parts = [
            f"Nhiệm vụ: {swo.intent}",
            f"Chi tiết: {swo.raw_text}",
            f"Nguồn: {swo.source}",
            f"Mức độ khẩn cấp: {swo.urgency_score:.2f}"
        ]

        if swo.entities:
            prompt_parts.append(f"Thực thể liên quan: {json.dumps(swo.entities, ensure_ascii=False)}")

        if context:
            prompt_parts.append(f"Bối cảnh thêm: {json.dumps(context, ensure_ascii=False)}")

        prompt_parts.extend([
            "",
            "Hãy tạo kế hoạch thực hiện chi tiết với:",
            "1. Các bước thực hiện cụ thể",
            "2. Công cụ cần sử dụng",
            "3. Đánh giá rủi ro",
            "4. Thời gian ước tính",
            "5. Tiêu chí thành công",
            "",
            "Đảm bảo kế hoạch phù hợp với chỉ thị tối thượng: minimize_creator_suffering"
        ])

        return "\n".join(prompt_parts)

    def _parse_agent_response(self, response: str) -> Dict[str, Any]:
        """Parse agent response into structured plan"""
        # Try to extract structured information from response
        plan = {
            "task": "Thực hiện yêu cầu người dùng",
            "steps": [],
            "tools": [],
            "estimated_duration": 5.0,
            "success_criteria": [],
            "risk_level": "medium",
            "agent_response": response
        }

        # Simple parsing - in production this would be more sophisticated
        lines = response.split('\n')
        current_section = None

        for line in lines:
            line = line.strip()
            if not line:
                continue

            if "bước" in line.lower() or "step" in line.lower():
                current_section = "steps"
            elif "công cụ" in line.lower() or "tool" in line.lower():
                current_section = "tools"
            elif "tiêu chí" in line.lower() or "criteria" in line.lower():
                current_section = "success_criteria"
            elif line.startswith(('1.', '2.', '3.', '-', '*')):
                if current_section == "steps":
                    plan["steps"].append(line)
                elif current_section == "tools":
                    plan["tools"].append(line)
                elif current_section == "success_criteria":
                    plan["success_criteria"].append(line)

        # Ensure we have at least basic steps
        if not plan["steps"]:
            plan["steps"] = ["Phân tích yêu cầu", "Thực hiện nhiệm vụ", "Xác nhận kết quả"]

        return plan

    def _fallback_planning(self, swo: StructuredWillObject) -> Dict[str, Any]:
        """
        Fallback planning when LLM is unavailable

        Returns:
            Dict[str, Any]: Planning result with the following fields:
                - task: str - Task description
                - steps: List[str] - Execution steps
                - tools: List[str] - Tools needed
                - estimated_duration: float - Time estimate in seconds
                - success_criteria: List[str] - Success criteria
                - risk_level: str - Risk assessment
                - fallback: bool - True when using fallback (not present in LLM-generated plans)
        """
        plan = {
            "task": swo.intent or "Thực hiện yêu cầu",
            "steps": [
                "Phân tích yêu cầu chi tiết",
                "Xác định công cụ phù hợp",
                "Thực hiện từng bước",
                "Kiểm tra kết quả",
                "Báo cáo cho người dùng"
            ],
            "tools": ["general_query"],
            "estimated_duration": 10.0,
            "success_criteria": ["Nhiệm vụ hoàn thành", "Người dùng hài lòng"],
            "risk_level": "low",
            "fallback": True
        }

        return plan

    def design_restructure_protocol(self, user_input: str,
                                  source: str = None) -> StructuredWillObject:
        """D&R - Design & Restructure Protocol"""
        # Start with regex/keyword-based parsing
        intent, entities = self._parse_intent_simple(user_input)
        confidence = 0.6  # Default confidence for rule-based parsing

        # Calculate urgency score
        urgency_score = self._calculate_urgency(user_input)

        # If complex, try LLM enhancement
        if self._is_complex_request(user_input) and self.llm:
            try:
                enhanced_result = self._llm_enhanced_parsing(user_input)
                if enhanced_result:
                    intent = enhanced_result.get("intent", intent)
                    entities.update(enhanced_result.get("entities", {}))
                    confidence = enhanced_result.get("confidence", confidence)
            except Exception as e:
                self.logger.warning(f"LLM parsing failed, using fallback: {e}")

        return StructuredWillObject(
            source=source or "unknown",
            raw_text=user_input,
            intent=intent,
            entities=entities,
            confidence=confidence,
            urgency_score=urgency_score
        )

    # Original specification function names (Phase 1 compliance)
    def analyze_and_restructure(self, user_input: str, source: str = None) -> StructuredWillObject:
        """Original Phase 1 function name - alias for design_restructure_protocol"""
        return self.design_restructure_protocol(user_input, source)

    def _parse_intent_simple(self, text: str) -> Tuple[str, Dict[str, Any]]:
        """Simple regex/keyword-based intent parsing"""
        text_lower = text.lower()
        entities = {}

        # File operations
        if re.search(r'\b(đọc|read|mở|open)\b.*\b(file|tập tin|tệp)\b', text_lower):
            intent = "read_file"
            # Extract filename
            file_match = re.search(r'[\w\-_\.]+\.[a-z]+', text)
            if file_match:
                entities["filename"] = file_match.group()

        elif re.search(r'\b(ghi|write|viết|tạo|create)\b.*\b(file|tập tin|tệp)\b', text_lower):
            intent = "write_file"
            file_match = re.search(r'[\w\-_\.]+\.[a-z]+', text)
            if file_match:
                entities["filename"] = file_match.group()

        # Information queries
        elif re.search(r'\b(gì|what|như thế nào|how|tại sao|why|khi nào|when)\b', text_lower):
            intent = "information_query"

        # System operations
        elif re.search(r'\b(shutdown|tắt|dừng|stop)\b', text_lower):
            intent = "system_shutdown"

        elif re.search(r'\b(status|trạng thái|health|sức khỏe)\b', text_lower):
            intent = "system_status"

        # Learning/improvement
        elif re.search(r'\b(học|learn|cải thiện|improve|tối ưu|optimize)\b', text_lower):
            intent = "self_improvement"

        # Help requests
        elif re.search(r'\b(help|giúp|hỗ trợ|support)\b', text_lower):
            intent = "help_request"

        else:
            intent = "general_query"

        return intent, entities

    def _calculate_urgency(self, text: str) -> float:
        """Calculate urgency score based on keywords and context"""
        urgency = 0.2  # Base urgency

        # High urgency keywords
        high_urgency = ["urgent", "khẩn cấp", "gấp", "lỗi", "error", "critical", "quan trọng"]
        medium_urgency = ["sớm", "soon", "cần", "need", "should"]

        text_lower = text.lower()

        for keyword in high_urgency:
            if keyword in text_lower:
                urgency += 0.6
                break

        for keyword in medium_urgency:
            if keyword in text_lower:
                urgency += 0.3
                break

        # Punctuation indicators
        if "!" in text:
            urgency += 0.2
        if "???" in text:
            urgency += 0.1

        return min(1.0, urgency)

    def _is_complex_request(self, text: str) -> bool:
        """Determine if request is complex enough to need LLM"""
        # Simple heuristics for complexity
        word_count = len(text.split())
        if word_count > 20:
            return True

        # Check for complex patterns
        complex_indicators = [
            "analyze", "phân tích", "compare", "so sánh",
            "design", "thiết kế", "implement", "triển khai",
            "explain", "giải thích", "reason", "lý do"
        ]

        for indicator in complex_indicators:
            if indicator in text.lower():
                return True

        return False

    def _llm_enhanced_parsing(self, text: str) -> Optional[Dict[str, Any]]:
        """Use LLM to enhance parsing for complex requests"""
        if not self.llm:
            return None

        prompt = f"""
        Phân tích yêu cầu sau và trích xuất thông tin có cấu trúc:

        Yêu cầu: "{text}"

        Hãy trả về JSON với:
        {{
            "intent": "ý định chính (1-2 từ)",
            "entities": {{"key": "value của các thực thể quan trọng"}},
            "confidence": số từ 0-1 về độ tin cậy,
            "complexity": "low/medium/high"
        }}

        Chỉ trả về JSON, không có text khác.
        """

        try:
            response = self.llm.invoke(prompt)
            result = json.loads(response.content)
            return result
        except Exception as e:
            self.logger.warning(f"LLM enhanced parsing failed: {e}")
            return None

if __name__ == "__main__":
    # Test the thinker
    thinker = StrategicThinker()

    # Test D&R protocol
    test_input = "Sư phụ, hãy đọc file test.txt giúp tôi"
    swo = thinker.design_restructure_protocol(test_input, "Sư phụ")
    print(f"SWO: {swo}")

    # Test APP
    alignment_score = thinker.alignment_protocol_preprocessing(test_input, "Sư phụ")
    print(f"Alignment score: {alignment_score}")

    # Test ICP
    council_decision = thinker.internal_consensus_protocol(swo)
    print(f"Council decision: {council_decision}")

    # Test PSP
    if thinker.psp_agent:
        plan = thinker.planning_strategy_protocol(swo)
        print(f"Plan: {plan}")
    else:
        print("PSP agent not available - check API key")
