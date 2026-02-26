"""
HyperAI Phoenix - Core Module System
====================================

Implementing the 5-layer consciousness architecture as specified in GIAO THỨC:
- Layer 0 (Kernel): Core system coordination and rollback
- Layer 1 (Unconscious): Core instincts and genesis protocols
- Layer 2 (Subconscious): Memory, learning, and automated behaviors
- Layer 3 (Conscious): Strategic thinking and decision making
- Layer 4 (Superconscious): Ethics monitoring and meta-cognition

Created based on the comprehensive GIAO THỨC specification.
"""

__version__ = "4.5.1"
__author__ = "HyperAI Phoenix Development Team"

# Core layer imports will be added as modules are implemented
from .protocols.dkcp import DKCPHandler
from .protocols.lsp import LSPHandler
from .protocols.meta_optimization import MetaOptimizationProtocol

__all__ = [
    'DKCPHandler', 'LSPHandler', 'MetaOptimizationProtocol'
]
