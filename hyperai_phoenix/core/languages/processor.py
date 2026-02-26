
import json
import os
from typing import Dict, List, Any

class MultiLanguageProcessor:
    """Multi-language support for HyperAI Phoenix"""

    def __init__(self):
        self.load_language_configs()

    def load_language_configs(self):
        """Load language configurations"""
        config_path = os.path.join(os.path.dirname(__file__), "language_processors.json")
        with open(config_path, 'r', encoding='utf-8') as f:
            self.language_configs = json.load(f)

    def detect_language(self, file_path: str) -> str:
        """Detect programming language from file extension"""
        _, ext = os.path.splitext(file_path)

        for lang, config in self.language_configs.items():
            if ext in config["file_extensions"]:
                return lang

        return "unknown"

    def get_completion_templates(self, language: str) -> List[str]:
        """Get code completion templates for language"""
        return self.language_configs.get(language, {}).get("completion_templates", [])

    def analyze_syntax(self, code: str, language: str) -> Dict[str, Any]:
        """Basic syntax analysis for language"""
        patterns = self.language_configs.get(language, {}).get("syntax_patterns", [])

        analysis = {
            "language": language,
            "patterns_found": [],
            "line_count": len(code.splitlines()),
            "complexity_score": 0
        }

        for pattern in patterns:
            if pattern in code:
                analysis["patterns_found"].append(pattern)

        analysis["complexity_score"] = len(analysis["patterns_found"])
        return analysis

# Global multi-language processor
multi_lang_processor = MultiLanguageProcessor()
