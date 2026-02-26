from typing import Optional, List, Dict, Any
from adapters.macos_ax.observer import Snapshot

class AdversarialObserver:
    """Simulates non-deterministic UI behavior for stress testing."""

    def __init__(self):
        self.scenarios: Dict[str, Any] = {}
        self.call_count = 0
        self.current_scenario: Optional[str] = None
        self.params = {}

    def set_scenario(self, name: str, **params):
        self.current_scenario = name
        self.params = params
        self.call_count = 0

    def observe(self) -> Optional[Snapshot]:
        self.call_count += 1

        if self.current_scenario == "sluggish":
            # Requires N calls before returning the target stable hash
            threshold = self.params.get("threshold", 5)

            if self.call_count < threshold:
                return Snapshot(app="Test", role="Window", label=f"loading-{self.call_count}", bbox=(0,0,0,0))
            return Snapshot(app="Test", role="Window", label="stable", bbox=(0,0,0,0))

        if self.current_scenario == "ghost":
            # Changes state unexpectedly after a specific call
            if self.call_count > self.params.get("trigger_at", 2):
                return Snapshot(app="Test", role="Window", label="ghost-mutation", bbox=(0,0,0,0))
            return Snapshot(app="Test", role="Window", label="stable", bbox=(0,0,0,0))

        if self.current_scenario == "stutter":
            # Returns None randomly or periodically
            if self.call_count % self.params.get("period", 3) == 0:
                return None
            return Snapshot(app="Test", role="Window", label="stable", bbox=(0,0,0,0))

        # Default stable behavior
        return Snapshot(app="Test", role="Window", label="stable", bbox=(0,0,0,0))

class MockEventEmitter:
    """Traces emissions without hitting Quartz."""
    def __init__(self):
        self.emissions = []

    def emit(self, event):
        self.emissions.append(event)
        return True
