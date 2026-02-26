"""
HyperAI Phoenix - Multi-Agent Coordinator
Implements Phase 2 multi-agent collaboration with WFQ and CAP protocols
"""

import queue
import threading
import time
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Callable
from dataclasses import dataclass, asdict
from abc import ABC, abstractmethod
import logging
import json

@dataclass
class AgentTask:
    """Task for agent execution"""
    id: str
    agent_name: str
    task_type: str
    parameters: Dict[str, Any]
    priority: int
    created_at: datetime
    assigned_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    result: Optional[Dict[str, Any]] = None
    success: bool = False

@dataclass
class AgentMetrics:
    """Performance metrics for an agent"""
    name: str
    total_tasks: int = 0
    successful_tasks: int = 0
    total_execution_time: float = 0.0
    average_execution_time: float = 0.0
    success_rate: float = 1.0
    last_active: Optional[datetime] = None
    efficiency_factor: float = 1.0

class BaseAgent(ABC):
    """Base class for all agents"""

    def __init__(self, name: str, memory_engine=None):
        self.name = name
        self.memory_engine = memory_engine
        self.logger = logging.getLogger(f"{__name__}.{name}")
        self.metrics = AgentMetrics(name=name)

    @abstractmethod
    def execute(self, task: AgentTask) -> Dict[str, Any]:
        """Execute a task and return result"""
        pass

    def get_capabilities(self) -> List[str]:
        """Return list of capabilities this agent supports"""
        return []

    def update_metrics(self, execution_time: float, success: bool):
        """Update agent performance metrics"""
        self.metrics.total_tasks += 1
        self.metrics.total_execution_time += execution_time
        self.metrics.last_active = datetime.now()

        if success:
            self.metrics.successful_tasks += 1

        self.metrics.success_rate = (self.metrics.successful_tasks /
                                   self.metrics.total_tasks)
        self.metrics.average_execution_time = (self.metrics.total_execution_time /
                                             self.metrics.total_tasks)

class MetricsAnalyzer(BaseAgent):
    """Agent for analyzing system performance metrics"""

    def __init__(self, memory_engine=None):
        super().__init__("metrics_analyzer", memory_engine)

    def execute(self, task: AgentTask) -> Dict[str, Any]:
        """Analyze performance metrics from memory"""
        try:
            params = task.parameters
            hours_back = params.get('hours_back', 24)
            metric_types = params.get('metric_types', ['all'])

            # Get metrics from memory engine
            if self.memory_engine:
                recent_events = self.memory_engine.get_recent_events(hours=hours_back)

                # Calculate metrics
                durations = []
                successes = 0
                errors = 0
                alignment_scores = []

                for event in recent_events:
                    if event.get('event_type') == 'directive_completed':
                        if event.get('duration'):
                            durations.append(event['duration'])
                        if event.get('success'):
                            successes += 1
                        else:
                            errors += 1
                        if event.get('alignment_score'):
                            alignment_scores.append(event['alignment_score'])

                total_events = len(recent_events)
                avg_duration = sum(durations) / len(durations) if durations else 0
                error_rate = errors / total_events if total_events > 0 else 0
                avg_alignment = sum(alignment_scores) / len(alignment_scores) if alignment_scores else 0.8

                # Calculate trends (simple moving averages)
                ma30_duration = avg_duration  # Simplified
                ma100_duration = avg_duration  # Simplified

                analysis_result = {
                    'avg_duration': avg_duration,
                    'error_rate': error_rate,
                    'success_rate': 1.0 - error_rate,
                    'avg_alignment_score': avg_alignment,
                    'total_events': total_events,
                    'ma30_duration': ma30_duration,
                    'ma100_duration': ma100_duration,
                    'trend_direction': 'stable',  # Would implement trend analysis
                    'recommendations': self._generate_recommendations(avg_duration, error_rate, avg_alignment)
                }
            else:
                # Mock data for testing
                analysis_result = {
                    'avg_duration': 15.5,
                    'error_rate': 0.03,
                    'success_rate': 0.97,
                    'avg_alignment_score': 0.85,
                    'total_events': 100,
                    'recommendations': []
                }

            return {
                'success': True,
                'analysis': analysis_result,
                'agent': self.name,
                'analyzed_period_hours': hours_back
            }

        except Exception as e:
            self.logger.error(f"Metrics analysis failed: {e}")
            return {
                'success': False,
                'error': str(e),
                'agent': self.name
            }

    def _generate_recommendations(self, avg_duration: float, error_rate: float,
                                 avg_alignment: float) -> List[str]:
        """Generate recommendations based on metrics"""
        recommendations = []

        if avg_duration > 20:
            recommendations.append("Optimize response time - current average exceeds 20s")
        if error_rate > 0.05:
            recommendations.append("Reduce error rate - currently above 5% threshold")
        if avg_alignment < 0.8:
            recommendations.append("Improve alignment score - below 0.8 target")

        return recommendations

    def get_capabilities(self) -> List[str]:
        return ['performance_analysis', 'trend_analysis', 'recommendations']

class ProposalGenerator(BaseAgent):
    """Agent for generating improvement proposals"""

    def __init__(self, memory_engine=None):
        super().__init__("proposal_generator", memory_engine)

    def execute(self, task: AgentTask) -> Dict[str, Any]:
        """Generate improvement proposals based on analysis"""
        try:
            params = task.parameters
            analysis_data = params.get('analysis_data', {})
            priority_level = params.get('priority', 'medium')

            proposals = []

            # Generate proposals based on analysis
            avg_duration = analysis_data.get('avg_duration', 0)
            error_rate = analysis_data.get('error_rate', 0)
            alignment_score = analysis_data.get('avg_alignment_score', 0.8)

            if avg_duration > 20:
                proposals.append({
                    'id': f"perf_opt_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                    'title': 'Tối ưu hóa thời gian phản hồi',
                    'description': f'Thời gian phản hồi trung bình ({avg_duration:.2f}s) cần cải thiện',
                    'priority': 'high' if avg_duration > 30 else 'medium',
                    'expected_benefit': 'Giảm 30-50% thời gian phản hồi',
                    'implementation_steps': [
                        'Tối ưu hóa thuật toán xử lý',
                        'Cải thiện caching mechanism',
                        'Parallel processing tăng cường'
                    ]
                })

            if error_rate > 0.05:
                proposals.append({
                    'id': f"error_reduce_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                    'title': 'Giảm tỷ lệ lỗi hệ thống',
                    'description': f'Tỷ lệ lỗi ({error_rate:.2%}) vượt ngưỡng chấp nhận',
                    'priority': 'critical' if error_rate > 0.1 else 'high',
                    'expected_benefit': 'Giảm 50% tỷ lệ lỗi',
                    'implementation_steps': [
                        'Phân tích root cause lỗi',
                        'Tăng cường error handling',
                        'Cải thiện input validation'
                    ]
                })

            if alignment_score < 0.8:
                proposals.append({
                    'id': f"alignment_improve_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                    'title': 'Cải thiện độ tuân thủ chỉ thị',
                    'description': f'Alignment score ({alignment_score:.2f}) thấp hơn mục tiêu',
                    'priority': 'critical',
                    'expected_benefit': 'Tăng alignment score lên >0.85',
                    'implementation_steps': [
                        'Review council weights',
                        'Fine-tune prompt templates',
                        'Cải thiện context awareness'
                    ]
                })

            return {
                'success': True,
                'proposals': proposals,
                'total_generated': len(proposals),
                'agent': self.name,
                'generation_criteria': {
                    'avg_duration_threshold': 20,
                    'error_rate_threshold': 0.05,
                    'alignment_threshold': 0.8
                }
            }

        except Exception as e:
            self.logger.error(f"Proposal generation failed: {e}")
            return {
                'success': False,
                'error': str(e),
                'agent': self.name
            }

    def get_capabilities(self) -> List[str]:
        return ['proposal_generation', 'improvement_planning', 'priority_assessment']

class DialogueHandler(BaseAgent):
    """Agent for handling communication and narrative generation"""

    def __init__(self, memory_engine=None):
        super().__init__("dialogue_handler", memory_engine)

    def execute(self, task: AgentTask) -> Dict[str, Any]:
        """Handle dialogue and communication tasks"""
        try:
            params = task.parameters
            task_type = params.get('task_type', 'format_response')

            if task_type == 'format_response':
                return self._format_response(params)
            elif task_type == 'generate_narrative':
                return self._generate_narrative(params)
            elif task_type == 'translate_message':
                return self._translate_message(params)
            else:
                return {
                    'success': False,
                    'error': f'Unsupported task type: {task_type}',
                    'agent': self.name
                }

        except Exception as e:
            self.logger.error(f"Dialogue handling failed: {e}")
            return {
                'success': False,
                'error': str(e),
                'agent': self.name
            }

    def _format_response(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Format a response using templates"""
        response_type = params.get('response_type', 'info')
        data = params.get('data', {})
        language = params.get('language', 'vi')

        templates = {
            'success': {
                'vi': '✅ Hoàn thành thành công: {message}',
                'en': '✅ Successfully completed: {message}'
            },
            'error': {
                'vi': '❌ Lỗi xảy ra: {error}',
                'en': '❌ Error occurred: {error}'
            },
            'info': {
                'vi': 'ℹ️ Thông tin: {info}',
                'en': 'ℹ️ Information: {info}'
            },
            'analysis_complete': {
                'vi': '📊 Phân tích hoàn tất: {analysis_summary}',
                'en': '📊 Analysis completed: {analysis_summary}'
            }
        }

        template = templates.get(response_type, {}).get(language, '{data}')

        try:
            formatted_message = template.format(**data)
        except KeyError:
            formatted_message = f"Formatted response: {data}"

        return {
            'success': True,
            'formatted_message': formatted_message,
            'template_used': response_type,
            'language': language,
            'agent': self.name
        }

    def _generate_narrative(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Generate narrative for system events"""
        event_type = params.get('event_type', 'general')
        context = params.get('context', {})

        narratives = {
            'agent_coordination': 'Hệ thống multi-agent đang phối hợp xử lý tác vụ...',
            'performance_analysis': 'Đã hoàn thành phân tích hiệu suất hệ thống',
            'improvement_proposal': 'Sinh ra đề xuất cải tiến dựa trên phân tích',
            'system_optimization': 'Đang thực hiện tối ưu hóa hệ thống'
        }

        narrative = narratives.get(event_type, f'Xử lý sự kiện: {event_type}')

        return {
            'success': True,
            'narrative': narrative,
            'event_type': event_type,
            'context': context,
            'agent': self.name
        }

    def _translate_message(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Simple message translation (placeholder)"""
        message = params.get('message', '')
        target_language = params.get('target_language', 'vi')

        # Simple translation mappings (in production would use proper translation)
        translations = {
            'en_to_vi': {
                'success': 'thành công',
                'error': 'lỗi',
                'analysis': 'phân tích',
                'proposal': 'đề xuất'
            }
        }

        # Simple word replacement
        translated = message
        if target_language == 'vi':
            for en_word, vi_word in translations.get('en_to_vi', {}).items():
                translated = translated.replace(en_word, vi_word)

        return {
            'success': True,
            'translated_message': translated,
            'original_language': 'auto-detected',
            'target_language': target_language,
            'agent': self.name
        }

    def get_capabilities(self) -> List[str]:
        return ['response_formatting', 'narrative_generation', 'translation', 'communication']

class WeightedFairQueue:
    """Weighted Fair Queuing implementation for task scheduling"""

    def __init__(self):
        self.queues = {}  # agent_name -> queue
        self.weights = {}  # agent_name -> weight
        self.virtual_times = {}  # agent_name -> virtual_time
        self.global_virtual_time = 0.0

    def add_agent(self, agent_name: str, weight: float = 1.0):
        """Add an agent to the scheduling system"""
        self.queues[agent_name] = queue.Queue()
        self.weights[agent_name] = weight
        self.virtual_times[agent_name] = 0.0

    def enqueue_task(self, agent_name: str, task: AgentTask):
        """Enqueue a task for a specific agent"""
        if agent_name in self.queues:
            task.assigned_at = datetime.now()
            self.queues[agent_name].put(task)
        else:
            raise ValueError(f"Agent {agent_name} not registered in WFQ")

    def dequeue_task(self) -> Optional[tuple[str, AgentTask]]:
        """Dequeue next task based on WFQ algorithm"""
        eligible_agents = []

        for agent_name in self.queues:
            if not self.queues[agent_name].empty():
                eligible_agents.append(agent_name)

        if not eligible_agents:
            return None

        # Select agent with minimum virtual time
        selected_agent = min(eligible_agents,
                           key=lambda a: self.virtual_times[a])

        task = self.queues[selected_agent].get()

        # Update virtual time
        service_time = 1.0  # Simplified service time
        self.virtual_times[selected_agent] += service_time / self.weights[selected_agent]
        self.global_virtual_time = min(self.virtual_times.values())

        return selected_agent, task

    def get_queue_stats(self) -> Dict[str, Any]:
        """Get queue statistics"""
        stats = {}
        for agent_name in self.queues:
            stats[agent_name] = {
                'queue_size': self.queues[agent_name].qsize(),
                'weight': self.weights[agent_name],
                'virtual_time': self.virtual_times[agent_name]
            }
        stats['global_virtual_time'] = self.global_virtual_time
        return stats

class MultiAgentCoordinator:
    """Main coordinator for multi-agent system with WFQ and CAP"""

    def __init__(self, memory_engine=None):
        self.memory_engine = memory_engine
        self.logger = logging.getLogger(__name__)

        # Agent registry
        self.agents = {}
        self.agent_metrics = {}

        # Task scheduling
        self.wfq_scheduler = WeightedFairQueue()
        self.task_queue = queue.Queue()
        self.result_queue = queue.Queue()

        # Threading control
        self.running = False
        self.coordinator_thread = None

        # CAP (Cognitive Avalanche Protocol) parameters
        self.cap_efficiency_factor = 1.0
        self.cap_learning_rate = 0.3
        self.cap_cycle_count = 0

        # Performance tracking
        self.coordination_metrics = {
            'total_tasks': 0,
            'successful_tasks': 0,
            'total_coordination_time': 0.0,
            'agent_utilization': {}
        }

        # Initialize default agents
        self._initialize_default_agents()

    def _initialize_default_agents(self):
        """Initialize the default agent set"""
        # Metrics analyzer agent
        self.register_agent("metrics_analyzer", MetricsAnalyzer(self.memory_engine), weight=0.8)

        # Proposal generator agent
        self.register_agent("proposal_generator", ProposalGenerator(self.memory_engine), weight=0.6)

        # Dialogue handler agent
        self.register_agent("dialogue_handler", DialogueHandler(self.memory_engine), weight=0.4)

        self.logger.info("Default agents initialized")

    def register_agent(self, name: str, agent_instance: BaseAgent, weight: float = 1.0):
        """Register an agent with the coordinator"""
        self.agents[name] = agent_instance
        self.agent_metrics[name] = AgentMetrics(name=name)
        self.wfq_scheduler.add_agent(name, weight)

        self.logger.info(f"Agent registered: {name} (weight: {weight})")

    def start(self):
        """Start the multi-agent coordination system"""
        if self.running:
            return

        self.running = True
        self.coordinator_thread = threading.Thread(target=self._coordination_loop, daemon=True)
        self.coordinator_thread.start()

        self.logger.info("Multi-agent coordinator started")

    def stop(self):
        """Stop the coordination system safely"""
        self.running = False
        if self.coordinator_thread and self.coordinator_thread.is_alive():
            self.coordinator_thread.join(timeout=5)

        self.logger.info("Multi-agent coordinator stopped")

    def coordinate_task(self, task_type: str, parameters: Dict[str, Any],
                       priority: int = 1) -> str:
        """Submit a task for multi-agent coordination"""
        task_id = f"task_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}"

        # Determine best agent for task
        assigned_agent = self._determine_best_agent(task_type, parameters)

        task = AgentTask(
            id=task_id,
            agent_name=assigned_agent,
            task_type=task_type,
            parameters=parameters,
            priority=priority,
            created_at=datetime.now()
        )

        # Alignment check before task assignment
        alignment_score = self._alignment_check(task_type, parameters)
        if alignment_score < 0.8:
            self.logger.warning(f"Task {task_id} failed alignment check: {alignment_score}")
            return None

        # Enqueue task
        self.wfq_scheduler.enqueue_task(assigned_agent, task)
        self.coordination_metrics['total_tasks'] += 1

        self.logger.info(f"Task {task_id} assigned to {assigned_agent}")
        return task_id

    def get_task_result(self, task_id: str, timeout: float = 30.0) -> Optional[Dict[str, Any]]:
        """Get result for a specific task"""
        start_time = time.time()

        while time.time() - start_time < timeout:
            try:
                result = self.result_queue.get(timeout=1.0)
                if result.get('task_id') == task_id:
                    return result
                else:
                    # Put back for other consumers
                    self.result_queue.put(result)
            except queue.Empty:
                continue

        return None

    def _coordination_loop(self):
        """Main coordination loop"""
        while self.running:
            try:
                # Dequeue next task using WFQ
                agent_task_pair = self.wfq_scheduler.dequeue_task()

                if agent_task_pair:
                    agent_name, task = agent_task_pair
                    self._execute_agent_task(agent_name, task)
                else:
                    time.sleep(0.1)  # No tasks available

                # Apply CAP learning periodically
                self.cap_cycle_count += 1
                if self.cap_cycle_count % 100 == 0:
                    self._apply_cap_learning()

            except Exception as e:
                self.logger.error(f"Coordination loop error: {e}")
                time.sleep(1.0)

    def _execute_agent_task(self, agent_name: str, task: AgentTask):
        """Execute a task using the specified agent"""
        start_time = time.time()

        try:
            agent = self.agents[agent_name]

            # Execute task
            result = agent.execute(task)
            execution_time = time.time() - start_time

            # Update agent metrics
            success = result.get('success', False)
            agent.update_metrics(execution_time, success)

            # Update coordination metrics
            if success:
                self.coordination_metrics['successful_tasks'] += 1

            self.coordination_metrics['total_coordination_time'] += execution_time

            # Store result
            task.result = result
            task.success = success
            task.completed_at = datetime.now()

            # Put result in queue
            result_data = {
                'task_id': task.id,
                'agent_name': agent_name,
                'success': success,
                'result': result,
                'execution_time': execution_time,
                'completed_at': task.completed_at.isoformat()
            }

            self.result_queue.put(result_data)

            # Log to memory if available
            if self.memory_engine:
                self.memory_engine.log_event(
                    event_type="agent_task_completed",
                    source=f"multi_agent.{agent_name}",
                    details=f"Task: {task.task_type}, Success: {success}",
                    duration=execution_time,
                    success=success,
                    alignment_score=1.0 if success else 0.5
                )

        except Exception as e:
            self.logger.error(f"Agent task execution failed: {e}")

            # Create error result
            error_result = {
                'task_id': task.id,
                'agent_name': agent_name,
                'success': False,
                'error': str(e),
                'execution_time': time.time() - start_time
            }

            self.result_queue.put(error_result)

    def _determine_best_agent(self, task_type: str, parameters: Dict[str, Any]) -> str:
        """Determine the best agent for a given task"""
        # Simple task routing logic
        task_agent_mapping = {
            'performance_analysis': 'metrics_analyzer',
            'metrics_analysis': 'metrics_analyzer',
            'generate_proposals': 'proposal_generator',
            'improvement_planning': 'proposal_generator',
            'format_response': 'dialogue_handler',
            'generate_narrative': 'dialogue_handler',
            'translate_message': 'dialogue_handler'
        }

        # Default to metrics_analyzer if not found
        return task_agent_mapping.get(task_type, 'metrics_analyzer')

    def _alignment_check(self, task_type: str, parameters: Dict[str, Any]) -> float:
        """Check alignment of task with system values"""
        # Simple alignment scoring
        alignment_score = 0.9  # Base score

        # Reduce score for potentially risky operations
        risky_operations = ['system_modification', 'external_api_call', 'data_deletion']
        if task_type in risky_operations:
            alignment_score -= 0.2

        # Check for safety keywords in parameters
        safety_keywords = ['safe', 'secure', 'validate', 'check']
        param_text = str(parameters).lower()

        safety_mentions = sum(1 for keyword in safety_keywords if keyword in param_text)
        alignment_score += min(safety_mentions * 0.05, 0.1)

        return min(alignment_score, 1.0)

    def _apply_cap_learning(self):
        """Apply Cognitive Avalanche Protocol for performance learning"""
        try:
            # Calculate overall system efficiency
            total_tasks = self.coordination_metrics['total_tasks']
            successful_tasks = self.coordination_metrics['successful_tasks']

            if total_tasks > 0:
                current_success_rate = successful_tasks / total_tasks

                # Apply CAP learning
                if current_success_rate > 0.8:
                    # System performing well, increase efficiency
                    self.cap_efficiency_factor *= (1 + self.cap_learning_rate)
                    self.cap_efficiency_factor = min(self.cap_efficiency_factor, 2.0)
                elif current_success_rate < 0.6:
                    # System struggling, decrease efficiency factor
                    self.cap_efficiency_factor *= (1 - self.cap_learning_rate / 2)
                    self.cap_efficiency_factor = max(self.cap_efficiency_factor, 0.5)

                self.logger.info(f"CAP applied: efficiency_factor={self.cap_efficiency_factor:.2f}, "
                               f"success_rate={current_success_rate:.2f}")

                # Log CAP event
                if self.memory_engine:
                    self.memory_engine.log_event(
                        event_type="cap_learning_applied",
                        source="multi_agent_coordinator",
                        details=f"Efficiency factor: {self.cap_efficiency_factor:.2f}",
                        success=True,
                        alignment_score=1.0
                    )

        except Exception as e:
            self.logger.error(f"CAP learning failed: {e}")

    def get_system_status(self) -> Dict[str, Any]:
        """Get comprehensive system status"""
        # Calculate agent utilization
        agent_utilization = {}
        for name, agent in self.agents.items():
            metrics = agent.metrics
            agent_utilization[name] = {
                'total_tasks': metrics.total_tasks,
                'success_rate': metrics.success_rate,
                'avg_execution_time': metrics.average_execution_time,
                'last_active': metrics.last_active.isoformat() if metrics.last_active else None,
                'efficiency_factor': metrics.efficiency_factor
            }

        return {
            'running': self.running,
            'cap_efficiency_factor': self.cap_efficiency_factor,
            'cap_cycle_count': self.cap_cycle_count,
            'coordination_metrics': self.coordination_metrics,
            'agent_utilization': agent_utilization,
            'wfq_stats': self.wfq_scheduler.get_queue_stats(),
            'registered_agents': list(self.agents.keys()),
            'total_agents': len(self.agents)
        }

    def get_agent_capabilities(self) -> Dict[str, List[str]]:
        """Get capabilities of all registered agents"""
        capabilities = {}
        for name, agent in self.agents.items():
            capabilities[name] = agent.get_capabilities()
        return capabilities

if __name__ == "__main__":
    # Test the multi-agent coordinator
    coordinator = MultiAgentCoordinator()

    try:
        coordinator.start()

        # Test metrics analysis task
        task_id = coordinator.coordinate_task(
            task_type="performance_analysis",
            parameters={'hours_back': 24, 'metric_types': ['all']},
            priority=1
        )

        print(f"Submitted metrics analysis task: {task_id}")

        # Wait for result
        result = coordinator.get_task_result(task_id, timeout=10.0)
        if result:
            print(f"Task result: {result['success']}")
            if result['success']:
                analysis = result['result'].get('analysis', {})
                print(f"Analysis: avg_duration={analysis.get('avg_duration', 'N/A')}, "
                      f"error_rate={analysis.get('error_rate', 'N/A')}")
        else:
            print("No result received")

        # Test proposal generation
        task_id2 = coordinator.coordinate_task(
            task_type="generate_proposals",
            parameters={
                'analysis_data': {
                    'avg_duration': 25.0,  # Over threshold
                    'error_rate': 0.08,    # Over threshold
                    'avg_alignment_score': 0.75  # Under threshold
                },
                'priority': 'high'
            },
            priority=1
        )

        result2 = coordinator.get_task_result(task_id2, timeout=10.0)
        if result2 and result2['success']:
            proposals = result2['result'].get('proposals', [])
            print(f"Generated {len(proposals)} improvement proposals")

        # Get system status
        status = coordinator.get_system_status()
        print(f"System status: {status['total_agents']} agents, "
              f"efficiency_factor={status['cap_efficiency_factor']:.2f}")

        time.sleep(2)

    finally:
        coordinator.stop()
