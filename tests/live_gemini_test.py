import sys
import os
import time
from pathlib import Path
import google.generativeai as genai

# Thêm đường dẫn để import KeyManager
BASE_DIR = Path('/Users/andy/my_too_test')
sys.path.append(str(BASE_DIR / 'autonomous_operator'))
from key_manager import GeminiKeyManager

def live_test():
    manager = GeminiKeyManager(base_dir=BASE_DIR)

    print('--- STARTING LIVE EMPIRICAL TEST ---')

    # 1. Key 1 (Index hiện tại)
    idx1 = manager._get_current_index()
    key1 = manager.get_active_key()
    print(f'TIMESTAMP: {time.ctime()}')
    print(f'Attempting with Key Index {idx1} (Partial: {key1[:10]}...)')

    try:
        genai.configure(api_key=key1)
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content('HELLO')
        print(f'API RESPONSE 1: {response.text}')
    except Exception as e:
        print(f'API ERROR (KEY {idx1}): {e}')

    # 2. Xoay Key (Index + 1)
    print('\n--- PERFORMING AUTONOMOUS ROTATION ---')
    manager.rotate_key()

    # 3. Key 2 (Index tiếp theo)
    idx2 = manager._get_current_index()
    key2 = manager.get_active_key()
    print(f'TIMESTAMP: {time.ctime()}')
    print(f'Attempting with Key Index {idx2} (Partial: {key2[:10]}...)')

    try:
        genai.configure(api_key=key2)
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content('HELLO')
        print(f'API RESPONSE 2: {response.text}')
    except Exception as e:
        print(f'API ERROR (KEY {idx2}): {e}')

if __name__ == '__main__':
    live_test()
