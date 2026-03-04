import sys
from pathlib import Path
import google.generativeai as genai

BASE_DIR = Path('/Users/andy/my_too_test')
sys.path.append(str(BASE_DIR / 'autonomous_operator'))
from key_manager import GeminiKeyManager

manager = GeminiKeyManager(base_dir=BASE_DIR)
key = manager.get_active_key()
genai.configure(api_key=key)

print(f"--- FETCHING MODELS WITH KEY: {key[:10]}... ---")
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"Model: {m.name}")
except Exception as e:
    print(f"Error fetching models: {e}")
