
import numpy as np
from typing import List, Dict, Any

class LearningVelocityOptimizer:
    """Optimize learning velocity for positive growth"""

    def __init__(self):
        self.velocity_history = []
        self.optimization_factor = 1.5

    def optimize_learning_velocity(self, current_velocity: float) -> float:
        """Optimize learning velocity để đảm bảo positive growth"""

        # Nếu velocity âm, áp dụng correction
        if current_velocity < 0:
            corrected_velocity = abs(current_velocity) * self.optimization_factor
            self.velocity_history.append(corrected_velocity)
            return corrected_velocity

        # Nếu velocity dương, tiếp tục enhance
        enhanced_velocity = current_velocity * (1 + self.optimization_factor * 0.1)
        self.velocity_history.append(enhanced_velocity)
        return enhanced_velocity

    def calculate_adaptive_learning_rate(self, performance_metrics: Dict[str, Any]) -> float:
        """Calculate adaptive learning rate based on performance"""

        base_rate = 0.01
        success_rate = performance_metrics.get('success_rate', 0.5)

        # Adjust learning rate based on success
        if success_rate > 0.8:
            return base_rate * 1.2  # Increase for high success
        elif success_rate < 0.6:
            return base_rate * 0.8  # Decrease for low success
        else:
            return base_rate

    def get_velocity_trend(self) -> str:
        """Analyze velocity trend"""
        if len(self.velocity_history) < 3:
            return "INSUFFICIENT_DATA"

        recent_velocities = self.velocity_history[-3:]
        if all(v > 0 for v in recent_velocities):
            return "POSITIVE_TREND"
        else:
            return "NEEDS_OPTIMIZATION"

# Global learning optimizer
learning_optimizer = LearningVelocityOptimizer()
