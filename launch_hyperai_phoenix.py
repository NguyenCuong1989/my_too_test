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
