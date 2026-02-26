"""
Offline Embedding Function for HyperAI Phoenix
Simple TF-IDF based embeddings that work without internet connection
Supports Vietnamese text processing
"""

import numpy as np
import hashlib
import re
from typing import List, Dict, Any
from collections import Counter
import math
import json
import os

class OfflineEmbeddingFunction:
    """
    Simple offline embedding function using TF-IDF for Vietnamese and English text
    """

    def __init__(self):
        self.vocabulary = {}
        self.idf_scores = {}
        self.vocab_size = 0
        self.embedding_dim = 384  # Compatible with sentence transformers

        # Vietnamese stopwords and common words
        self.vietnamese_stopwords = {
            'là', 'của', 'và', 'có', 'trong', 'được', 'với', 'không', 'để', 'một',
            'các', 'này', 'đó', 'cho', 'từ', 'về', 'đã', 'sẽ', 'như', 'trên',
            'khi', 'mà', 'đang', 'đến', 'hay', 'hoặc', 'những', 'nhiều', 'tất',
            'cả', 'theo', 'thì', 'chỉ', 'vào', 'ra', 'lại', 'nếu', 'bởi', 'còn'
        }

        # Load vocabulary if exists
        self._load_vocabulary()

    def _preprocess_text(self, text: str) -> List[str]:
        """Preprocess Vietnamese/English text"""
        # Convert to lowercase
        text = text.lower()

        # Remove special characters but keep Vietnamese diacritics
        text = re.sub(r'[^\w\sáàảãạâấầẩẫậăắằẳẵặéèẻẽẹêếềểễệíìỉĩịóòỏõọôốồổỗộơớờởỡợúùủũụưứừửữựýỳỷỹỵđ]', ' ', text)

        # Tokenize
        words = text.split()

        # Remove stopwords
        words = [word for word in words if word not in self.vietnamese_stopwords and len(word) > 1]

        return words

    def _build_vocabulary(self, documents: List[str]):
        """Build vocabulary from documents"""
        all_words = []
        doc_word_counts = []

        for doc in documents:
            words = self._preprocess_text(doc)
            all_words.extend(words)
            doc_word_counts.append(Counter(words))

        # Build vocabulary
        word_counts = Counter(all_words)
        # Keep words that appear at least twice
        self.vocabulary = {word: idx for idx, (word, count) in enumerate(word_counts.items()) if count >= 2}
        self.vocab_size = len(self.vocabulary)

        # Calculate IDF scores
        num_docs = len(documents)
        for word in self.vocabulary:
            doc_freq = sum(1 for doc_words in doc_word_counts if word in doc_words)
            self.idf_scores[word] = math.log(num_docs / doc_freq)

    def _text_to_vector(self, text: str) -> np.ndarray:
        """Convert text to TF-IDF vector"""
        words = self._preprocess_text(text)
        word_counts = Counter(words)

        # Create sparse vector
        vector = np.zeros(max(384, self.vocab_size))  # Ensure minimum size

        total_words = len(words)
        if total_words == 0:
            return vector

        for word, count in word_counts.items():
            if word in self.vocabulary:
                word_idx = self.vocabulary[word]
                if word_idx < len(vector):
                    tf = count / total_words
                    idf = self.idf_scores.get(word, 1.0)
                    vector[word_idx] = tf * idf

        # Normalize vector
        norm = np.linalg.norm(vector)
        if norm > 0:
            vector = vector / norm

        # Ensure output is exactly 384 dimensions
        if len(vector) > 384:
            vector = vector[:384]
        elif len(vector) < 384:
            padded = np.zeros(384)
            padded[:len(vector)] = vector
            vector = padded

        return vector

    def _save_vocabulary(self):
        """Save vocabulary to file"""
        try:
            vocab_data = {
                'vocabulary': self.vocabulary,
                'idf_scores': self.idf_scores,
                'vocab_size': self.vocab_size
            }
            os.makedirs('hyperai_phoenix/data/databases', exist_ok=True)
            with open('hyperai_phoenix/data/databases/vocabulary.json', 'w', encoding='utf-8') as f:
                json.dump(vocab_data, f, ensure_ascii=False, indent=2)
        except Exception:
            pass  # Fail silently if can't save

    def _load_vocabulary(self):
        """Load vocabulary from file"""
        try:
            with open('hyperai_phoenix/data/databases/vocabulary.json', 'r', encoding='utf-8') as f:
                vocab_data = json.load(f)
                self.vocabulary = vocab_data.get('vocabulary', {})
                self.idf_scores = vocab_data.get('idf_scores', {})
                self.vocab_size = vocab_data.get('vocab_size', 0)
        except Exception:
            pass  # Will build vocabulary on first use

    def name(self) -> str:
        """Return the name of this embedding function (required by ChromaDB)"""
        return "offline_vietnamese_embeddings"

    def __call__(self, input: List[str]) -> List[List[float]]:
        """
        ChromaDB compatible embedding function
        """
        if not input:
            return []

        # If vocabulary is empty, build it from input texts
        if not self.vocabulary:
            self._build_vocabulary(input)
            self._save_vocabulary()

        # Generate embeddings
        embeddings = []
        for text in input:
            vector = self._text_to_vector(text)
            embeddings.append(vector.tolist())

        return embeddings

# Test the embedding function
if __name__ == "__main__":
    embedder = OfflineEmbeddingFunction()

    # Test with Vietnamese text
    test_texts = [
        "HyperAI Phoenix là một hệ thống AI agent tự cải thiện",
        "Triết lý hệ thống: Học để Phục vụ",
        "Dual memory system với SQLite và ChromaDB"
    ]

    embeddings = embedder(test_texts)
    print(f"Generated {len(embeddings)} embeddings, each with {len(embeddings[0])} dimensions")
    print("Offline embedding function working correctly!")
