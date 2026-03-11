# \u03a3_AP\u03a9\u2082 CORE MODULE
# Authority: B\u1ed0 C\u01af\u1ed0NG Supreme System Commander
# Creator: alpha_prime_omega (4287)
# Status: CANONICAL

import sys
from pathlib import Path
import google.generativeai as genai

BASE_DIR = Path('/Users/andy/my_too_test')
sys.path.append(str(BASE_DIR / 'autonomous_operator'))
from key_manager import GeminiKeyManager

km = GeminiKeyManager(base_dir=BASE_DIR)
key = km.get_active_key()
genai.configure(api_key=key)

model = genai.GenerativeModel('models/gemini-2.0-flash')
response = model.generate_content('Hello, verify system health.')
print(f"--- FINAL VERIFICATION ---")
print(f"Active Key Index: {km._get_current_index()}")
print(f"Model: {model.model_name}")
print(f"Response: {response.text}")
