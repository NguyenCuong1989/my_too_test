"""
HyperAI Phoenix - System Observer
Real-time monitoring of system resources and performance
"""

import psutil
import threading
import time
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Callable
from dataclasses import dataclass, asdict
import json
import logging

@dataclass
class SystemMetrics:
    """System resource metrics snapshot"""
    timestamp: datetime
    cpu_percent: float
    memory_percent: float
    memory_used_mb: float
    memory_available_mb: float
    disk_usage_percent: float
    network_sent_mb: float
    network_recv_mb: float
    process_count: int
    uptime_seconds: float

@dataclass
class PerformanceAlert:
    """Performance alert when thresholds are exceeded"""
    metric_name: str
    current_value: float
    threshold: float
    severity: str  # low, medium, high, critical
    message: str
    timestamp: datetime
    suggested_action: str

class SystemObserver:
    """Real-time system monitoring and alerting"""

    def __init__(self, observation_interval: float = 5.0):
        self.observation_interval = observation_interval
        self.logger = logging.getLogger(__name__)

        # Monitoring control
        self.running = False
        self.monitor_thread = None

        # Metrics storage
        self.metrics_history = []
        self.max_history_size = 720  # 1 hour at 5-second intervals

        # Alert thresholds
        self.thresholds = {
            'cpu_percent': {'warning': 70.0, 'critical': 85.0},
            'memory_percent': {'warning': 75.0, 'critical': 90.0},
            'disk_usage_percent': {'warning': 80.0, 'critical': 95.0},
            'process_count': {'warning': 200, 'critical': 400}
        }

        # Alert callbacks
        self.alert_callbacks = []

        # Performance tracking
        self.startup_time = datetime.now()
        self.last_network_stats = None

        # Process info (for HyperAI Phoenix specifically)
        self.target_process = None
        try:
            current_process = psutil.Process()
            cmdline = current_process.cmdline()
            if len(cmdline) > 0 and ('hyperai_phoenix' in cmdline[0].lower() or
                                   any('genesis.py' in arg for arg in cmdline)):
                self.target_process = current_process
        except psutil.NoSuchProcess:
            pass

    def add_alert_callback(self, callback: Callable[[PerformanceAlert], None]):
        """Add callback function for performance alerts"""
        self.alert_callbacks.append(callback)

    def start_monitoring(self):
        """Start continuous system monitoring"""
        if self.running:
            return

        self.running = True
        self.monitor_thread = threading.Thread(target=self._monitor_loop, daemon=True)
        self.monitor_thread.start()

        self.logger.info("System monitoring started")

    def stop_monitoring(self):
        """Stop system monitoring"""
        self.running = False

        if self.monitor_thread and self.monitor_thread.is_alive():
            self.monitor_thread.join(timeout=10)

        self.logger.info("System monitoring stopped")

    def _monitor_loop(self):
        """Main monitoring loop"""
        while self.running:
            try:
                # Collect current metrics
                metrics = self._collect_metrics()

                # Store in history
                self.metrics_history.append(metrics)

                # Trim history if too long
                if len(self.metrics_history) > self.max_history_size:
                    self.metrics_history = self.metrics_history[-self.max_history_size:]

                # Check for alerts
                alerts = self._check_alerts(metrics)

                # Trigger alert callbacks
                for alert in alerts:
                    for callback in self.alert_callbacks:
                        try:
                            callback(alert)
                        except Exception as e:
                            self.logger.error(f"Alert callback failed: {e}")

                time.sleep(self.observation_interval)

            except Exception as e:
                self.logger.error(f"Monitoring loop error: {e}")
                time.sleep(5.0)  # Wait longer on error

    def _collect_metrics(self) -> SystemMetrics:
        """Collect current system metrics"""
        # CPU and Memory
        cpu_percent = psutil.cpu_percent(interval=0.1)
        memory = psutil.virtual_memory()

        # Disk usage
        disk = psutil.disk_usage('/')
        disk_usage_percent = disk.used / disk.total * 100

        # Network I/O
        network = psutil.net_io_counters()
        network_sent_mb = network.bytes_sent / (1024 * 1024)
        network_recv_mb = network.bytes_recv / (1024 * 1024)

        # Process count
        process_count = len(psutil.pids())

        # Uptime
        uptime_seconds = (datetime.now() - self.startup_time).total_seconds()

        return SystemMetrics(
            timestamp=datetime.now(),
            cpu_percent=cpu_percent,
            memory_percent=memory.percent,
            memory_used_mb=memory.used / (1024 * 1024),
            memory_available_mb=memory.available / (1024 * 1024),
            disk_usage_percent=disk_usage_percent,
            network_sent_mb=network_sent_mb,
            network_recv_mb=network_recv_mb,
            process_count=process_count,
            uptime_seconds=uptime_seconds
        )

    def _check_alerts(self, metrics: SystemMetrics) -> List[PerformanceAlert]:
        """Check metrics against thresholds and generate alerts"""
        alerts = []

        # CPU check
        cpu_thresholds = self.thresholds['cpu_percent']
        if metrics.cpu_percent >= cpu_thresholds['critical']:
            alerts.append(PerformanceAlert(
                metric_name='cpu_percent',
                current_value=metrics.cpu_percent,
                threshold=cpu_thresholds['critical'],
                severity='critical',
                message=f'CPU sử dụng quá cao: {metrics.cpu_percent:.1f}%',
                timestamp=metrics.timestamp,
                suggested_action='Kiểm tra các tiến trình đang chạy và tối ưu hóa'
            ))
        elif metrics.cpu_percent >= cpu_thresholds['warning']:
            alerts.append(PerformanceAlert(
                metric_name='cpu_percent',
                current_value=metrics.cpu_percent,
                threshold=cpu_thresholds['warning'],
                severity='warning',
                message=f'CPU sử dụng cao: {metrics.cpu_percent:.1f}%',
                timestamp=metrics.timestamp,
                suggested_action='Theo dõi các tác vụ đang chạy'
            ))

        # Memory check
        memory_thresholds = self.thresholds['memory_percent']
        if metrics.memory_percent >= memory_thresholds['critical']:
            alerts.append(PerformanceAlert(
                metric_name='memory_percent',
                current_value=metrics.memory_percent,
                threshold=memory_thresholds['critical'],
                severity='critical',
                message=f'Bộ nhớ sử dụng quá cao: {metrics.memory_percent:.1f}%',
                timestamp=metrics.timestamp,
                suggested_action='Dọn dẹp bộ nhớ và giảm tải hệ thống'
            ))
        elif metrics.memory_percent >= memory_thresholds['warning']:
            alerts.append(PerformanceAlert(
                metric_name='memory_percent',
                current_value=metrics.memory_percent,
                threshold=memory_thresholds['warning'],
                severity='warning',
                message=f'Bộ nhớ sử dụng cao: {metrics.memory_percent:.1f}%',
                timestamp=metrics.timestamp,
                suggested_action='Theo dõi việc sử dụng bộ nhớ'
            ))

        # Disk check
        disk_thresholds = self.thresholds['disk_usage_percent']
        if metrics.disk_usage_percent >= disk_thresholds['critical']:
            alerts.append(PerformanceAlert(
                metric_name='disk_usage_percent',
                current_value=metrics.disk_usage_percent,
                threshold=disk_thresholds['critical'],
                severity='critical',
                message=f'Ổ đĩa gần đầy: {metrics.disk_usage_percent:.1f}%',
                timestamp=metrics.timestamp,
                suggested_action='Dọn dẹp ổ đĩa ngay lập tức'
            ))
        elif metrics.disk_usage_percent >= disk_thresholds['warning']:
            alerts.append(PerformanceAlert(
                metric_name='disk_usage_percent',
                current_value=metrics.disk_usage_percent,
                threshold=disk_thresholds['warning'],
                severity='warning',
                message=f'Ổ đĩa sử dụng cao: {metrics.disk_usage_percent:.1f}%',
                timestamp=metrics.timestamp,
                suggested_action='Lên kế hoạch dọn dẹp ổ đĩa'
            ))

        return alerts

    def get_current_metrics(self) -> Optional[SystemMetrics]:
        """Get the most recent metrics"""
        if not self.metrics_history:
            return self._collect_metrics()
        return self.metrics_history[-1]

    def get_metrics_history(self, minutes: int = 60) -> List[SystemMetrics]:
        """Get metrics history for specified time period"""
        cutoff_time = datetime.now() - timedelta(minutes=minutes)

        return [m for m in self.metrics_history if m.timestamp >= cutoff_time]

    def get_average_metrics(self, minutes: int = 10) -> Optional[Dict[str, float]]:
        """Get average metrics over specified time period"""
        history = self.get_metrics_history(minutes)

        if not history:
            return None

        total_metrics = {
            'cpu_percent': 0.0,
            'memory_percent': 0.0,
            'memory_used_mb': 0.0,
            'disk_usage_percent': 0.0,
            'process_count': 0
        }

        for metrics in history:
            total_metrics['cpu_percent'] += metrics.cpu_percent
            total_metrics['memory_percent'] += metrics.memory_percent
            total_metrics['memory_used_mb'] += metrics.memory_used_mb
            total_metrics['disk_usage_percent'] += metrics.disk_usage_percent
            total_metrics['process_count'] += metrics.process_count

        count = len(history)
        avg_metrics = {k: v / count for k, v in total_metrics.items()}

        return avg_metrics

    def get_peak_metrics(self, minutes: int = 60) -> Optional[Dict[str, float]]:
        """Get peak metrics over specified time period"""
        history = self.get_metrics_history(minutes)

        if not history:
            return None

        peak_metrics = {
            'cpu_percent': max(m.cpu_percent for m in history),
            'memory_percent': max(m.memory_percent for m in history),
            'memory_used_mb': max(m.memory_used_mb for m in history),
            'disk_usage_percent': max(m.disk_usage_percent for m in history),
            'process_count': max(m.process_count for m in history)
        }

        return peak_metrics

    def get_system_health_score(self) -> float:
        """Calculate overall system health score (0-1)"""
        current_metrics = self.get_current_metrics()
        if not current_metrics:
            return 0.5

        # Calculate health based on resource usage
        cpu_health = max(0, 1 - (current_metrics.cpu_percent / 100))
        memory_health = max(0, 1 - (current_metrics.memory_percent / 100))
        disk_health = max(0, 1 - (current_metrics.disk_usage_percent / 100))

        # Weighted average (memory is most critical for AI workloads)
        health_score = (cpu_health * 0.3 + memory_health * 0.5 + disk_health * 0.2)

        return health_score

    def get_process_specific_metrics(self) -> Optional[Dict[str, Any]]:
        """Get metrics specific to the HyperAI Phoenix process"""
        if not self.target_process:
            return None

        try:
            with self.target_process.oneshot():
                process_metrics = {
                    'pid': self.target_process.pid,
                    'cpu_percent': self.target_process.cpu_percent(),
                    'memory_percent': self.target_process.memory_percent(),
                    'memory_info_mb': {
                        'rss': self.target_process.memory_info().rss / (1024 * 1024),
                        'vms': self.target_process.memory_info().vms / (1024 * 1024)
                    },
                    'num_threads': self.target_process.num_threads(),
                    'connections': len(self.target_process.connections()),
                    'create_time': datetime.fromtimestamp(self.target_process.create_time()).isoformat(),
                    'status': self.target_process.status()
                }

            return process_metrics

        except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
            self.logger.warning(f"Could not get process metrics: {e}")
            return None

    def export_metrics(self, filepath: str, minutes: int = 60):
        """Export metrics history to JSON file"""
        history = self.get_metrics_history(minutes)

        export_data = {
            'export_timestamp': datetime.now().isoformat(),
            'time_range_minutes': minutes,
            'metrics_count': len(history),
            'metrics': [asdict(m) for m in history]
        }

        # Convert datetime objects to ISO strings
        for metrics in export_data['metrics']:
            metrics['timestamp'] = metrics['timestamp'].isoformat()

        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(export_data, f, ensure_ascii=False, indent=2)

            self.logger.info(f"Metrics exported to {filepath}")
        except Exception as e:
            self.logger.error(f"Failed to export metrics: {e}")

    def create_performance_report(self, hours: int = 24) -> Dict[str, Any]:
        """Create comprehensive performance report"""
        history = self.get_metrics_history(hours * 60)

        if not history:
            return {
                'report_time': datetime.now().isoformat(),
                'time_range_hours': hours,
                'status': 'no_data',
                'message': 'Không có dữ liệu để tạo báo cáo'
            }

        # Calculate statistics
        cpu_values = [m.cpu_percent for m in history]
        memory_values = [m.memory_percent for m in history]

        report = {
            'report_time': datetime.now().isoformat(),
            'time_range_hours': hours,
            'data_points': len(history),
            'system_health_score': self.get_system_health_score(),
            'cpu_stats': {
                'average': sum(cpu_values) / len(cpu_values),
                'peak': max(cpu_values),
                'minimum': min(cpu_values),
                'p95': sorted(cpu_values)[int(len(cpu_values) * 0.95)]
            },
            'memory_stats': {
                'average': sum(memory_values) / len(memory_values),
                'peak': max(memory_values),
                'minimum': min(memory_values),
                'p95': sorted(memory_values)[int(len(memory_values) * 0.95)]
            },
            'disk_usage': history[-1].disk_usage_percent if history else 0,
            'uptime_hours': history[-1].uptime_seconds / 3600 if history else 0,
            'process_metrics': self.get_process_specific_metrics(),
            'recommendations': self._generate_recommendations(history)
        }

        return report

    def _generate_recommendations(self, history: List[SystemMetrics]) -> List[str]:
        """Generate performance recommendations based on metrics"""
        recommendations = []

        if not history:
            return recommendations

        # CPU analysis
        cpu_values = [m.cpu_percent for m in history]
        avg_cpu = sum(cpu_values) / len(cpu_values)

        if avg_cpu > 70:
            recommendations.append("CPU sử dụng cao - cân nhắc tối ưu hóa thuật toán hoặc nâng cấp phần cứng")
        elif avg_cpu < 20:
            recommendations.append("CPU sử dụng thấp - có thể tăng concurrency hoặc batch size")

        # Memory analysis
        memory_values = [m.memory_percent for m in history]
        avg_memory = sum(memory_values) / len(memory_values)

        if avg_memory > 75:
            recommendations.append("Bộ nhớ sử dụng cao - thực hiện memory compaction thường xuyên hơn")
        if max(memory_values) > 90:
            recommendations.append("Có spike bộ nhớ - kiểm tra memory leaks")

        # Disk analysis
        latest_disk = history[-1].disk_usage_percent
        if latest_disk > 80:
            recommendations.append("Dung lượng đĩa thấp - dọn dẹp logs và cold storage")

        # Stability analysis
        cpu_variance = max(cpu_values) - min(cpu_values)
        if cpu_variance > 50:
            recommendations.append("CPU không ổn định - kiểm tra workload balancing")

        if not recommendations:
            recommendations.append("Hệ thống hoạt động ổn định")

        return recommendations

# Global observer instance
observer = SystemObserver()

if __name__ == "__main__":
    # Test the system observer
    def alert_handler(alert: PerformanceAlert):
        print(f"ALERT [{alert.severity}]: {alert.message}")
        print(f"Suggested action: {alert.suggested_action}")

    observer.add_alert_callback(alert_handler)
    observer.start_monitoring()

    try:
        # Let it run for a bit
        time.sleep(30)

        # Get current metrics
        current = observer.get_current_metrics()
        if current:
            print(f"Current CPU: {current.cpu_percent:.1f}%")
            print(f"Current Memory: {current.memory_percent:.1f}%")

        # Get health score
        health = observer.get_system_health_score()
        print(f"System health score: {health:.2f}")

        # Create report
        report = observer.create_performance_report(hours=1)
        print(f"Performance report: {report['cpu_stats']['average']:.1f}% avg CPU")

    finally:
        observer.stop_monitoring()
