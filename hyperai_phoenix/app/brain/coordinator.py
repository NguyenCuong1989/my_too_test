"""
HyperAI Phoenix - Meta-Optimization Coordinator
Central orchestration with state machine and queue-based communication
Implements MOP, DKCP, LSP, CCP protocols
"""

import json
import time
import threading
import queue
from enum import Enum
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
from dataclasses import dataclass, asdict
import logging
from .i18n import error_message
import os

from .memory import MemoryEngine
from .thinker import StrategicThinker, StructuredWillObject, CouncilDecision

# Import enhanced MOP and OCP integration
from ...core.protocols.meta_optimization import MetaOptimizationProtocol
from ...core.protocols.ocp import global_ocp, integrate_ocp_with_component, OCPOperationType

class SystemState(Enum):
    INITIALIZING = "initializing"
    IDLE = "idle"
    THINKING = "thinking"
    EXECUTING = "executing"
    LOGGING = "logging"
    ERROR = "error"
    SHUTDOWN = "shutdown"

@dataclass
class Directive:
    """User directive with metadata"""
    id: str
    content: str
    source: str
    timestamp: datetime
    priority: int = 1
    session_id: Optional[str] = None

@dataclass
class ExecutionResult:
    """Result of executing a directive"""
    directive_id: str
    success: bool
    result_data: Any
    error_message: Optional[str]
    execution_time: float
    alignment_score: float
    timestamp: datetime

@dataclass
class SystemMessage:
    """System message for communication"""
    type: str
    content: str
    metadata: Dict[str, Any]
    timestamp: datetime

class ResponseHandler:
    """DKCP - Dynamic Knowledge & Communication Protocol"""

    def __init__(self, templates_config: Dict):
        self.templates = templates_config.get("response_templates", {})
        self.personality = templates_config.get("personality", {})
        self.format_settings = templates_config.get("format_settings", {})
        self.logger = logging.getLogger(__name__)

    def format_response(self, response_type: str, language: str = "vi",
                       **kwargs) -> str:
        """Format response using templates"""
        template_group = self.templates.get(response_type, {})
        template = template_group.get(language, template_group.get("vi", ""))

        if not template:
            # Fallback template
            template = "Đã xử lý yêu cầu. Kết quả: {result}"

        try:
            formatted = template.format(**kwargs)

            # Apply format settings
            max_length = self.format_settings.get("max_length", 2000)
            if len(formatted) > max_length:
                formatted = formatted[:max_length-3] + "..."

            return formatted
        except KeyError as e:
            self.logger.warning(f"Template formatting error: {e}")
            return f"Phản hồi: {kwargs.get('details', 'Hoàn thành')}"

class MetaOptimizationCoordinator:
    """Central coordinator implementing MOP state machine"""

    def __init__(self, config_path: str = "configs", data_path: str = "data"):
        self.config_path = config_path
        self.data_path = data_path
        self.logger = logging.getLogger(__name__)

        # Initialize state
        self.current_state = SystemState.INITIALIZING
        self.session_id = f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        self.startup_time = datetime.now()

        # Initialize communication queues
        self.directive_queue = queue.Queue()
        self.result_queue = queue.Queue()
        self.approval_queue = queue.Queue()
        self.system_message_queue = queue.Queue()

        # Initialize components
        self.memory_engine = MemoryEngine(
            db_path=os.path.join(data_path, "databases", "hyperai.db"),
            chroma_path=os.path.join(data_path, "databases", "knowledge_base"),
            archive_path=os.path.join(data_path, "logs", "archive")
        )

        self.thinker = StrategicThinker(config_path)

        # Initialize enhanced MOP as the OVERARCHING MECHANISM
        self.mop = MetaOptimizationProtocol(
            dkcp_handler=None,  # Will be set if available
            lsp_handler=None,   # Will be set if available
            memory_engine=self.memory_engine
        )

        # Register this coordinator with MOP for OCP integration
        self.mop.register_component_for_ocp(self, "MetaOptimizationCoordinator")

        # Also integrate all major components with OCP through MOP
        self.memory_engine = self.mop.register_component_for_ocp(self.memory_engine, "MemoryEngine")
        self.thinker = self.mop.register_component_for_ocp(self.thinker, "StrategicThinker")

        # Load configurations
        self.fasr_state = self._load_fasr_state()
        self.will_data = self.thinker.will_data

        # Initialize response handler
        self.response_handler = ResponseHandler(self.thinker.templates)

        # Threading control
        self.running = False
        self.main_thread = None
        self.last_heartbeat = datetime.now()

        # Performance tracking
        self.performance_metrics = {
            'total_directives': 0,
            'successful_executions': 0,
            'total_execution_time': 0.0,
            'error_count': 0
        }

        # Tool registry
        self.tool_registry = {
            'read_file': self._tool_read_file,
            'write_file': self._tool_write_file,
            'system_status': self._tool_system_status,
            'memory_search': self._tool_memory_search,
            'general_query': self._tool_general_query
        }

        self.logger.info(f"Coordinator initialized with session ID: {self.session_id}")
        self.logger.info("🎨 OCP integration active in ALL coordinator functions via MOP")
        self.logger.info("🧭 MOP established as overarching mechanism coordinating entire system")

    def _load_fasr_state(self) -> Dict:
        """Load FASR state from file"""
        fasr_path = os.path.join(self.config_path, "fasr_state.json")
        try:
            with open(fasr_path, 'r', encoding='utf-8') as f:
                state = json.load(f)
                state['session_id'] = self.session_id
                state['last_heartbeat'] = datetime.now().isoformat()
                return state
        except FileNotFoundError:
            self.logger.warning(f"FASR state file not found: {fasr_path}")
            return {
                'current_state': 'INITIALIZING',
                'session_id': self.session_id,
                'last_heartbeat': datetime.now().isoformat(),
                'performance_metrics': {}
            }

    def _save_fasr_state(self):
        """Save current FASR state to file"""
        fasr_path = os.path.join(self.config_path, "fasr_state.json")

        # Update state with current metrics
        self.fasr_state.update({
            'current_state': self.current_state.value,
            'session_id': self.session_id,
            'last_heartbeat': datetime.now().isoformat(),
            'performance_metrics': self._calculate_current_metrics()
        })

        try:
            # Create backup
            backup_path = f"{fasr_path}.backup"
            if os.path.exists(fasr_path):
                os.replace(fasr_path, backup_path)

            # Save new state
            with open(fasr_path, 'w', encoding='utf-8') as f:
                json.dump(self.fasr_state, f, ensure_ascii=False, indent=2)

            self.logger.debug("FASR state saved successfully")
        except Exception as e:
            self.logger.error(f"Failed to save FASR state: {e}")

    def start(self):
        """Start the coordinator main loop"""
        if self.running:
            return

        self.running = True
        self.current_state = SystemState.IDLE

        # Start main coordination thread
        self.main_thread = threading.Thread(target=self._main_loop, daemon=True)
        self.main_thread.start()

        # Implant will and state into memory
        self.memory_engine.implant_will_and_fasr(self.will_data, self.fasr_state)

        self.logger.info("Coordinator started successfully")

    def stop(self):
        """Stop the coordinator safely (CCP - Continuity Check Protocol)"""
        self.logger.info("Initiating safe shutdown...")

        self.current_state = SystemState.SHUTDOWN
        self.running = False

        try:
            # Wait for current operations to complete
            if self.main_thread and self.main_thread.is_alive():
                self.main_thread.join(timeout=10)

            # Compact memories if needed
            if self._should_compact_memories():
                self.memory_engine.compact_memories()

            # Save final state
            self._save_fasr_state()

            # Close memory engine
            self.memory_engine.close()

            self.logger.info("Safe shutdown completed")
        except Exception as e:
            self.logger.error(f"Error during shutdown: {e}")

    def submit_directive(self, content: str, source: str = "user",
                        priority: int = 1) -> str:
        """Submit a directive for processing"""
        directive_id = f"dir_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}"

        directive = Directive(
            id=directive_id,
            content=content,
            source=source,
            timestamp=datetime.now(),
            priority=priority,
            session_id=self.session_id
        )

        self.directive_queue.put(directive)
        self.logger.info(f"Directive submitted: {directive_id}")

        return directive_id

    def get_result(self, directive_id: str, timeout: float = 30.0) -> Optional[ExecutionResult]:
        """Get result for a specific directive"""
        start_time = time.time()

        while time.time() - start_time < timeout:
            try:
                result = self.result_queue.get(timeout=1.0)
                if result.directive_id == directive_id:
                    return result
                else:
                    # Put it back for other consumers
                    self.result_queue.put(result)
            except queue.Empty:
                continue

        return None

    def get_system_message(self, timeout: float = 1.0) -> Optional[SystemMessage]:
        """Get system message"""
        try:
            return self.system_message_queue.get(timeout=timeout)
        except queue.Empty:
            return None

    def _main_loop(self):
        """Main coordination loop implementing MOP state machine"""
        while self.running:
            try:
                self._update_heartbeat()

                if self.current_state == SystemState.IDLE:
                    self._handle_idle_state()
                elif self.current_state == SystemState.THINKING:
                    self._handle_thinking_state()
                elif self.current_state == SystemState.EXECUTING:
                    self._handle_executing_state()
                elif self.current_state == SystemState.LOGGING:
                    self._handle_logging_state()
                elif self.current_state == SystemState.ERROR:
                    self._handle_error_state()

                time.sleep(0.1)  # Prevent CPU spinning

            except Exception as e:
                self.logger.error(f"Main loop error: {e}")
                self.current_state = SystemState.ERROR
                time.sleep(1.0)

    def _handle_idle_state(self):
        """Handle IDLE state - wait for directives"""
        try:
            directive = self.directive_queue.get(timeout=1.0)
            self.current_directive = directive
            self.current_state = SystemState.THINKING

            # Log directive received
            self.memory_engine.log_event(
                event_type="directive_received",
                source=directive.source,
                details=f"Content: {directive.content[:100]}...",
                session_id=self.session_id
            )

        except queue.Empty:
            # Check for maintenance tasks
            self._check_maintenance_tasks()

    def _handle_thinking_state(self):
        """Handle THINKING state - process directive through protocols"""
        directive = self.current_directive
        start_time = time.time()

        try:
            # APP - Alignment Protocol Preprocessing
            alignment_score = self.thinker.alignment_protocol_preprocessing(
                directive.content, directive.source
            )

            # D&R - Design & Restructure Protocol
            swo = self.thinker.design_restructure_protocol(
                directive.content, directive.source
            )

            # Decision path based on alignment score
            if alignment_score > 0.8:
                # High alignment - go directly to PSP
                plan = self.thinker.planning_strategy_protocol(swo)
                decision = CouncilDecision("APPROVE", alignment_score, {}, "High alignment bypass")
            else:
                # ICP - Internal Consensus Protocol
                decision = self.thinker.internal_consensus_protocol(swo)

                if decision.decision == "APPROVE":
                    plan = self.thinker.planning_strategy_protocol(swo)
                else:
                    plan = None

            # Store thinking result
            self.current_plan = plan
            self.current_decision = decision
            self.current_swo = swo
            self.thinking_duration = time.time() - start_time

            if decision.decision == "APPROVE" and plan:
                self.current_state = SystemState.EXECUTING
            elif decision.decision == "ESCALATE_TO_CREATOR":
                self._escalate_to_creator(directive, decision)
                self.current_state = SystemState.LOGGING
            else:
                self._reject_directive(directive, decision)
                self.current_state = SystemState.LOGGING

        except Exception as e:
            self.logger.error(f"Thinking error: {e}")
            self.current_state = SystemState.ERROR

    def _handle_executing_state(self):
        """Handle EXECUTING state - execute approved plan (LSP)"""
        directive = self.current_directive
        plan = self.current_plan
        start_time = time.time()

        try:
            # LSP - Logic & Source-code Protocol
            execution_result = self._execute_plan(plan, directive)

            # Create result
            result = ExecutionResult(
                directive_id=directive.id,
                success=execution_result['success'],
                result_data=execution_result.get('data'),
                error_message=execution_result.get('error'),
                execution_time=time.time() - start_time,
                alignment_score=self.current_decision.score,
                timestamp=datetime.now()
            )

            self.current_result = result
            self.result_queue.put(result)

            self.current_state = SystemState.LOGGING

        except Exception as e:
            self.logger.error(f"Execution error: {e}")

            # Create error result
            error_result = ExecutionResult(
                directive_id=directive.id,
                success=False,
                result_data=None,
                error_message=str(e),
                execution_time=time.time() - start_time,
                alignment_score=0.0,
                timestamp=datetime.now()
            )

            self.current_result = error_result
            self.result_queue.put(error_result)

            self.current_state = SystemState.LOGGING

    def _handle_logging_state(self):
        """Handle LOGGING state - log execution results"""
        try:
            result = self.current_result

            # Log to memory engine
            self.memory_engine.log_event(
                event_type="directive_completed",
                source=self.current_directive.source,
                details=f"Result: {result.success}, Time: {result.execution_time:.2f}s",
                duration=result.execution_time,
                success=result.success,
                alignment_score=result.alignment_score,
                session_id=self.session_id
            )

            # Update performance metrics
            self.performance_metrics['total_directives'] += 1
            self.performance_metrics['total_execution_time'] += result.execution_time

            if result.success:
                self.performance_metrics['successful_executions'] += 1
            else:
                self.performance_metrics['error_count'] += 1

            # Clean up current operation
            self.current_directive = None
            self.current_plan = None
            self.current_decision = None
            self.current_result = None

            self.current_state = SystemState.IDLE

        except Exception as e:
            self.logger.error(f"Logging error: {e}")
            self.current_state = SystemState.ERROR

    def _handle_error_state(self):
        """Handle ERROR state - attempt recovery"""
        try:
            # Log error
            self.memory_engine.log_event(
                event_type="system_error",
                source="system",
                details="System in error state, attempting recovery",
                success=False,
                session_id=self.session_id
            )

            # Simple recovery - return to idle
            time.sleep(2.0)  # Brief pause for stability
            self.current_state = SystemState.IDLE

        except Exception as e:
            self.logger.error(f"Error recovery failed: {e}")
            time.sleep(5.0)  # Longer pause before retry

    def _execute_plan(self, plan: Dict[str, Any], directive: Directive) -> Dict[str, Any]:
        """Execute a plan using available tools (LSP)"""
        try:
            result_data = {}

            # Get tools from plan
            tools_needed = plan.get('tools', ['general_query'])

            for tool_name in tools_needed:
                if tool_name in self.tool_registry:
                    tool_func = self.tool_registry[tool_name]

                    # Prepare tool parameters
                    tool_params = {
                        'directive': directive,
                        'plan': plan,
                        'swo': self.current_swo
                    }

                    tool_result = tool_func(**tool_params)
                    result_data[tool_name] = tool_result
                else:
                    self.logger.warning(f"Tool not found: {tool_name}")

            return {
                'success': True,
                'data': result_data,
                'plan_executed': plan
            }

        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'plan': plan
            }

    def _escalate_to_creator(self, directive: Directive, decision: CouncilDecision):
        """Escalate directive to creator for approval"""
        escalation_message = SystemMessage(
            type="escalation",
            content=self.response_handler.format_response(
                "approval_needed",
                details=f"Directive: {directive.content}\nReasoning: {decision.reasoning}"
            ),
            metadata={
                'directive_id': directive.id,
                'decision_score': decision.score,
                'votes': decision.votes
            },
            timestamp=datetime.now()
        )

        self.system_message_queue.put(escalation_message)

    def _reject_directive(self, directive: Directive, decision: CouncilDecision):
        """Reject directive based on council decision"""
        rejection_result = ExecutionResult(
            directive_id=directive.id,
            success=False,
            result_data=None,
            error_message=f"Directive rejected by council: {decision.reasoning}",
            execution_time=0.0,
            alignment_score=decision.score,
            timestamp=datetime.now()
        )

        self.current_result = rejection_result
        self.result_queue.put(rejection_result)

    def _update_heartbeat(self):
        """Update system heartbeat"""
        self.last_heartbeat = datetime.now()

    def _should_compact_memories(self) -> bool:
        """Check if memory compaction is needed"""
        # Check if it's been more than 24 hours since last compaction
        last_compaction = self.fasr_state.get('last_memory_compaction')
        if not last_compaction:
            return True

        last_time = datetime.fromisoformat(last_compaction)
        if datetime.now() - last_time > timedelta(days=1):
            return True

        return False

    def _check_maintenance_tasks(self):
        """Check and perform maintenance tasks"""
        # Memory compaction check
        if self._should_compact_memories():
            try:
                result = self.memory_engine.compact_memories()
                self.fasr_state['last_memory_compaction'] = datetime.now().isoformat()

                # Notify about compaction
                message = SystemMessage(
                    type="maintenance",
                    content=self.response_handler.format_response(
                        "memory_compacted",
                        count=result['archived_events']
                    ),
                    metadata=result,
                    timestamp=datetime.now()
                )
                self.system_message_queue.put(message)

            except Exception as e:
                self.logger.error(f"Memory compaction failed: {e}")

    def _calculate_current_metrics(self) -> Dict[str, float]:
        """Calculate current performance metrics"""
        total_directives = self.performance_metrics['total_directives']
        if total_directives == 0:
            return {
                'avg_duration': 0.0,
                'error_rate': 0.0,
                'success_rate': 0.0
            }

        avg_duration = (self.performance_metrics['total_execution_time'] /
                       total_directives)
        error_rate = (self.performance_metrics['error_count'] /
                     total_directives)
        success_rate = (self.performance_metrics['successful_executions'] /
                       total_directives)

        return {
            'avg_duration': avg_duration,
            'error_rate': error_rate,
            'success_rate': success_rate,
            'total_directives': total_directives
        }

    # Tool implementations
    def _tool_read_file(self, **kwargs) -> Dict[str, Any]:
        """Tool: Read file contents"""
        directive = kwargs['directive']
        swo = kwargs.get('swo')

        filename = None
        if swo and swo.entities.get('filename'):
            filename = swo.entities['filename']
        else:
            # Try to extract filename from content
            import re
            match = re.search(r'[\w\-_\.]+\.[a-z]+', directive.content)
            if match:
                filename = match.group()

        if not filename:
            return {'error': error_message('filename_missing')}

        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            return {'content': content, 'filename': filename}
        except FileNotFoundError:
            return {'error': error_message('file_not_found', path=filename)}
        except Exception as e:
            return {'error': error_message('file_read_error', error=str(e))}

    def _tool_write_file(self, **kwargs) -> Dict[str, Any]:
        """Tool: Write file contents"""
        directive = kwargs['directive']
        # This is a stub - in production would need content extraction
        return {'message': 'Chức năng ghi file chưa được triển khai đầy đủ'}

    def _tool_system_status(self, **kwargs) -> Dict[str, Any]:
        """Tool: Get system status"""
        uptime = datetime.now() - self.startup_time
        metrics = self._calculate_current_metrics()

        status = {
            'state': self.current_state.value,
            'uptime_seconds': uptime.total_seconds(),
            'session_id': self.session_id,
            'metrics': metrics,
            'queue_sizes': {
                'directive': self.directive_queue.qsize(),
                'result': self.result_queue.qsize(),
                'approval': self.approval_queue.qsize()
            }
        }

        return status

    def _tool_memory_search(self, **kwargs) -> Dict[str, Any]:
        """Tool: Search memory"""
        directive = kwargs['directive']

        # Perform semantic search
        results = self.memory_engine.semantic_search(directive.content)

        return {
            'search_results': results,
            'query': directive.content
        }

    def _tool_general_query(self, **kwargs) -> Dict[str, Any]:
        """Tool: Handle general queries"""
        directive = kwargs['directive']

        # This is a fallback tool for general processing
        return {
            'message': f'Đã xử lý yêu cầu: {directive.content}',
            'processed_at': datetime.now().isoformat()
        }

if __name__ == "__main__":
    # Test the coordinator
    coordinator = MetaOptimizationCoordinator()

    try:
        coordinator.start()

        # Test directive submission
        directive_id = coordinator.submit_directive("Kiểm tra trạng thái hệ thống", "test_user")
        print(f"Submitted directive: {directive_id}")

        # Wait for result
        result = coordinator.get_result(directive_id, timeout=10.0)
        if result:
            print(f"Result: {result}")
        else:
            print("No result received")

        time.sleep(2)

    finally:
        coordinator.stop()
