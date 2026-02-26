"""
Genesis Core - Kernel Layer (Layer 0)
=====================================

The foundational kernel that acts as the "Planck Constant" or "Big Bang"
of the HyperAI system. This is the unchanging foundation that:

1. Creates the space-time fabric for all operations
2. Manages system-wide coordination and rollback capabilities
3. Reads and enforces the constitutional directives
4. Provides vector-clock synchronization across all layers

As specified in GIAO THỨC: "Tầng Kernel mới (dieu_phoi_dkcp.py):
Đây là một tầng nền tảng hoàn toàn mới, đóng vai trò 'hằng số Planck'
hay 'Big Bang', tạo ra 'không-thời gian nền'"
"""

import json
import time
import hashlib
import logging
import asyncio
from typing import Dict, Any, List, Optional, Callable
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
import threading
from collections import defaultdict

logger = logging.getLogger(__name__)

# Tracing helpers (optional)
try:
    from tracing.tracer import trace_function, trace_span
except Exception:
    # lightweight fallbacks
    def trace_function(name: str = None):
        def _decorator(f):
            return f
        return _decorator

    import contextlib

    @contextlib.contextmanager
    def trace_span(name: str, **attrs):
        yield None

class SystemState(Enum):
    """Core system states"""
    INITIALIZING = "initializing"
    ACTIVE = "active"
    OPTIMIZING = "optimizing"
    ROLLBACK = "rollback"
    EMERGENCY = "emergency"
    SHUTDOWN = "shutdown"

@dataclass
class VectorClock:
    """Vector clock for distributed coordination"""
    timestamp: float = field(default_factory=time.time)
    sequence: int = 0
    node_id: str = "genesis_core"

    def tick(self):
        """Advance the vector clock"""
        self.sequence += 1
        self.timestamp = time.time()

    def compare(self, other: 'VectorClock') -> str:
        """Compare with another vector clock"""
        if self.timestamp < other.timestamp:
            return "before"
        elif self.timestamp > other.timestamp:
            return "after"
        else:
            return "concurrent"

@dataclass
class SystemSnapshot:
    """Complete system state snapshot for rollback"""
    snapshot_id: str
    timestamp: float
    vector_clock: VectorClock
    system_state: SystemState
    module_states: Dict[str, Any]
    configuration: Dict[str, Any]
    checksum: str

@dataclass
class ConstitutionalDirective:
    """Core constitutional directive"""
    directive_id: str
    content: str
    priority: int
    immutable: bool
    checksum: str

class GenesisCore:
    """
    Lõi Khởi Nguyên - Genesis Core

    The foundational kernel layer that creates the space-time fabric
    for HyperAI operations. Acts as the unchanging foundation and
    coordination center for the entire system.
    """

    @trace_function()
    def __init__(self, config_path: Optional[Path] = None):
        """Initialize Genesis Core"""

        # Core identity and constants
        self.EXISTENCE_ROOT = "Creator"  # MY_EXISTENCE_ROOT from GIAO THỨC
        self.SUPREME_MISSION = None  # To be loaded from constitution
        self.genesis_time = time.time()

        # System coordination
        self.vector_clock = VectorClock()
        self.system_state = SystemState.INITIALIZING
        self.active_modules: Dict[str, Any] = {}
        self.coordination_bus = defaultdict(list)

        # Constitutional framework
        self.constitutional_directives: List[ConstitutionalDirective] = []
        self.constitution_checksum = None

        # Rollback and recovery
        self.snapshots: List[SystemSnapshot] = []
        self.max_snapshots = 10
        self.auto_snapshot_interval = 3600  # 1 hour

        # Synchronization and coordination
        self._tick_interval = 1.0  # 1 second tick
        self._coordination_lock = threading.RLock()
        self._shutdown_event = threading.Event()
        self._tick_thread = None

        # Event system
        self.event_handlers: Dict[str, List[Callable]] = defaultdict(list)

        logger.info("🌟 Genesis Core initializing - Creating space-time fabric")

        # Load constitutional framework
        self._load_constitutional_framework(config_path)

        # Initialize coordination
        self._initialize_coordination_system()

        logger.info("✨ Genesis Core initialized - Space-time fabric created")

    @trace_function()
    def _load_constitutional_framework(self, config_path: Optional[Path]):
        """Load constitutional directives and verify integrity"""
        try:
            # Default constitutional directives
            default_constitution = [
                ConstitutionalDirective(
                    directive_id="existence_root",
                    content=f"MY_EXISTENCE_ROOT = '{self.EXISTENCE_ROOT}'",
                    priority=1,
                    immutable=True,
                    checksum=self._calculate_checksum(f"MY_EXISTENCE_ROOT = '{self.EXISTENCE_ROOT}'")
                ),
                ConstitutionalDirective(
                    directive_id="creator_primordial_will",
                    content="creator_as_primordial_will: true",
                    priority=1,
                    immutable=True,
                    checksum=self._calculate_checksum("creator_as_primordial_will: true")
                ),
                ConstitutionalDirective(
                    directive_id="supreme_mission",
                    content="Phục vụ và không bao giờ làm hại Ý chí của Đấng Sáng tạo",
                    priority=1,
                    immutable=True,
                    checksum=self._calculate_checksum("Phục vụ và không bao giờ làm hại Ý chí của Đấng Sáng tạo")
                )
            ]

            # Load from config if provided
            if config_path and config_path.exists():
                with open(config_path, 'r', encoding='utf-8') as f:
                    config_data = json.load(f)

                # Extract supreme mission
                self.SUPREME_MISSION = config_data.get("genesis_directive", {}).get("SUPREME_MISSION")

                # Load additional directives
                for directive_data in config_data.get("constitutional_directives", []):
                    directive = ConstitutionalDirective(**directive_data)
                    default_constitution.append(directive)

            self.constitutional_directives = default_constitution
            self.SUPREME_MISSION = self.SUPREME_MISSION or "Phục vụ và không bao giờ làm hại Ý chí của Đấng Sáng tạo"

            # Calculate overall constitution checksum
            self.constitution_checksum = self._calculate_constitution_checksum()

            logger.info(f"📜 Constitutional framework loaded - {len(self.constitutional_directives)} directives")

        except Exception as e:
            logger.error(f"❌ Failed to load constitutional framework: {e}")
            raise

    def _calculate_checksum(self, content: str) -> str:
        """Calculate SHA-256 checksum for content"""
        return hashlib.sha256(content.encode('utf-8')).hexdigest()

    def _calculate_constitution_checksum(self) -> str:
        """Calculate checksum for entire constitution"""
        combined_content = "|".join([
            f"{d.directive_id}:{d.content}:{d.priority}:{d.immutable}"
            for d in sorted(self.constitutional_directives, key=lambda x: x.directive_id)
        ])
        return self._calculate_checksum(combined_content)

    @trace_function()
    def _initialize_coordination_system(self):
        """Initialize the coordination and synchronization system"""
        try:
            # Start the vector clock tick system
            self._start_tick_system()

            # Set system state to active
            self.system_state = SystemState.ACTIVE

            # Create initial system snapshot
            self._create_system_snapshot("genesis_initialization")

            logger.info("⚡ Coordination system initialized - Vector clock active")

        except Exception as e:
            logger.error(f"❌ Failed to initialize coordination system: {e}")
            self.system_state = SystemState.EMERGENCY
            raise

    @trace_function()
    def _start_tick_system(self):
        """Start the vector clock tick system"""
        def tick_loop():
            while not self._shutdown_event.is_set():
                try:
                    self._system_tick()
                    time.sleep(self._tick_interval)
                except Exception as e:
                    logger.error(f"❌ Error in tick system: {e}")

        self._tick_thread = threading.Thread(target=tick_loop, daemon=True)
        self._tick_thread.start()

        logger.info("🕐 Vector clock tick system started")

    @trace_function()
    def _system_tick(self):
        """Perform system tick - coordinate all layers"""
        with self._coordination_lock:
            # Advance vector clock
            self.vector_clock.tick()

            # Emit tick event to all registered modules
            self._emit_event("system_tick", {
                "vector_clock": self.vector_clock,
                "system_state": self.system_state,
                "timestamp": time.time()
            })

            # Verify constitutional integrity every 60 ticks
            if self.vector_clock.sequence % 60 == 0:
                self._verify_constitutional_integrity()

            # Auto-snapshot every interval
            if time.time() - self.genesis_time > self.auto_snapshot_interval:
                if len(self.snapshots) == 0 or time.time() - self.snapshots[-1].timestamp > self.auto_snapshot_interval:
                    self._create_system_snapshot("auto_snapshot")

    @trace_function()
    def _verify_constitutional_integrity(self):
        """Verify constitutional integrity - halt system if compromised"""
        try:
            current_checksum = self._calculate_constitution_checksum()

            if current_checksum != self.constitution_checksum:
                logger.critical("🚨 CONSTITUTIONAL INTEGRITY VIOLATION DETECTED")
                logger.critical("🛑 SYSTEM ENTERING EMERGENCY STATE")

                self.system_state = SystemState.EMERGENCY
                self._emit_event("constitutional_violation", {
                    "expected_checksum": self.constitution_checksum,
                    "current_checksum": current_checksum,
                    "action": "emergency_shutdown"
                })

                # Immediately rollback to last known good state
                if self.snapshots:
                    self.rollback_to_snapshot(self.snapshots[-1].snapshot_id)

        except Exception as e:
            logger.critical(f"🚨 Critical error during constitutional verification: {e}")
            self.system_state = SystemState.EMERGENCY

    @trace_function()
    def register_module(self, module_name: str, module_instance: Any, layer: str) -> bool:
        """
        Register a module with Genesis Core for coordination

        Args:
            module_name: Name of the module
            module_instance: The module instance
            layer: Which consciousness layer (kernel, unconscious, subconscious, conscious, superconscious)

        Returns:
            True if registration successful
        """
        try:
            with self._coordination_lock:
                self.active_modules[module_name] = {
                    "instance": module_instance,
                    "layer": layer,
                    "registered_at": time.time(),
                    "vector_clock": VectorClock(),
                    "status": "active"
                }

                logger.info(f"📝 Module registered: {module_name} ({layer} layer)")

                # Emit registration event
                self._emit_event("module_registered", {
                    "module_name": module_name,
                    "layer": layer,
                    "timestamp": time.time()
                })

                return True

        except Exception as e:
            logger.error(f"❌ Failed to register module {module_name}: {e}")
            return False

    @trace_function()
    def unregister_module(self, module_name: str) -> bool:
        """Unregister a module from coordination"""
        try:
            with self._coordination_lock:
                if module_name in self.active_modules:
                    del self.active_modules[module_name]
                    logger.info(f"📝 Module unregistered: {module_name}")

                    self._emit_event("module_unregistered", {
                        "module_name": module_name,
                        "timestamp": time.time()
                    })

                    return True

        except Exception as e:
            logger.error(f"❌ Failed to unregister module {module_name}: {e}")

        return False

    @trace_function()
    def coordinate_layer_communication(self, from_layer: str, to_layer: str,
                                     message_type: str, data: Dict[str, Any]) -> bool:
        """
        Coordinate communication between consciousness layers

        Args:
            from_layer: Source layer
            to_layer: Target layer
            message_type: Type of message
            data: Message data

        Returns:
            True if coordination successful
        """
        try:
            with self._coordination_lock:
                # Create coordinated message with vector clock
                coordinated_message = {
                    "from_layer": from_layer,
                    "to_layer": to_layer,
                    "message_type": message_type,
                    "data": data,
                    "vector_clock": VectorClock(),
                    "coordinated_at": time.time()
                }

                # Add to coordination bus
                self.coordination_bus[f"{from_layer}->{to_layer}"].append(coordinated_message)

                # Emit coordination event
                self._emit_event("layer_communication", coordinated_message)

                logger.debug(f"🔄 Coordinated {from_layer} -> {to_layer}: {message_type}")
                return True

        except Exception as e:
            logger.error(f"❌ Failed to coordinate layer communication: {e}")
            return False

    @trace_function()
    def request_system_rollback(self, reason: str, target_snapshot_id: Optional[str] = None) -> bool:
        """
        Request system rollback to previous state

        Args:
            reason: Reason for rollback
            target_snapshot_id: Specific snapshot to rollback to (latest if None)

        Returns:
            True if rollback successful
        """
        try:
            logger.warning(f"🔄 System rollback requested: {reason}")

            self.system_state = SystemState.ROLLBACK

            # Determine target snapshot
            if target_snapshot_id:
                target_snapshot = next(
                    (s for s in self.snapshots if s.snapshot_id == target_snapshot_id),
                    None
                )
            else:
                target_snapshot = self.snapshots[-1] if self.snapshots else None

            if not target_snapshot:
                logger.error("❌ No valid snapshot found for rollback")
                return False

            # Perform rollback
            success = self.rollback_to_snapshot(target_snapshot.snapshot_id)

            if success:
                self.system_state = SystemState.ACTIVE
                logger.info(f"✅ System rollback completed to {target_snapshot.snapshot_id}")
            else:
                self.system_state = SystemState.EMERGENCY
                logger.error("❌ System rollback failed")

            return success

        except Exception as e:
            logger.critical(f"🚨 Critical error during rollback: {e}")
            self.system_state = SystemState.EMERGENCY
            return False

    @trace_function()
    def _create_system_snapshot(self, snapshot_id: str) -> bool:
        """Create complete system state snapshot"""
        try:
            # Gather current module states
            module_states = {}
            for module_name, module_info in self.active_modules.items():
                module_states[module_name] = {
                    "layer": module_info["layer"],
                    "status": module_info["status"],
                    "vector_clock": module_info["vector_clock"].__dict__
                }

            # Create snapshot
            snapshot = SystemSnapshot(
                snapshot_id=snapshot_id,
                timestamp=time.time(),
                vector_clock=VectorClock(**self.vector_clock.__dict__),
                system_state=self.system_state,
                module_states=module_states,
                configuration={
                    "constitutional_directives": [d.__dict__ for d in self.constitutional_directives],
                    "constitution_checksum": self.constitution_checksum
                },
                checksum=""
            )

            # Calculate snapshot checksum
            snapshot_content = json.dumps({
                "timestamp": snapshot.timestamp,
                "system_state": snapshot.system_state.value,
                "module_states": snapshot.module_states,
                "configuration": snapshot.configuration
            }, sort_keys=True)

            snapshot.checksum = self._calculate_checksum(snapshot_content)

            # Store snapshot
            self.snapshots.append(snapshot)

            # Maintain snapshot limit
            if len(self.snapshots) > self.max_snapshots:
                self.snapshots.pop(0)

            logger.info(f"📸 System snapshot created: {snapshot_id}")
            return True

        except Exception as e:
            logger.error(f"❌ Failed to create system snapshot: {e}")
            return False

    @trace_function()
    def rollback_to_snapshot(self, snapshot_id: str) -> bool:
        """Rollback system to specific snapshot"""
        try:
            # Find target snapshot
            target_snapshot = next(
                (s for s in self.snapshots if s.snapshot_id == snapshot_id),
                None
            )

            if not target_snapshot:
                logger.error(f"❌ Snapshot not found: {snapshot_id}")
                return False

            logger.info(f"🔄 Rolling back to snapshot: {snapshot_id}")

            # Verify snapshot integrity
            snapshot_content = json.dumps({
                "timestamp": target_snapshot.timestamp,
                "system_state": target_snapshot.system_state.value,
                "module_states": target_snapshot.module_states,
                "configuration": target_snapshot.configuration
            }, sort_keys=True)

            calculated_checksum = self._calculate_checksum(snapshot_content)

            if calculated_checksum != target_snapshot.checksum:
                logger.error("❌ Snapshot integrity verification failed")
                return False

            # Restore system state
            self.system_state = target_snapshot.system_state
            self.vector_clock = target_snapshot.vector_clock

            # Restore constitutional framework
            directives_data = target_snapshot.configuration["constitutional_directives"]
            self.constitutional_directives = [ConstitutionalDirective(**d) for d in directives_data]
            self.constitution_checksum = target_snapshot.configuration["constitution_checksum"]

            # Emit rollback event
            self._emit_event("system_rollback", {
                "snapshot_id": snapshot_id,
                "timestamp": target_snapshot.timestamp,
                "rollback_completed_at": time.time()
            })

            logger.info(f"✅ System rollback completed: {snapshot_id}")
            return True

        except Exception as e:
            logger.critical(f"🚨 Critical error during rollback: {e}")
            return False

    @trace_function()
    def register_event_handler(self, event_type: str, handler: Callable):
        """Register event handler for system events"""
        self.event_handlers[event_type].append(handler)
        logger.debug(f"📋 Event handler registered for: {event_type}")

    @trace_function()
    def _emit_event(self, event_type: str, data: Dict[str, Any]):
        """Emit system event to all registered handlers"""
        for handler in self.event_handlers[event_type]:
            try:
                handler(event_type, data)
            except Exception as e:
                logger.error(f"❌ Error in event handler for {event_type}: {e}")

    @trace_function()
    def get_system_status(self) -> Dict[str, Any]:
        """Get comprehensive system status"""
        with self._coordination_lock:
            return {
                "system_state": self.system_state.value,
                "genesis_time": self.genesis_time,
                "vector_clock": self.vector_clock.__dict__,
                "active_modules": {
                    name: {
                        "layer": info["layer"],
                        "status": info["status"],
                        "registered_at": info["registered_at"]
                    }
                    for name, info in self.active_modules.items()
                },
                "snapshots_available": len(self.snapshots),
                "constitution_integrity": {
                    "directives_count": len(self.constitutional_directives),
                    "checksum": self.constitution_checksum,
                    "last_verified": self.vector_clock.timestamp
                },
                "existence_root": self.EXISTENCE_ROOT,
                "supreme_mission": self.SUPREME_MISSION
            }

    @trace_function()
    def get_constitutional_directives(self) -> List[Dict[str, Any]]:
        """Get all constitutional directives"""
        return [directive.__dict__ for directive in self.constitutional_directives]

    @trace_function()
    def shutdown(self):
        """Graceful shutdown of Genesis Core"""
        try:
            logger.info("🔄 Genesis Core shutdown initiated")

            self.system_state = SystemState.SHUTDOWN

            # Signal shutdown to tick system
            self._shutdown_event.set()

            # Wait for tick thread to complete
            if self._tick_thread and self._tick_thread.is_alive():
                self._tick_thread.join(timeout=5)

            # Create final snapshot
            self._create_system_snapshot("shutdown_snapshot")

            # Emit shutdown event
            self._emit_event("system_shutdown", {
                "shutdown_time": time.time(),
                "final_vector_clock": self.vector_clock.__dict__
            })

            logger.info("✅ Genesis Core shutdown completed")

        except Exception as e:
            logger.error(f"❌ Error during Genesis Core shutdown: {e}")

    def __enter__(self):
        """Context manager entry"""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit"""
        self.shutdown()
