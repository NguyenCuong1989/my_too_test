"""
Performance Optimization System - System Efficiency Engine
=========================================================
Advanced performance monitoring and optimization system
"""

import json
import asyncio
import time
import psutil
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple
from collections import defaultdict, deque
import statistics

class PerformanceOptimizationSystem:
    """
    Advanced Performance Optimization System
    Monitors, analyzes and optimizes system performance in real-time
    """

    def __init__(self):
        self.metrics_history = defaultdict(deque)
        self.optimization_strategies = {}
        self.performance_targets = {}
        self.active_optimizations = {}
        self.bottleneck_detection = {}
        self.resource_usage = {}

        # Performance thresholds
        self.thresholds = {
            'cpu_usage': {'warning': 70, 'critical': 85},
            'memory_usage': {'warning': 75, 'critical': 90},
            'response_time': {'warning': 500, 'critical': 1000},  # milliseconds
            'throughput': {'warning': 100, 'critical': 50},  # requests/minute
            'error_rate': {'warning': 5, 'critical': 10}  # percentage
        }

        # Optimization techniques
        self.optimization_techniques = {
            'caching': {
                'description': 'implement_intelligent_caching',
                'effectiveness': 0.3,
                'complexity': 'medium'
            },
            'load_balancing': {
                'description': 'distribute_workload_efficiently',
                'effectiveness': 0.4,
                'complexity': 'high'
            },
            'resource_pooling': {
                'description': 'optimize_resource_allocation',
                'effectiveness': 0.25,
                'complexity': 'medium'
            },
            'algorithm_optimization': {
                'description': 'improve_algorithmic_efficiency',
                'effectiveness': 0.5,
                'complexity': 'high'
            },
            'parallel_processing': {
                'description': 'enable_concurrent_execution',
                'effectiveness': 0.4,
                'complexity': 'high'
            }
        }

        # Initialize monitoring
        self.monitoring_active = False
        self.optimization_history = []

    async def start_performance_monitoring(self) -> Dict[str, Any]:
        """Bắt đầu performance monitoring"""

        if self.monitoring_active:
            return {'status': 'already_monitoring'}

        self.monitoring_active = True

        # Start monitoring task
        monitoring_task = asyncio.create_task(self._continuous_monitoring())

        return {
            'status': 'monitoring_started',
            'monitoring_interval': '10_seconds',
            'metrics_tracked': list(self.thresholds.keys()),
            'task_id': id(monitoring_task)
        }

    async def _continuous_monitoring(self):
        """Continuous performance monitoring loop"""

        while self.monitoring_active:
            try:
                # Collect current metrics
                current_metrics = await self._collect_system_metrics()

                # Store metrics with timestamp
                timestamp = datetime.now()
                for metric_name, value in current_metrics.items():
                    self.metrics_history[metric_name].append((timestamp, value))

                    # Keep only recent history (last 1000 entries)
                    if len(self.metrics_history[metric_name]) > 1000:
                        self.metrics_history[metric_name].popleft()

                # Analyze performance and detect issues
                await self._analyze_performance_metrics(current_metrics)

                # Check for optimization opportunities
                await self._check_optimization_opportunities(current_metrics)

                # Wait for next monitoring cycle
                await asyncio.sleep(10)

            except Exception as e:
                print(f"Monitoring error: {e}")
                await asyncio.sleep(30)  # Longer wait on error

    async def _collect_system_metrics(self) -> Dict[str, float]:
        """Collect current system metrics"""

        try:
            # CPU usage
            cpu_usage = psutil.cpu_percent(interval=1)

            # Memory usage
            memory = psutil.virtual_memory()
            memory_usage = memory.percent

            # Disk usage
            disk = psutil.disk_usage('/')
            disk_usage = disk.percent

            # Network stats (simplified)
            network = psutil.net_io_counters()

            # Process count
            process_count = len(psutil.pids())

        except Exception:
            # Fallback metrics if psutil not available
            cpu_usage = self._simulate_cpu_usage()
            memory_usage = self._simulate_memory_usage()
            disk_usage = self._simulate_disk_usage()
            process_count = 50

        # Application-specific metrics (simulated)
        response_time = await self._measure_response_time()
        throughput = await self._calculate_throughput()
        error_rate = await self._calculate_error_rate()

        return {
            'cpu_usage': cpu_usage,
            'memory_usage': memory_usage,
            'disk_usage': disk_usage,
            'process_count': process_count,
            'response_time': response_time,
            'throughput': throughput,
            'error_rate': error_rate
        }

    def _simulate_cpu_usage(self) -> float:
        """Simulate CPU usage"""
        import random
        base_usage = 30 + random.gauss(0, 10)
        return max(0, min(100, base_usage))

    def _simulate_memory_usage(self) -> float:
        """Simulate memory usage"""
        import random
        base_usage = 45 + random.gauss(0, 15)
        return max(0, min(100, base_usage))

    def _simulate_disk_usage(self) -> float:
        """Simulate disk usage"""
        import random
        base_usage = 60 + random.gauss(0, 5)
        return max(0, min(100, base_usage))

    async def _measure_response_time(self) -> float:
        """Measure application response time"""

        start_time = time.time()

        # Simulate a typical operation
        await asyncio.sleep(0.1)  # 100ms base response

        end_time = time.time()
        response_time = (end_time - start_time) * 1000  # Convert to milliseconds

        # Add some variation
        import random
        variation = random.gauss(1.0, 0.2)
        return response_time * variation

    async def _calculate_throughput(self) -> float:
        """Calculate system throughput"""

        # Simulate throughput calculation
        import random
        base_throughput = 150 + random.gauss(0, 30)  # requests per minute
        return max(0, base_throughput)

    async def _calculate_error_rate(self) -> float:
        """Calculate error rate"""

        # Simulate error rate calculation
        import random
        base_error_rate = 2 + random.gauss(0, 1)  # percentage
        return max(0, min(100, base_error_rate))

    async def _analyze_performance_metrics(self, current_metrics: Dict[str, float]):
        """Analyze current performance metrics"""

        performance_status = {}

        for metric_name, value in current_metrics.items():
            if metric_name not in self.thresholds:
                continue

            thresholds = self.thresholds[metric_name]

            if value >= thresholds['critical']:
                status = 'critical'
            elif value >= thresholds['warning']:
                status = 'warning'
            else:
                status = 'normal'

            performance_status[metric_name] = {
                'value': value,
                'status': status,
                'threshold_warning': thresholds['warning'],
                'threshold_critical': thresholds['critical']
            }

        # Store performance analysis
        self.resource_usage[datetime.now().isoformat()] = performance_status

        # Trigger alerts for critical issues
        await self._handle_performance_alerts(performance_status)

    async def _handle_performance_alerts(self, performance_status: Dict[str, Dict[str, Any]]):
        """Handle performance alerts"""

        critical_metrics = [
            metric for metric, status in performance_status.items()
            if status['status'] == 'critical'
        ]

        warning_metrics = [
            metric for metric, status in performance_status.items()
            if status['status'] == 'warning'
        ]

        if critical_metrics:
            await self._trigger_emergency_optimization(critical_metrics)
        elif warning_metrics:
            await self._trigger_preventive_optimization(warning_metrics)

    async def _trigger_emergency_optimization(self, critical_metrics: List[str]):
        """Trigger emergency optimization for critical metrics"""

        for metric in critical_metrics:
            optimization = await self._select_emergency_optimization(metric)
            if optimization:
                await self._apply_optimization(optimization, priority='critical')

    async def _trigger_preventive_optimization(self, warning_metrics: List[str]):
        """Trigger preventive optimization for warning metrics"""

        for metric in warning_metrics:
            optimization = await self._select_preventive_optimization(metric)
            if optimization:
                await self._apply_optimization(optimization, priority='warning')

    async def _select_emergency_optimization(self, metric: str) -> Optional[Dict[str, Any]]:
        """Select emergency optimization for metric"""

        emergency_optimizations = {
            'cpu_usage': {
                'technique': 'parallel_processing',
                'action': 'distribute_cpu_intensive_tasks',
                'expected_improvement': 0.4
            },
            'memory_usage': {
                'technique': 'resource_pooling',
                'action': 'optimize_memory_allocation',
                'expected_improvement': 0.3
            },
            'response_time': {
                'technique': 'caching',
                'action': 'implement_aggressive_caching',
                'expected_improvement': 0.5
            }
        }

        return emergency_optimizations.get(metric)

    async def _select_preventive_optimization(self, metric: str) -> Optional[Dict[str, Any]]:
        """Select preventive optimization for metric"""

        preventive_optimizations = {
            'cpu_usage': {
                'technique': 'algorithm_optimization',
                'action': 'optimize_computational_algorithms',
                'expected_improvement': 0.2
            },
            'memory_usage': {
                'technique': 'caching',
                'action': 'implement_smart_caching',
                'expected_improvement': 0.25
            },
            'throughput': {
                'technique': 'load_balancing',
                'action': 'optimize_load_distribution',
                'expected_improvement': 0.3
            }
        }

        return preventive_optimizations.get(metric)

    async def _check_optimization_opportunities(self, current_metrics: Dict[str, float]):
        """Check for optimization opportunities"""

        opportunities = []

        # Analyze trends in metrics
        for metric_name, history in self.metrics_history.items():
            if len(history) < 10:  # Need enough history
                continue

            recent_values = [value for _, value in list(history)[-10:]]
            trend = await self._analyze_metric_trend(recent_values)

            if trend['direction'] == 'degrading' and trend['severity'] > 0.1:
                opportunity = {
                    'metric': metric_name,
                    'trend': trend,
                    'optimization_needed': True,
                    'urgency': 'high' if trend['severity'] > 0.3 else 'medium'
                }
                opportunities.append(opportunity)

        # Store opportunities
        if opportunities:
            await self._process_optimization_opportunities(opportunities)

    async def _analyze_metric_trend(self, values: List[float]) -> Dict[str, Any]:
        """Analyze trend in metric values"""

        if len(values) < 3:
            return {'direction': 'stable', 'severity': 0.0}

        # Simple trend analysis
        x_vals = list(range(len(values)))

        # Calculate slope
        n = len(values)
        sum_x = sum(x_vals)
        sum_y = sum(values)
        sum_xy = sum(x * y for x, y in zip(x_vals, values))
        sum_x2 = sum(x ** 2 for x in x_vals)

        denominator = n * sum_x2 - sum_x ** 2
        if denominator == 0:
            slope = 0
        else:
            slope = (n * sum_xy - sum_x * sum_y) / denominator

        # Determine direction and severity
        if abs(slope) < 0.1:
            direction = 'stable'
        elif slope > 0:
            direction = 'improving' if values[0] < statistics.mean(values) else 'degrading'
        else:
            direction = 'degrading' if values[0] < statistics.mean(values) else 'improving'

        severity = abs(slope) / (statistics.mean(values) if statistics.mean(values) > 0 else 1)

        return {
            'direction': direction,
            'severity': min(1.0, severity),
            'slope': slope
        }

    async def _process_optimization_opportunities(self, opportunities: List[Dict[str, Any]]):
        """Process optimization opportunities"""

        for opportunity in opportunities:
            metric = opportunity['metric']
            urgency = opportunity['urgency']

            # Select appropriate optimization
            optimization = await self._recommend_optimization(metric, urgency)

            if optimization:
                # Add to optimization queue
                await self._queue_optimization(optimization, opportunity)

    async def _recommend_optimization(self, metric: str, urgency: str) -> Optional[Dict[str, Any]]:
        """Recommend optimization based on metric and urgency"""

        recommendations = {
            ('cpu_usage', 'high'): {
                'technique': 'parallel_processing',
                'description': 'implement_multi_threading',
                'priority': 'high'
            },
            ('cpu_usage', 'medium'): {
                'technique': 'algorithm_optimization',
                'description': 'optimize_computational_complexity',
                'priority': 'medium'
            },
            ('memory_usage', 'high'): {
                'technique': 'resource_pooling',
                'description': 'implement_memory_pooling',
                'priority': 'high'
            },
            ('memory_usage', 'medium'): {
                'technique': 'caching',
                'description': 'optimize_memory_usage_patterns',
                'priority': 'medium'
            },
            ('response_time', 'high'): {
                'technique': 'caching',
                'description': 'implement_response_caching',
                'priority': 'high'
            },
            ('throughput', 'high'): {
                'technique': 'load_balancing',
                'description': 'implement_load_balancing',
                'priority': 'high'
            }
        }

        return recommendations.get((metric, urgency))

    async def _queue_optimization(self, optimization: Dict[str, Any], opportunity: Dict[str, Any]):
        """Queue optimization for execution"""

        optimization_id = f"opt_{int(datetime.now().timestamp())}"

        queued_optimization = {
            'id': optimization_id,
            'optimization': optimization,
            'opportunity': opportunity,
            'status': 'queued',
            'queued_at': datetime.now().isoformat(),
            'priority': optimization.get('priority', 'medium')
        }

        self.active_optimizations[optimization_id] = queued_optimization

    async def _apply_optimization(self, optimization: Dict[str, Any], priority: str = 'medium') -> Dict[str, Any]:
        """Apply optimization technique"""

        optimization_id = f"opt_{int(datetime.now().timestamp())}"

        # Simulate optimization application
        start_time = datetime.now()

        technique = optimization.get('technique', 'unknown')
        expected_improvement = optimization.get('expected_improvement', 0.1)

        # Simulate optimization process
        await self._execute_optimization_technique(technique)

        end_time = datetime.now()
        execution_time = (end_time - start_time).total_seconds()

        # Record optimization
        optimization_record = {
            'id': optimization_id,
            'technique': technique,
            'priority': priority,
            'start_time': start_time.isoformat(),
            'end_time': end_time.isoformat(),
            'execution_time': execution_time,
            'expected_improvement': expected_improvement,
            'status': 'completed'
        }

        self.optimization_history.append(optimization_record)

        return optimization_record

    async def _execute_optimization_technique(self, technique: str):
        """Execute specific optimization technique"""

        # Simulate different optimization techniques
        execution_times = {
            'caching': 2.0,
            'load_balancing': 5.0,
            'resource_pooling': 3.0,
            'algorithm_optimization': 10.0,
            'parallel_processing': 7.0
        }

        execution_time = execution_times.get(technique, 5.0)

        # Simulate execution with progress
        steps = 5
        for step in range(steps):
            await asyncio.sleep(execution_time / steps)
            # In real implementation, this would perform actual optimization

    async def analyze_performance_trends(self, time_window: int = 3600) -> Dict[str, Any]:
        """Analyze performance trends over time window (seconds)"""

        cutoff_time = datetime.now() - timedelta(seconds=time_window)

        trends = {}

        for metric_name, history in self.metrics_history.items():
            # Filter recent history
            recent_data = [
                (timestamp, value) for timestamp, value in history
                if timestamp >= cutoff_time
            ]

            if len(recent_data) < 5:
                continue

            values = [value for _, value in recent_data]
            timestamps = [timestamp for timestamp, _ in recent_data]

            # Calculate trend statistics
            trend_stats = {
                'average': statistics.mean(values),
                'median': statistics.median(values),
                'std_dev': statistics.stdev(values) if len(values) > 1 else 0,
                'min': min(values),
                'max': max(values),
                'trend': await self._analyze_metric_trend(values),
                'data_points': len(values),
                'time_span': (timestamps[-1] - timestamps[0]).total_seconds()
            }

            trends[metric_name] = trend_stats

        return {
            'analysis_window': time_window,
            'metrics_analyzed': len(trends),
            'trends': trends,
            'overall_health': await self._assess_overall_performance_health(trends)
        }

    async def _assess_overall_performance_health(self, trends: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
        """Assess overall performance health"""

        health_scores = {}

        for metric_name, trend_data in trends.items():
            average = trend_data['average']
            trend_direction = trend_data['trend']['direction']

            # Calculate health score based on thresholds and trends
            if metric_name in self.thresholds:
                thresholds = self.thresholds[metric_name]

                if average < thresholds['warning']:
                    base_score = 0.8
                elif average < thresholds['critical']:
                    base_score = 0.5
                else:
                    base_score = 0.2

                # Adjust based on trend
                if trend_direction == 'improving':
                    base_score = min(1.0, base_score + 0.2)
                elif trend_direction == 'degrading':
                    base_score = max(0.0, base_score - 0.3)

                health_scores[metric_name] = base_score

        overall_score = statistics.mean(health_scores.values()) if health_scores else 0.5

        return {
            'overall_score': overall_score,
            'individual_scores': health_scores,
            'health_status': 'excellent' if overall_score > 0.8 else
                           'good' if overall_score > 0.6 else
                           'fair' if overall_score > 0.4 else 'poor'
        }

    async def generate_optimization_report(self) -> Dict[str, Any]:
        """Generate comprehensive optimization report"""

        current_time = datetime.now()

        # Recent performance trends
        trends = await self.analyze_performance_trends(3600)  # Last hour

        # Optimization history summary
        recent_optimizations = [
            opt for opt in self.optimization_history
            if datetime.fromisoformat(opt['start_time']) > current_time - timedelta(hours=24)
        ]

        # Performance improvements
        improvements = await self._calculate_performance_improvements(recent_optimizations)

        # Current bottlenecks
        bottlenecks = await self._identify_current_bottlenecks()

        # Recommendations
        recommendations = await self._generate_optimization_recommendations(trends, bottlenecks)

        report = {
            'report_generated': current_time.isoformat(),
            'monitoring_status': 'active' if self.monitoring_active else 'inactive',
            'performance_trends': trends,
            'recent_optimizations': {
                'count': len(recent_optimizations),
                'techniques_used': list(set(opt['technique'] for opt in recent_optimizations)),
                'total_execution_time': sum(opt['execution_time'] for opt in recent_optimizations)
            },
            'performance_improvements': improvements,
            'current_bottlenecks': bottlenecks,
            'recommendations': recommendations,
            'system_health': trends.get('overall_health', {})
        }

        return report

    async def _calculate_performance_improvements(self, optimizations: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Calculate performance improvements from optimizations"""

        if not optimizations:
            return {'total_improvement': 0.0, 'by_technique': {}}

        total_expected_improvement = sum(
            opt.get('expected_improvement', 0.0) for opt in optimizations
        )

        by_technique = defaultdict(float)
        for opt in optimizations:
            technique = opt['technique']
            improvement = opt.get('expected_improvement', 0.0)
            by_technique[technique] += improvement

        return {
            'total_improvement': total_expected_improvement,
            'by_technique': dict(by_technique),
            'optimization_count': len(optimizations)
        }

    async def _identify_current_bottlenecks(self) -> List[Dict[str, Any]]:
        """Identify current system bottlenecks"""

        bottlenecks = []

        # Check current metrics against thresholds
        if self.metrics_history:
            for metric_name, history in self.metrics_history.items():
                if not history:
                    continue

                # Get latest value
                latest_timestamp, latest_value = history[-1]

                if metric_name in self.thresholds:
                    thresholds = self.thresholds[metric_name]

                    if latest_value >= thresholds['warning']:
                        severity = 'critical' if latest_value >= thresholds['critical'] else 'warning'

                        bottleneck = {
                            'metric': metric_name,
                            'current_value': latest_value,
                            'threshold': thresholds[severity],
                            'severity': severity,
                            'impact': await self._assess_bottleneck_impact(metric_name, latest_value)
                        }

                        bottlenecks.append(bottleneck)

        # Sort by severity and impact
        bottlenecks.sort(key=lambda x: (
            0 if x['severity'] == 'critical' else 1,
            -x['impact']
        ))

        return bottlenecks

    async def _assess_bottleneck_impact(self, metric_name: str, value: float) -> float:
        """Assess impact of bottleneck"""

        impact_weights = {
            'cpu_usage': 0.8,
            'memory_usage': 0.7,
            'response_time': 0.9,
            'throughput': 0.8,
            'error_rate': 1.0
        }

        base_impact = impact_weights.get(metric_name, 0.5)

        # Adjust based on severity
        if metric_name in self.thresholds:
            thresholds = self.thresholds[metric_name]
            if value >= thresholds['critical']:
                base_impact *= 1.5
            elif value >= thresholds['warning']:
                base_impact *= 1.2

        return min(1.0, base_impact)

    async def _generate_optimization_recommendations(self, trends: Dict[str, Any], bottlenecks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Generate optimization recommendations"""

        recommendations = []

        # Recommendations based on bottlenecks
        for bottleneck in bottlenecks[:3]:  # Top 3 bottlenecks
            metric = bottleneck['metric']
            severity = bottleneck['severity']

            recommendation = {
                'type': 'bottleneck_resolution',
                'metric': metric,
                'severity': severity,
                'recommended_technique': await self._recommend_optimization(metric, severity),
                'priority': 'high' if severity == 'critical' else 'medium',
                'expected_impact': bottleneck['impact']
            }

            recommendations.append(recommendation)

        # Recommendations based on trends
        trends_data = trends.get('trends', {})
        for metric_name, trend_data in trends_data.items():
            if trend_data['trend']['direction'] == 'degrading':
                recommendation = {
                    'type': 'trend_improvement',
                    'metric': metric_name,
                    'trend_severity': trend_data['trend']['severity'],
                    'recommended_action': 'monitor_and_optimize',
                    'priority': 'low'
                }

                recommendations.append(recommendation)

        # General recommendations
        if not recommendations:
            recommendations.append({
                'type': 'preventive_maintenance',
                'description': 'system_performing_well',
                'recommended_action': 'continue_monitoring',
                'priority': 'low'
            })

        return recommendations

    async def stop_monitoring(self) -> Dict[str, Any]:
        """Stop performance monitoring"""

        self.monitoring_active = False

        return {
            'status': 'monitoring_stopped',
            'final_report': await self.generate_optimization_report()
        }

# Global instance
performance_optimizer = PerformanceOptimizationSystem()

async def create_performance_optimization_system():
    """Tạo và khởi tạo performance optimization system"""

    return {
        "component": "Performance Optimization System",
        "location": "support_systems",
        "status": "active",
        "capabilities": [
            "real_time_monitoring",
            "bottleneck_detection",
            "automatic_optimization",
            "trend_analysis",
            "performance_reporting",
            "resource_management"
        ],
        "optimization_techniques": performance_optimizer.optimization_techniques,
        "instance": performance_optimizer
    }
