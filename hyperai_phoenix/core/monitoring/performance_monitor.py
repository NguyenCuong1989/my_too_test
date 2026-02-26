
import asyncio
import time
import psutil
import json
from datetime import datetime
from typing import Dict, Any

class PerformanceMonitor:
    """Real-time performance monitoring for HyperAI Phoenix"""

    def __init__(self):
        self.monitoring_active = True
        self.performance_history = []
        self.alerts = []

    async def monitor_system_performance(self) -> Dict[str, Any]:
        """Monitor overall system performance"""

        # System metrics
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()

        # Process metrics
        unlimited_process = self.find_unlimited_process()

        performance_data = {
            "timestamp": datetime.now().isoformat(),
            "system": {
                "cpu_percent": cpu_percent,
                "memory_percent": memory.percent,
                "memory_available_gb": memory.available / (1024**3),
                "memory_used_gb": memory.used / (1024**3)
            },
            "unlimited_optimization": {
                "active": unlimited_process is not None,
                "cpu_percent": unlimited_process.cpu_percent() if unlimited_process else 0,
                "memory_mb": unlimited_process.memory_info().rss / (1024**2) if unlimited_process else 0
            },
            "performance_score": self.calculate_performance_score(cpu_percent, memory.percent)
        }

        self.performance_history.append(performance_data)

        # Keep only recent history
        if len(self.performance_history) > 100:
            self.performance_history = self.performance_history[-100:]

        return performance_data

    def find_unlimited_process(self):
        """Find UNLIMITED OPTIMIZATION process"""
        try:
            for process in psutil.process_iter(['pid', 'name', 'cmdline']):
                if 'UNLIMITED_HYPERAI_OPTIMIZATION.py' in ' '.join(process.info['cmdline'] or []):
                    return psutil.Process(process.info['pid'])
        except:
            pass
        return None

    def calculate_performance_score(self, cpu_percent: float, memory_percent: float) -> float:
        """Calculate overall performance score"""
        # Higher CPU usage is good for optimization, but not too high
        cpu_score = min(cpu_percent / 70.0, 1.0) if cpu_percent < 90 else 0.5

        # Lower memory usage is better
        memory_score = max(0.0, 1.0 - (memory_percent / 100.0))

        return (cpu_score + memory_score) / 2.0

    async def generate_performance_report(self) -> Dict[str, Any]:
        """Generate comprehensive performance report"""
        if not self.performance_history:
            return {"error": "No performance data available"}

        recent_data = self.performance_history[-10:]

        avg_cpu = sum(d["system"]["cpu_percent"] for d in recent_data) / len(recent_data)
        avg_memory = sum(d["system"]["memory_percent"] for d in recent_data) / len(recent_data)
        avg_score = sum(d["performance_score"] for d in recent_data) / len(recent_data)

        return {
            "report_time": datetime.now().isoformat(),
            "monitoring_duration_minutes": (time.time() - getattr(self, 'start_time', time.time())) / 60,
            "average_metrics": {
                "cpu_percent": avg_cpu,
                "memory_percent": avg_memory,
                "performance_score": avg_score
            },
            "unlimited_optimization_status": "ACTIVE" if any(d["unlimited_optimization"]["active"] for d in recent_data) else "INACTIVE",
            "performance_trend": "IMPROVING" if avg_score > 0.7 else "STABLE" if avg_score > 0.5 else "NEEDS_OPTIMIZATION"
        }

# Global performance monitor
performance_monitor = PerformanceMonitor()
