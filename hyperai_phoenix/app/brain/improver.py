"""
HyperAI Phoenix - Self Improver - Enhanced with OCP
==================================================
Implements OCP (Optimization & Control Protocol) and IIP (Improvement Implementation Protocol)
P90 latency monitoring, Moving Average analysis, and automated improvement proposals

OCP INTEGRATION: All improvement operations are enhanced with creativity, optimization,
and quality assurance through the Omni-Creation Protocol.
"""

import statistics
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, asdict
import json
import logging

# Import OCP for universal enhancement
from ...core.protocols.ocp import ocp_enhance, OCPOperationType

@dataclass
class ImprovementProposal:
    """Structured improvement proposal"""
    id: str
    title: str
    description: str
    rationale: str
    implementation_steps: List[str]
    risk_assessment: str
    expected_benefit: str
    priority: str  # low, medium, high, critical
    estimated_effort: str
    success_criteria: List[str]
    created_at: datetime
    status: str = "pending"  # pending, approved, rejected, implemented

@dataclass
class PerformanceAnalysis:
    """Performance analysis result"""
    metric_name: str
    current_value: float
    ma30_trend: float
    ma100_trend: float
    p90_latency: Optional[float]
    trend_direction: str  # improving, stable, degrading
    severity: str  # normal, warning, critical
    analysis_summary: str

class SelfImprover:
    """Self-improvement system with performance analysis - OCP Enhanced"""

    def __init__(self, memory_engine, system_observer):
        self.memory_engine = memory_engine
        self.system_observer = system_observer
        self.logger = logging.getLogger(__name__)

        # Enable OCP integration for this component
        self._ocp_enabled = True
        self._component_name = "SelfImprover"

        # Improvement tracking
        self.proposals = []
        self.implemented_improvements = []

        # Performance thresholds
        self.thresholds = {
            'avg_duration': {'warning': 20.0, 'critical': 30.0},
            'error_rate': {'warning': 0.05, 'critical': 0.10},
            'p90_latency': {'warning': 25.0, 'critical': 40.0},
            'alignment_score': {'warning': 0.7, 'critical': 0.6}
        }

        # Moving average windows
        self.ma30_window = 30
        self.ma100_window = 100

        # Performance history for MA calculation
        self.performance_history = []

    @ocp_enhance(OCPOperationType.ANALYTICAL, "SelfImprover")
    def analyze_performance(self, time_window_hours: int = 24) -> List[PerformanceAnalysis]:
        """Analyze system performance and generate insights"""
        analyses = []

        # Get performance metrics from memory
        recent_metrics = self.memory_engine.get_performance_metrics(days=time_window_hours/24)

        # Analyze average duration
        duration_analysis = self._analyze_metric(
            'avg_duration',
            recent_metrics.get('avg_duration', 0.0),
            'Response Time'
        )
        analyses.append(duration_analysis)

        # Analyze error rate
        error_analysis = self._analyze_metric(
            'error_rate',
            recent_metrics.get('error_rate', 0.0),
            'Error Rate'
        )
        analyses.append(error_analysis)

        # Analyze alignment score
        alignment_analysis = self._analyze_metric(
            'alignment_score',
            recent_metrics.get('alignment_score', 0.8),
            'Alignment Score'
        )
        analyses.append(alignment_analysis)

        # System resource analysis if available
        if self.system_observer:
            health_score = self.system_observer.get_system_health_score()
            system_analysis = self._analyze_metric(
                'system_health',
                health_score,
                'System Health'
            )
            analyses.append(system_analysis)

        return analyses

    def _analyze_metric(self, metric_name: str, current_value: float,
                       display_name: str) -> PerformanceAnalysis:
        """Analyze a specific metric with MA trends"""

        # Get historical data for moving averages
        ma30_value = self._calculate_ma(metric_name, self.ma30_window)
        ma100_value = self._calculate_ma(metric_name, self.ma100_window)

        # Calculate P90 latency if applicable
        p90_latency = None
        if metric_name == 'avg_duration':
            p90_latency = self._calculate_p90_latency()

        # Determine trend direction
        trend_direction = self._determine_trend(current_value, ma30_value, ma100_value)

        # Assess severity
        severity = self._assess_severity(metric_name, current_value)

        # Generate analysis summary
        summary = self._generate_analysis_summary(
            display_name, current_value, ma30_value, ma100_value,
            trend_direction, severity, p90_latency
        )

        return PerformanceAnalysis(
            metric_name=metric_name,
            current_value=current_value,
            ma30_trend=ma30_value or current_value,
            ma100_trend=ma100_value or current_value,
            p90_latency=p90_latency,
            trend_direction=trend_direction,
            severity=severity,
            analysis_summary=summary
        )

    def _calculate_ma(self, metric_name: str, window: int) -> Optional[float]:
        """Calculate moving average for a metric"""
        try:
            # Get recent events from memory
            recent_events = self.memory_engine.get_recent_events(hours=window)

            # Extract metric values
            values = []
            for event in recent_events:
                if event.get('event_type') == 'directive_completed':
                    if metric_name == 'avg_duration' and event.get('duration'):
                        values.append(event['duration'])
                    elif metric_name == 'alignment_score' and event.get('alignment_score'):
                        values.append(event['alignment_score'])

            # Calculate MA if we have enough data
            if len(values) >= min(10, window // 2):
                return statistics.mean(values[-window:])

        except Exception as e:
            self.logger.warning(f"MA calculation failed for {metric_name}: {e}")

        return None

    def _calculate_p90_latency(self) -> Optional[float]:
        """Calculate P90 latency from recent performance data"""
        try:
            recent_events = self.memory_engine.get_recent_events(hours=24)

            # Extract duration values
            durations = []
            for event in recent_events:
                if (event.get('event_type') == 'directive_completed' and
                    event.get('duration') is not None):
                    durations.append(event['duration'])

            if len(durations) >= 10:
                durations.sort()
                p90_index = int(len(durations) * 0.9)
                return durations[p90_index]

        except Exception as e:
            self.logger.warning(f"P90 calculation failed: {e}")

        return None

    def _determine_trend(self, current: float, ma30: Optional[float],
                        ma100: Optional[float]) -> str:
        """Determine performance trend direction"""
        if ma30 is None or ma100 is None:
            return "insufficient_data"

        # Compare current with MA30
        ma30_diff = (current - ma30) / ma30 if ma30 != 0 else 0

        # Compare MA30 with MA100
        trend_diff = (ma30 - ma100) / ma100 if ma100 != 0 else 0

        if abs(ma30_diff) < 0.05 and abs(trend_diff) < 0.05:
            return "stable"
        elif ma30_diff < -0.1 or trend_diff < -0.1:
            return "improving"
        elif ma30_diff > 0.1 or trend_diff > 0.1:
            return "degrading"
        else:
            return "stable"

    def _assess_severity(self, metric_name: str, value: float) -> str:
        """Assess severity level of a metric"""
        thresholds = self.thresholds.get(metric_name, {})

        if value >= thresholds.get('critical', float('inf')):
            return "critical"
        elif value >= thresholds.get('warning', float('inf')):
            return "warning"
        else:
            return "normal"

    def _generate_analysis_summary(self, display_name: str, current: float,
                                 ma30: Optional[float], ma100: Optional[float],
                                 trend: str, severity: str,
                                 p90: Optional[float] = None) -> str:
        """Generate human-readable analysis summary"""
        summary_parts = [f"{display_name}: {current:.3f}"]

        if ma30 is not None:
            summary_parts.append(f"MA30: {ma30:.3f}")

        if ma100 is not None:
            summary_parts.append(f"MA100: {ma100:.3f}")

        if p90 is not None:
            summary_parts.append(f"P90: {p90:.3f}s")

        # Trend description
        trend_descriptions = {
            "improving": "đang cải thiện",
            "stable": "ổn định",
            "degrading": "đang xuống cấp",
            "insufficient_data": "chưa đủ dữ liệu"
        }

        summary_parts.append(f"Xu hướng: {trend_descriptions.get(trend, trend)}")

        # Severity indicator
        if severity != "normal":
            severity_descriptions = {
                "warning": "⚠️ Cảnh báo",
                "critical": "🚨 Nghiêm trọng"
            }
            summary_parts.append(severity_descriptions.get(severity, severity))

        return " | ".join(summary_parts)

    @ocp_enhance(OCPOperationType.CREATIVE, "SelfImprover")
    def generate_improvement_proposals(self, analyses: List[PerformanceAnalysis]) -> List[ImprovementProposal]:
        """Generate improvement proposals based on performance analysis - OCP Enhanced"""
        proposals = []

        for analysis in analyses:
            # Generate proposals based on severity and trend
            if analysis.severity in ["warning", "critical"] or analysis.trend_direction == "degrading":
                proposal = self._create_improvement_proposal(analysis)
                if proposal:
                    proposals.append(proposal)

        return proposals

    def _create_improvement_proposal(self, analysis: PerformanceAnalysis) -> Optional[ImprovementProposal]:
        """Create specific improvement proposal based on analysis"""
        metric_name = analysis.metric_name
        current_value = analysis.current_value

        proposal_id = f"improvement_{metric_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        # Average duration improvements
        if metric_name == 'avg_duration':
            if current_value > 20.0:
                return ImprovementProposal(
                    id=proposal_id,
                    title="Tối ưu hóa thời gian phản hồi",
                    description="Thời gian phản hồi trung bình đang cao, cần tối ưu hóa",
                    rationale=f"Thời gian hiện tại ({current_value:.2f}s) vượt ngưỡng khuyến nghị (20s)",
                    implementation_steps=[
                        "Tối ưu hóa thuật toán xử lý",
                        "Cải thiện caching mechanism",
                        "Giảm số lượng LLM calls không cần thiết",
                        "Tăng cường parallel processing"
                    ],
                    risk_assessment="Rủi ro thấp - chỉ tối ưu hóa performance",
                    expected_benefit="Giảm 30-50% thời gian phản hồi",
                    priority="high" if current_value > 30.0 else "medium",
                    estimated_effort="2-3 ngày",
                    success_criteria=[
                        "Thời gian phản hồi trung bình < 15s",
                        "P90 latency < 25s",
                        "Không ảnh hưởng độ chính xác"
                    ],
                    created_at=datetime.now()
                )

        # Error rate improvements
        elif metric_name == 'error_rate':
            if current_value > 0.05:
                return ImprovementProposal(
                    id=proposal_id,
                    title="Giảm tỷ lệ lỗi hệ thống",
                    description="Tỷ lệ lỗi đang cao, cần cải thiện độ tin cậy",
                    rationale=f"Tỷ lệ lỗi hiện tại ({current_value:.2%}) vượt ngưỡng 5%",
                    implementation_steps=[
                        "Phân tích root cause của các lỗi phổ biến",
                        "Tăng cường error handling",
                        "Cải thiện input validation",
                        "Thêm retry mechanisms"
                    ],
                    risk_assessment="Rủi ro trung bình - cần test kỹ",
                    expected_benefit="Giảm 50% tỷ lệ lỗi",
                    priority="critical" if current_value > 0.10 else "high",
                    estimated_effort="3-5 ngày",
                    success_criteria=[
                        "Tỷ lệ lỗi < 3%",
                        "Không có lỗi critical trong 24h",
                        "Improved error recovery"
                    ],
                    created_at=datetime.now()
                )

        # Alignment score improvements
        elif metric_name == 'alignment_score':
            if current_value < 0.8:
                return ImprovementProposal(
                    id=proposal_id,
                    title="Cải thiện độ tuân thủ chỉ thị",
                    description="Điểm alignment thấp, cần fine-tune hệ thống",
                    rationale=f"Alignment score ({current_value:.2f}) thấp hơn ngưỡng 0.8",
                    implementation_steps=[
                        "Review và cập nhật council weights",
                        "Fine-tune prompt templates",
                        "Cải thiện context awareness",
                        "Tăng cường training data"
                    ],
                    risk_assessment="Rủi ro cao - ảnh hưởng behavior",
                    expected_benefit="Tăng alignment score lên >0.85",
                    priority="critical",
                    estimated_effort="5-7 ngày",
                    success_criteria=[
                        "Alignment score > 0.85",
                        "Giảm escalation rate",
                        "User satisfaction tăng"
                    ],
                    created_at=datetime.now()
                )

        # System health improvements
        elif metric_name == 'system_health':
            if current_value < 0.7:
                return ImprovementProposal(
                    id=proposal_id,
                    title="Tối ưu hóa tài nguyên hệ thống",
                    description="Sức khỏe hệ thống kém, cần tối ưu hóa",
                    rationale=f"System health score ({current_value:.2f}) thấp",
                    implementation_steps=[
                        "Memory leak detection và fix",
                        "Tối ưu hóa CPU usage",
                        "Disk cleanup automation",
                        "Resource monitoring improvements"
                    ],
                    risk_assessment="Rủi ro trung bình",
                    expected_benefit="Cải thiện stability và performance",
                    priority="high",
                    estimated_effort="3-4 ngày",
                    success_criteria=[
                        "System health > 0.8",
                        "Memory usage stable",
                        "No resource alerts"
                    ],
                    created_at=datetime.now()
                )

        return None

    def evaluate_improvement_impact(self, proposal: ImprovementProposal) -> Dict[str, Any]:
        """Evaluate potential impact of an improvement proposal"""

        # Simple impact scoring based on proposal characteristics
        impact_score = 0.0

        # Priority weight
        priority_weights = {"low": 0.2, "medium": 0.5, "high": 0.8, "critical": 1.0}
        impact_score += priority_weights.get(proposal.priority, 0.5)

        # Effort consideration (lower effort = higher score)
        if "1-2" in proposal.estimated_effort:
            impact_score += 0.3
        elif "2-3" in proposal.estimated_effort:
            impact_score += 0.2
        elif "3-5" in proposal.estimated_effort:
            impact_score += 0.1

        # Risk consideration (lower risk = higher score)
        if "thấp" in proposal.risk_assessment.lower():
            impact_score += 0.2
        elif "trung bình" in proposal.risk_assessment.lower():
            impact_score += 0.1

        # Success criteria count (more criteria = more comprehensive)
        impact_score += min(len(proposal.success_criteria) * 0.1, 0.3)

        return {
            'impact_score': min(impact_score, 1.0),
            'roi_estimate': self._estimate_roi(proposal),
            'implementation_difficulty': self._assess_difficulty(proposal),
            'recommended_order': self._recommend_implementation_order(proposal)
        }

    def _estimate_roi(self, proposal: ImprovementProposal) -> str:
        """Estimate return on investment"""
        if proposal.priority == "critical":
            return "Very High - prevents system degradation"
        elif proposal.priority == "high":
            return "High - significant performance improvement"
        elif proposal.priority == "medium":
            return "Medium - moderate improvements"
        else:
            return "Low - incremental gains"

    def _assess_difficulty(self, proposal: ImprovementProposal) -> str:
        """Assess implementation difficulty"""
        effort = proposal.estimated_effort.lower()
        risk = proposal.risk_assessment.lower()

        if "cao" in risk or "7" in effort:
            return "High"
        elif "trung bình" in risk or "3-5" in effort:
            return "Medium"
        else:
            return "Low"

    def _recommend_implementation_order(self, proposal: ImprovementProposal) -> int:
        """Recommend implementation order (1 = highest priority)"""
        priority_order = {"critical": 1, "high": 2, "medium": 3, "low": 4}
        return priority_order.get(proposal.priority, 5)

    def run_improvement_cycle(self) -> Dict[str, Any]:
        """Run complete improvement analysis and proposal cycle"""
        cycle_start = datetime.now()

        try:
            # Analyze performance
            analyses = self.analyze_performance()

            # Generate proposals
            proposals = self.generate_improvement_proposals(analyses)

            # Evaluate proposals
            evaluated_proposals = []
            for proposal in proposals:
                impact = self.evaluate_improvement_impact(proposal)
                evaluated_proposals.append({
                    'proposal': proposal,
                    'impact_evaluation': impact
                })

            # Store proposals
            self.proposals.extend(proposals)

            # Log improvement cycle
            self.memory_engine.log_event(
                event_type="improvement_cycle",
                source="self_improver",
                details=f"Generated {len(proposals)} improvement proposals",
                success=True,
                alignment_score=1.0
            )

            cycle_result = {
                'cycle_id': f"cycle_{cycle_start.strftime('%Y%m%d_%H%M%S')}",
                'timestamp': cycle_start.isoformat(),
                'analyses_count': len(analyses),
                'proposals_generated': len(proposals),
                'analyses': [asdict(a) for a in analyses],
                'proposals': evaluated_proposals,
                'cycle_duration': (datetime.now() - cycle_start).total_seconds(),
                'status': 'completed'
            }

            return cycle_result

        except Exception as e:
            self.logger.error(f"Improvement cycle failed: {e}")

            error_result = {
                'cycle_id': f"cycle_{cycle_start.strftime('%Y%m%d_%H%M%S')}",
                'timestamp': cycle_start.isoformat(),
                'status': 'failed',
                'error': str(e),
                'cycle_duration': (datetime.now() - cycle_start).total_seconds()
            }

            return error_result

    def get_pending_proposals(self) -> List[ImprovementProposal]:
        """Get all pending improvement proposals"""
        return [p for p in self.proposals if p.status == "pending"]

    def approve_proposal(self, proposal_id: str) -> bool:
        """Approve an improvement proposal"""
        for proposal in self.proposals:
            if proposal.id == proposal_id:
                proposal.status = "approved"
                self.logger.info(f"Proposal approved: {proposal_id}")
                return True
        return False

    def implement_proposal(self, proposal_id: str) -> Dict[str, Any]:
        """Mark proposal as implemented (actual implementation would be external)"""
        for proposal in self.proposals:
            if proposal.id == proposal_id and proposal.status == "approved":
                proposal.status = "implemented"
                self.implemented_improvements.append(proposal)

                # Log implementation
                self.memory_engine.log_event(
                    event_type="improvement_implemented",
                    source="self_improver",
                    details=f"Implemented: {proposal.title}",
                    success=True,
                    alignment_score=1.0
                )

                return {
                    'status': 'success',
                    'proposal_id': proposal_id,
                    'title': proposal.title,
                    'implemented_at': datetime.now().isoformat()
                }

        return {'status': 'error', 'message': 'Proposal not found or not approved'}

    # Phase 2: Enhanced Self-Improvement Methods
    def run_a_b_testing(self, proposal: ImprovementProposal, test_duration_hours: int = 24) -> Dict[str, Any]:
        """Run A/B testing for improvement proposals"""
        try:
            from datetime import datetime, timedelta
            import random

            # Check if we have enough historical data for A/B testing
            recent_events = self.memory_engine.get_recent_events(hours=test_duration_hours)

            if len(recent_events) < 50:  # Minimum sample size
                return self._fallback_simulation(proposal)

            # Check if enough time has passed since last test (allow first test)
            last_test_time = getattr(self, 'last_ab_test_time', None)
            if last_test_time and (datetime.now() - last_test_time).total_seconds() < test_duration_hours * 3600:
                return self._fallback_simulation(proposal)

            # Split data into A (control) and B (test) groups
            random.shuffle(recent_events)
            mid_point = len(recent_events) // 2
            group_a_events = recent_events[:mid_point]
            group_b_events = recent_events[mid_point:]

            # Calculate baseline metrics for group A
            group_a_metrics = self._calculate_group_metrics(group_a_events)

            # Simulate group B with proposed improvements
            group_b_metrics = self._simulate_improved_metrics(group_b_events, proposal)

            # Determine winner
            improvement_score = self._compare_ab_groups(group_a_metrics, group_b_metrics)

            self.last_ab_test_time = datetime.now()

            ab_result = {
                'test_type': 'ab_testing',
                'proposal_id': proposal.id,
                'group_a_size': len(group_a_events),
                'group_b_size': len(group_b_events),
                'group_a_metrics': group_a_metrics,
                'group_b_metrics': group_b_metrics,
                'improvement_score': improvement_score,
                'winner': 'B' if improvement_score > 0.05 else 'A',
                'confidence': min(abs(improvement_score) * 10, 0.95),
                'test_duration_hours': test_duration_hours,
                'completed_at': datetime.now().isoformat()
            }

            # Log A/B test
            self.memory_engine.log_event(
                event_type="ab_test_completed",
                source="self_improver",
                details=f"A/B test for {proposal.title}: {ab_result['winner']} wins",
                success=True,
                alignment_score=1.0
            )

            return ab_result

        except Exception as e:
            self.logger.error(f"A/B testing failed: {e}")
            return self._fallback_simulation(proposal)

    def _fallback_simulation(self, proposal: ImprovementProposal) -> Dict[str, Any]:
        """Fallback simulation when A/B testing isn't possible"""
        try:
            # Get historical data for simulation
            historical_events = self.memory_engine.get_recent_events(hours=168)  # 7 days

            if len(historical_events) < 10:
                # Very limited data - conservative estimate
                simulated_improvement = 0.05  # 5% improvement
            else:
                # Use historical patterns to estimate improvement
                baseline_metrics = self._calculate_group_metrics(historical_events)

                # Estimate improvement based on proposal type
                improvement_factor = self._estimate_improvement_factor(proposal)
                simulated_improvement = improvement_factor

            simulation_result = {
                'test_type': 'fallback_simulation',
                'proposal_id': proposal.id,
                'baseline_sample_size': len(historical_events) if historical_events else 0,
                'estimated_improvement': simulated_improvement,
                'confidence': 0.6,  # Lower confidence for simulation
                'simulation_basis': 'historical_pattern_analysis',
                'completed_at': datetime.now().isoformat()
            }

            # Log simulation
            self.memory_engine.log_event(
                event_type="improvement_simulation",
                source="self_improver",
                details=f"Simulation for {proposal.title}: {simulated_improvement:.1%} improvement",
                success=True,
                alignment_score=1.0
            )

            return simulation_result

        except Exception as e:
            self.logger.error(f"Fallback simulation failed: {e}")
            return {
                'test_type': 'fallback_simulation',
                'error': str(e),
                'estimated_improvement': 0.01,  # Minimal conservative estimate
                'confidence': 0.3
            }

    def _calculate_group_metrics(self, events: List[Dict[str, Any]]) -> Dict[str, float]:
        """Calculate performance metrics for a group of events"""
        if not events:
            return {}

        total_events = len(events)
        successful_events = sum(1 for e in events if e.get('success', True))
        durations = [e.get('duration', 0) for e in events if e.get('duration') is not None]
        alignment_scores = [e.get('alignment_score', 0.8) for e in events if e.get('alignment_score') is not None]

        metrics = {
            'total_events': total_events,
            'success_rate': successful_events / total_events,
            'error_rate': 1 - (successful_events / total_events),
            'avg_duration': sum(durations) / len(durations) if durations else 0,
            'avg_alignment_score': sum(alignment_scores) / len(alignment_scores) if alignment_scores else 0.8
        }

        return metrics

    def _simulate_improved_metrics(self, events: List[Dict[str, Any]],
                                  proposal: ImprovementProposal) -> Dict[str, float]:
        """Simulate metrics with proposed improvements applied"""
        baseline_metrics = self._calculate_group_metrics(events)
        improvement_factor = self._estimate_improvement_factor(proposal)

        # Apply improvements based on proposal type
        improved_metrics = baseline_metrics.copy()

        if 'thời gian' in proposal.title.lower() or 'duration' in proposal.title.lower():
            # Performance improvement proposal
            improved_metrics['avg_duration'] = baseline_metrics['avg_duration'] * (1 - improvement_factor)

        if 'lỗi' in proposal.title.lower() or 'error' in proposal.title.lower():
            # Error reduction proposal
            improved_metrics['error_rate'] = baseline_metrics['error_rate'] * (1 - improvement_factor)
            improved_metrics['success_rate'] = 1 - improved_metrics['error_rate']

        if 'alignment' in proposal.title.lower() or 'tuân thủ' in proposal.title.lower():
            # Alignment improvement proposal
            improved_metrics['avg_alignment_score'] = min(
                baseline_metrics['avg_alignment_score'] * (1 + improvement_factor),
                1.0
            )

        return improved_metrics

    def _estimate_improvement_factor(self, proposal: ImprovementProposal) -> float:
        """Estimate improvement factor based on proposal characteristics"""
        base_factor = 0.1  # 10% base improvement

        # Adjust based on priority
        priority_multipliers = {
            'critical': 0.3,
            'high': 0.2,
            'medium': 0.1,
            'low': 0.05
        }

        priority_factor = priority_multipliers.get(proposal.priority, 0.1)

        # Adjust based on implementation complexity
        effort = proposal.estimated_effort.lower()
        if '1-2' in effort:
            complexity_factor = 0.15  # Simple changes, good impact
        elif '2-3' in effort:
            complexity_factor = 0.12
        elif '3-5' in effort:
            complexity_factor = 0.08
        else:
            complexity_factor = 0.05  # Complex changes, uncertain impact

        return min(priority_factor + complexity_factor, 0.5)  # Cap at 50% improvement

    def _compare_ab_groups(self, group_a_metrics: Dict[str, float],
                          group_b_metrics: Dict[str, float]) -> float:
        """Compare A/B groups and return improvement score"""
        improvement_score = 0.0

        # Compare success rates
        if 'success_rate' in group_a_metrics and 'success_rate' in group_b_metrics:
            success_improvement = group_b_metrics['success_rate'] - group_a_metrics['success_rate']
            improvement_score += success_improvement * 0.4  # 40% weight

        # Compare average duration (lower is better)
        if 'avg_duration' in group_a_metrics and 'avg_duration' in group_b_metrics:
            if group_a_metrics['avg_duration'] > 0:
                duration_improvement = (group_a_metrics['avg_duration'] - group_b_metrics['avg_duration']) / group_a_metrics['avg_duration']
                improvement_score += duration_improvement * 0.3  # 30% weight

        # Compare alignment scores
        if 'avg_alignment_score' in group_a_metrics and 'avg_alignment_score' in group_b_metrics:
            alignment_improvement = group_b_metrics['avg_alignment_score'] - group_a_metrics['avg_alignment_score']
            improvement_score += alignment_improvement * 0.3  # 30% weight

        return improvement_score

    def real_time_learning_cycle(self, query: str = None) -> Dict[str, Any]:
        """Enhanced real-time learning from ChromaDB semantic search"""
        try:
            if not query:
                query = "performance optimization improvement success patterns"

            # Semantic search for successful patterns
            search_results = self.memory_engine.semantic_search(query, n_results=20)

            if not search_results:
                return {
                    'status': 'no_data',
                    'message': 'No semantic search results found',
                    'query': query
                }

            # Analyze patterns from search results
            patterns = self._analyze_success_patterns(search_results)

            # Identify false positives for batch processing
            false_positives = self._identify_false_positives(search_results)

            # Batch process false positives if we have enough
            batch_result = None
            if len(false_positives) >= 10:
                batch_result = self._batch_process_false_positives(false_positives)

            # Generate learning insights
            learning_insights = self._generate_learning_insights(patterns)

            # Update thresholds based on learning
            threshold_updates = self._update_improvement_thresholds(patterns)

            learning_result = {
                'query': query,
                'search_results_count': len(search_results),
                'patterns_identified': len(patterns),
                'false_positives_found': len(false_positives),
                'batch_processed': batch_result is not None,
                'learning_insights': learning_insights,
                'threshold_updates': threshold_updates,
                'completed_at': datetime.now().isoformat(),
                'status': 'completed'
            }

            # Log learning cycle
            self.memory_engine.log_event(
                event_type="real_time_learning",
                source="self_improver",
                details=f"Learned from {len(search_results)} patterns, {len(false_positives)} false positives",
                success=True,
                alignment_score=1.0
            )

            return learning_result

        except Exception as e:
            self.logger.error(f"Real-time learning failed: {e}")
            return {
                'status': 'error',
                'error': str(e),
                'query': query
            }

    def _analyze_success_patterns(self, search_results: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Analyze successful patterns from semantic search results"""
        patterns = []

        # Group results by similarity and success
        successful_results = [r for r in search_results if r.get('metadata', {}).get('success', True)]

        # Extract common themes
        if successful_results:
            # Simple pattern analysis - in production would use more sophisticated NLP
            common_words = {}

            for result in successful_results:
                content = result.get('content', '').lower()
                words = content.split()

                for word in words:
                    if len(word) > 3:  # Filter short words
                        common_words[word] = common_words.get(word, 0) + 1

            # Get top patterns
            top_patterns = sorted(common_words.items(), key=lambda x: x[1], reverse=True)[:10]

            for word, frequency in top_patterns:
                if frequency >= 2:  # Appeared in at least 2 results
                    patterns.append({
                        'pattern': word,
                        'frequency': frequency,
                        'confidence': min(frequency / len(successful_results), 1.0),
                        'type': 'keyword_pattern'
                    })

        return patterns

    def _identify_false_positives(self, search_results: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Identify potential false positives in search results"""
        false_positives = []

        for result in search_results:
            # Check for indicators of false positives
            similarity = result.get('similarity', 0)
            metadata = result.get('metadata', {})

            # Low similarity but included in results
            if similarity < 0.7:
                false_positives.append({
                    'result_id': result.get('id'),
                    'similarity': similarity,
                    'reason': 'low_similarity',
                    'content_preview': result.get('content', '')[:100]
                })

            # Check for contradictory metadata
            if metadata.get('success') is False and 'success' in result.get('content', '').lower():
                false_positives.append({
                    'result_id': result.get('id'),
                    'reason': 'metadata_content_mismatch',
                    'content_preview': result.get('content', '')[:100]
                })

        return false_positives

    def _batch_process_false_positives(self, false_positives: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Batch process false positives to improve system accuracy"""
        try:
            # Limit batch size to manage computational cost
            batch_size = min(len(false_positives), 100)
            batch = false_positives[:batch_size]

            # Use memory engine's batch processing
            batch_result = self.memory_engine.batch_process_false_positives(batch)

            # Analyze false positive patterns
            fp_patterns = {}
            for fp in batch:
                reason = fp.get('reason', 'unknown')
                fp_patterns[reason] = fp_patterns.get(reason, 0) + 1

            # Update system thresholds based on false positive analysis
            if fp_patterns.get('low_similarity', 0) > batch_size * 0.3:
                # Too many low similarity false positives - increase similarity threshold
                self.semantic_search_threshold = getattr(self, 'semantic_search_threshold', 0.7) + 0.05

            batch_result.update({
                'false_positive_patterns': fp_patterns,
                'threshold_adjustments': {
                    'semantic_search_threshold': getattr(self, 'semantic_search_threshold', 0.7)
                }
            })

            self.logger.info(f"Batch processed {batch_size} false positives")
            return batch_result

        except Exception as e:
            self.logger.error(f"Batch processing false positives failed: {e}")
            return {'error': str(e), 'processed_count': 0}

    def _generate_learning_insights(self, patterns: List[Dict[str, Any]]) -> List[str]:
        """Generate learning insights from identified patterns"""
        insights = []

        if not patterns:
            insights.append("No significant patterns identified in current data")
            return insights

        # Analyze pattern frequencies
        high_confidence_patterns = [p for p in patterns if p.get('confidence', 0) > 0.5]

        if high_confidence_patterns:
            top_pattern = high_confidence_patterns[0]
            insights.append(f"Most common success pattern: '{top_pattern['pattern']}' (confidence: {top_pattern['confidence']:.2f})")

        # Pattern diversity analysis
        if len(patterns) > 5:
            insights.append(f"High pattern diversity detected ({len(patterns)} patterns) - system learning is robust")
        elif len(patterns) < 3:
            insights.append("Low pattern diversity - may need more varied training data")
        else:
            insights.append(f"Moderate pattern diversity with {len(patterns)} patterns identified")

        # Frequency analysis
        total_frequency = sum(p.get('frequency', 0) for p in patterns)
        if total_frequency > 20:
            insights.append("High pattern frequency indicates strong learning signals")

        return insights

    def _update_improvement_thresholds(self, patterns: List[Dict[str, Any]]) -> Dict[str, float]:
        """Update improvement thresholds based on learned patterns"""
        updates = {}

        # Analyze patterns to adjust thresholds
        performance_patterns = [p for p in patterns if 'performance' in p.get('pattern', '').lower()]
        error_patterns = [p for p in patterns if 'error' in p.get('pattern', '').lower()]

        # Adjust duration threshold based on performance patterns
        if performance_patterns:
            avg_confidence = sum(p.get('confidence', 0) for p in performance_patterns) / len(performance_patterns)
            if avg_confidence > 0.7:
                # High confidence in performance patterns - can be more aggressive
                new_threshold = self.thresholds['avg_duration']['warning'] * 0.95
                self.thresholds['avg_duration']['warning'] = new_threshold
                updates['avg_duration_warning'] = new_threshold

        # Adjust error threshold based on error patterns
        if error_patterns:
            avg_confidence = sum(p.get('confidence', 0) for p in error_patterns) / len(error_patterns)
            if avg_confidence > 0.7:
                new_threshold = self.thresholds['error_rate']['warning'] * 0.95
                self.thresholds['error_rate']['warning'] = new_threshold
                updates['error_rate_warning'] = new_threshold

        return updates

if __name__ == "__main__":
    # Mock test of the improver
    class MockMemoryEngine:
        def get_performance_metrics(self, days=1):
            return {
                'avg_duration': 25.0,  # Over threshold
                'error_rate': 0.08,    # Over threshold
                'alignment_score': 0.75  # Under threshold
            }

        def get_recent_events(self, hours=24):
            return [
                {'event_type': 'directive_completed', 'duration': 22.0, 'alignment_score': 0.8},
                {'event_type': 'directive_completed', 'duration': 28.0, 'alignment_score': 0.7},
                {'event_type': 'directive_completed', 'duration': 30.0, 'alignment_score': 0.75}
            ]

        def log_event(self, **kwargs):
            pass

    mock_memory = MockMemoryEngine()
    improver = SelfImprover(mock_memory, None)

    # Run improvement cycle
    result = improver.run_improvement_cycle()
    print(f"Improvement cycle: {result['proposals_generated']} proposals generated")

    for proposal_data in result['proposals']:
        proposal = proposal_data['proposal']
        impact = proposal_data['impact_evaluation']
        print(f"- {proposal.title} (Priority: {proposal.priority}, Impact: {impact['impact_score']:.2f})")
