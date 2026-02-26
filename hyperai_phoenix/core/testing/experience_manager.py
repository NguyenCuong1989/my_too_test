#!/usr/bin/env python3
"""
HyperAI Phoenix - Integrated Experience Manager
==============================================

Manages testing experiences to reduce API calls and improve efficiency,
integrated with HyperAI Phoenix memory system.
"""

import os
import json
import sqlite3
import hashlib
import pickle
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, asdict
import logging

# Import HyperAI Phoenix memory integration
try:
    from ..subconscious.memory_engine import MemoryEngine
    from ..utils.logging_utils import get_logger
except ImportError:
    # Fallback for standalone usage
    pass

@dataclass
class Experience:
    """Represents a learned experience from testing"""
    id: str
    scenario_pattern: str  # Pattern that matches similar scenarios
    input_hash: str        # Hash of input parameters
    successful_response: Dict[str, Any]
    confidence_score: float  # How confident we are in reusing this
    usage_count: int
    last_used: str
    created_at: str
    effectiveness_score: float  # How effective this experience was

@dataclass
class APICallOptimization:
    """Tracks API call optimization strategies"""
    pattern_type: str
    original_calls: int
    optimized_calls: int
    savings_percentage: float
    reuse_frequency: int

class ExperienceManager:
    """Manages learned experiences to optimize future testing, integrated with HyperAI memory"""

    def __init__(self, db_path: str = None):
        # Default path within HyperAI structure or from environment variable
        if db_path is None:
            db_path = os.getenv(
                "HYPERAI_TESTING_DB_PATH",
                os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../data/databases/testing_experience.db"))
            )

        self.db_path = db_path

        # Setup logging
        self.logger = self._setup_logging()

        # HyperAI Phoenix memory integration
        self.memory_engine = None
        try:
            self.memory_engine = MemoryEngine()
            self.logger.info("✅ HyperAI Phoenix memory integration enabled")
        except:
            self.logger.info("⚠️ Running in standalone mode")

        # Ensure directory exists
        os.makedirs(os.path.dirname(db_path), exist_ok=True)

        # Initialize database
        self._init_database()

        # Cache for frequently used experiences
        self.cache = {}
        self.cache_size_limit = 100

        self.logger.info(f"💾 Experience Manager initialized with database: {db_path}")

    def _setup_logging(self) -> logging.Logger:
        """Setup experience manager logging"""
        try:
            return get_logger(f"experience_manager_{id(self)}")
        except:
            logger = logging.getLogger(f"experience_manager_{id(self)}")
            logger.setLevel(logging.INFO)
            return logger

    def _init_database(self):
        """Initialize the experience database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Create experiences table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS experiences (
                id TEXT PRIMARY KEY,
                scenario_pattern TEXT NOT NULL,
                input_hash TEXT NOT NULL,
                successful_response TEXT NOT NULL,
                confidence_score REAL DEFAULT 0.5,
                usage_count INTEGER DEFAULT 0,
                last_used TEXT,
                created_at TEXT NOT NULL,
                effectiveness_score REAL DEFAULT 0.5
            )
        ''')

        # Create API optimization tracking table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS api_optimizations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pattern_type TEXT NOT NULL,
                original_calls INTEGER NOT NULL,
                optimized_calls INTEGER NOT NULL,
                savings_percentage REAL NOT NULL,
                reuse_frequency INTEGER DEFAULT 0,
                created_at TEXT NOT NULL
            )
        ''')

        # Create indexes for faster lookups
        cursor.execute('''
            CREATE INDEX IF NOT EXISTS idx_scenario_pattern
            ON experiences(scenario_pattern)
        ''')

        cursor.execute('''
            CREATE INDEX IF NOT EXISTS idx_input_hash
            ON experiences(input_hash)
        ''')

        conn.commit()
        conn.close()

    def store_experience(self, scenario_pattern: str, input_data: Dict[str, Any],
                        successful_response: Dict[str, Any], confidence_score: float = 0.8) -> str:
        """Store a successful testing experience for future reuse"""

        experience_id = f"exp_{int(datetime.now().timestamp())}_{hashlib.md5(str(input_data).encode()).hexdigest()[:8]}"
        input_hash = hashlib.sha256(json.dumps(input_data, sort_keys=True).encode()).hexdigest()

        experience = Experience(
            id=experience_id,
            scenario_pattern=scenario_pattern,
            input_hash=input_hash,
            successful_response=successful_response,
            confidence_score=confidence_score,
            usage_count=0,
            last_used=datetime.now().isoformat(),
            created_at=datetime.now().isoformat(),
            effectiveness_score=confidence_score
        )

        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            cursor.execute('''
                INSERT INTO experiences
                (id, scenario_pattern, input_hash, successful_response, confidence_score,
                 usage_count, last_used, created_at, effectiveness_score)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                experience.id,
                experience.scenario_pattern,
                experience.input_hash,
                json.dumps(experience.successful_response),
                experience.confidence_score,
                experience.usage_count,
                experience.last_used,
                experience.created_at,
                experience.effectiveness_score
            ))

            conn.commit()
            conn.close()

            # Store in HyperAI memory if available
            if self.memory_engine:
                try:
                    self.memory_engine.store_experience({
                        "type": "testing_experience",
                        "experience_id": experience_id,
                        "scenario_pattern": scenario_pattern,
                        "confidence_score": confidence_score,
                        "timestamp": experience.created_at
                    })
                except:
                    pass

            self.logger.info(f"✅ Stored experience: {experience_id} for pattern: {scenario_pattern}")
            return experience_id

        except Exception as e:
            self.logger.error(f"❌ Failed to store experience: {e}")
            return None

    def find_similar_experience(self, scenario_pattern: str, input_data: Dict[str, Any],
                              min_confidence: float = 0.7) -> Optional[Experience]:
        """Find a similar experience that can be reused"""

        input_hash = hashlib.sha256(json.dumps(input_data, sort_keys=True).encode()).hexdigest()

        # Check cache first
        cache_key = f"{scenario_pattern}_{input_hash}"
        if cache_key in self.cache:
            self.logger.info(f"🔄 Found experience in cache: {cache_key}")
            return self.cache[cache_key]

        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            # Look for exact match first
            cursor.execute('''
                SELECT id, scenario_pattern, input_hash, successful_response, confidence_score,
                       usage_count, last_used, created_at, effectiveness_score
                FROM experiences
                WHERE scenario_pattern = ? AND input_hash = ? AND confidence_score >= ?
                ORDER BY effectiveness_score DESC, usage_count DESC
                LIMIT 1
            ''', (scenario_pattern, input_hash, min_confidence))

            result = cursor.fetchone()

            if not result:
                # Look for pattern match
                cursor.execute('''
                    SELECT id, scenario_pattern, input_hash, successful_response, confidence_score,
                           usage_count, last_used, created_at, effectiveness_score
                    FROM experiences
                    WHERE scenario_pattern = ? AND confidence_score >= ?
                    ORDER BY effectiveness_score DESC, usage_count DESC
                    LIMIT 1
                ''', (scenario_pattern, min_confidence))

                result = cursor.fetchone()

            conn.close()

            if result:
                experience = Experience(
                    id=result[0],
                    scenario_pattern=result[1],
                    input_hash=result[2],
                    successful_response=json.loads(result[3]),
                    confidence_score=result[4],
                    usage_count=result[5],
                    last_used=result[6],
                    created_at=result[7],
                    effectiveness_score=result[8]
                )

                # Update cache
                if len(self.cache) < self.cache_size_limit:
                    self.cache[cache_key] = experience

                self.logger.info(f"🔄 Found similar experience: {experience.id} (confidence: {experience.confidence_score:.2f})")
                return experience

            return None

        except Exception as e:
            self.logger.error(f"❌ Failed to find similar experience: {e}")
            return None

    def update_experience_usage(self, experience_id: str, effectiveness_score: float = None):
        """Update experience usage statistics"""

        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            update_fields = ["usage_count = usage_count + 1", "last_used = ?"]
            params = [datetime.now().isoformat()]

            if effectiveness_score is not None:
                update_fields.append("effectiveness_score = ?")
                params.append(effectiveness_score)

            params.append(experience_id)

            cursor.execute(f'''
                UPDATE experiences
                SET {", ".join(update_fields)}
                WHERE id = ?
            ''', params)

            conn.commit()
            conn.close()

            self.logger.info(f"📊 Updated usage for experience: {experience_id}")

        except Exception as e:
            self.logger.error(f"❌ Failed to update experience usage: {e}")

    def get_reuse_statistics(self) -> Dict[str, Any]:
        """Get statistics about experience reuse"""

        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            # Total experiences
            cursor.execute("SELECT COUNT(*) FROM experiences")
            total_experiences = cursor.fetchone()[0]

            # Used experiences (usage_count > 0)
            cursor.execute("SELECT COUNT(*) FROM experiences WHERE usage_count > 0")
            used_experiences = cursor.fetchone()[0]

            # Total reuses
            cursor.execute("SELECT SUM(usage_count) FROM experiences")
            total_reuses = cursor.fetchone()[0] or 0

            # Average effectiveness
            cursor.execute("SELECT AVG(effectiveness_score) FROM experiences")
            avg_effectiveness = cursor.fetchone()[0] or 0

            # API savings (mock calculation)
            estimated_api_savings = total_reuses * 2  # Assume 2 API calls saved per reuse

            conn.close()

            reuse_rate = (used_experiences / total_experiences * 100) if total_experiences > 0 else 0

            return {
                "total_experiences": total_experiences,
                "used_experiences": used_experiences,
                "total_reuses": total_reuses,
                "reuse_rate": reuse_rate,
                "average_effectiveness": avg_effectiveness,
                "estimated_api_savings": estimated_api_savings,
                "api_savings_percentage": min(reuse_rate * 0.3, 30)  # Cap at 30%
            }

        except Exception as e:
            self.logger.error(f"❌ Failed to get reuse statistics: {e}")
            return {
                "total_experiences": 0,
                "used_experiences": 0,
                "total_reuses": 0,
                "reuse_rate": 0,
                "average_effectiveness": 0,
                "estimated_api_savings": 0,
                "api_savings_percentage": 0
            }

    def cleanup_old_experiences(self, days_old: int = 30) -> int:
        """Clean up old, unused experiences"""

        cutoff_date = (datetime.now() - timedelta(days=days_old)).isoformat()

        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            # Delete old, unused experiences
            cursor.execute('''
                DELETE FROM experiences
                WHERE created_at < ? AND usage_count = 0
            ''', (cutoff_date,))

            deleted_count = cursor.rowcount
            conn.commit()
            conn.close()

            self.logger.info(f"🧹 Cleaned up {deleted_count} old experiences")

            # Clear cache
            self.cache.clear()

            return deleted_count

        except Exception as e:
            self.logger.error(f"❌ Failed to cleanup old experiences: {e}")
            return 0

    def record_api_optimization(self, pattern_type: str, original_calls: int,
                              optimized_calls: int):
        """Record API call optimization for analysis"""

        savings_percentage = ((original_calls - optimized_calls) / original_calls * 100) if original_calls > 0 else 0

        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            cursor.execute('''
                INSERT INTO api_optimizations
                (pattern_type, original_calls, optimized_calls, savings_percentage, created_at)
                VALUES (?, ?, ?, ?, ?)
            ''', (
                pattern_type,
                original_calls,
                optimized_calls,
                savings_percentage,
                datetime.now().isoformat()
            ))

            conn.commit()
            conn.close()

            self.logger.info(f"📈 Recorded API optimization: {savings_percentage:.1f}% savings for {pattern_type}")

        except Exception as e:
            self.logger.error(f"❌ Failed to record API optimization: {e}")

if __name__ == "__main__":
    # Example usage
    manager = ExperienceManager()

    print("💾 HyperAI Phoenix - Experience Manager Test")
    print("=" * 50)

    # Test storing an experience
    exp_id = manager.store_experience(
        "file_operations",
        {"file_name": "test.txt", "operation": "read"},
        {"status": "success", "content": "file content", "size": 1024},
        0.9
    )

    if exp_id:
        print(f"✅ Stored experience: {exp_id}")

        # Test finding similar experience
        found = manager.find_similar_experience(
            "file_operations",
            {"file_name": "test.txt", "operation": "read"},
            0.8
        )

        if found:
            print(f"🔄 Found experience: {found.id} (confidence: {found.confidence_score})")
            manager.update_experience_usage(found.id, 0.95)

        # Get statistics
        stats = manager.get_reuse_statistics()
        print(f"📊 Statistics: {stats['total_experiences']} experiences, {stats['reuse_rate']:.1f}% reuse rate")
