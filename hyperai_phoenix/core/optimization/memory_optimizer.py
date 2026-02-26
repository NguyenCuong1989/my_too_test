
import gc
import sys
from typing import Dict, Any

class MemoryOptimizer:
    """Advanced memory optimization for HyperAI Phoenix"""

    def __init__(self):
        self.optimization_active = True

    def optimize_memory(self) -> Dict[str, Any]:
        """Tối ưu memory usage"""
        initial_usage = self.get_memory_usage()

        # Force garbage collection
        gc.collect()

        # Clear unnecessary caches
        sys.modules.clear()

        # Optimize object references
        self._optimize_object_references()

        final_usage = self.get_memory_usage()
        improvement = initial_usage - final_usage

        return {
            "initial_usage": initial_usage,
            "final_usage": final_usage,
            "improvement": improvement,
            "efficiency_percent": (improvement / initial_usage) * 100 if initial_usage > 0 else 0
        }

    def get_memory_usage(self) -> int:
        """Get current memory usage"""
        import psutil
        process = psutil.Process()
        return process.memory_info().rss / 1024 / 1024  # MB

    def _optimize_object_references(self):
        """Optimize object references"""
        # Clean up circular references
        gc.set_threshold(700, 10, 10)
        collected = gc.collect()
        return collected

# Global memory optimizer instance
memory_optimizer = MemoryOptimizer()
