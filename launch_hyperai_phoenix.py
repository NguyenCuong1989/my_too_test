# \u03a3_AP\u03a9\u2082 CORE MODULE
# Authority: B\u1ed0 C\u01af\u1ed0NG Supreme System Commander
# Creator: alpha_prime_omega (4287)
# Status: CANONICAL

#!/usr/bin/env python3
"""
HyperAI Phoenix Streamlit Launcher
Proper module path setup for Streamlit execution
"""

import sys
import os

# Add the project root to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

# Now we can import the main application
from hyperai_phoenix.app.genesis import HyperAIPhoenixApp, main

if __name__ == "__main__":
    main()
