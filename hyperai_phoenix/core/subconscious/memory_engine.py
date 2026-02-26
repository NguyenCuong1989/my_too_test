"""
Memory Engine - Subconscious Layer
==================================

Advanced memory management system using ChromaDB for vector storage and retrieval.
Implements the "Hầm di sản của kiến chúa" (Legacy Vault of the Queen) as specified
in GIAO THỨC.

Features:
- Long-term memory storage with ChromaDB
- Post-mortem analysis and hypothesis generation
- Experience prioritization and survival weighting
- Bootstrap memory logging
- RAG (Retrieval-Augmented Generation) capabilities
- Dynamic knowledge organization and retrieval
"""

import json
import time
import logging
import hashlib
import sqlite3
from typing import Dict, Any, List, Optional, Tuple
from dataclasses import dataclass, field
from pathlib import Path
import asyncio
from datetime import datetime, timedelta

try:
    import chromadb
    from chromadb.config import Settings
    CHROMADB_AVAILABLE = True
except ImportError:
    CHROMADB_AVAILABLE = False
    chromadb = None

try:
    from sentence_transformers import SentenceTransformer
    SENTENCE_TRANSFORMERS_AVAILABLE = True
except ImportError:
    SENTENCE_TRANSFORMERS_AVAILABLE = False
    SentenceTransformer = None

logger = logging.getLogger(__name__)

# Optional tracing helpers (no-op fallback if tracing not installed)
try:
    from tracing.tracer import trace_function, trace_span
except Exception:
    def trace_function(name: str = None):
        def _decorator(f):
            return f
        return _decorator

    import contextlib

    @contextlib.contextmanager
    def trace_span(name: str, **attrs):
        yield None

@dataclass
class MemoryEntry:
    """Individual memory entry"""
    memory_id: str
    content: str
    content_type: str  # 'lesson', 'experience', 'hypothesis', 'post_mortem'
    metadata: Dict[str, Any]
    survival_weight: float  # Importance for system survival
    created_at: float = field(default_factory=time.time)
    accessed_count: int = 0
    last_accessed: float = field(default_factory=time.time)

@dataclass
class PostMortemEntry:
    """Post-mortem analysis entry"""
    incident_id: str
    incident_description: str
    primary_hypothesis: str
    contributing_factors: List[str]
    lessons_learned: List[str]
    prevention_strategies: List[str]
    created_at: float = field(default_factory=time.time)

@dataclass
class ExperiencePattern:
    """Recognized experience pattern"""
    pattern_id: str
    pattern_type: str
    frequency: int
    success_rate: float
    context_conditions: List[str]
    outcomes: List[str]

class MemoryEngine:
    """
    Bộ nhớ dài hạn - Advanced Memory Engine

    Implements ChromaDB-based vector storage for long-term memory management,
    experience analysis, and knowledge retrieval as specified in GIAO THỨC.
    """

    @trace_function()
    def __init__(self, storage_path: Path = None,
                 embedding_model: str = "all-MiniLM-L6-v2"):
        """Initialize Memory Engine"""

        # Storage configuration
        self.storage_path = storage_path or Path("hyperai_phoenix/data/memory")
        self.storage_path.mkdir(parents=True, exist_ok=True)

        # Initialize ChromaDB if available
        self.chroma_client = None
        self.collection = None
        self.embedding_model = None

        if CHROMADB_AVAILABLE:
            self._initialize_chromadb()
        else:
            logger.warning("⚠️ ChromaDB not available - using fallback storage")

        # Initialize embedding model if available
        if SENTENCE_TRANSFORMERS_AVAILABLE:
            try:
                self.embedding_model = SentenceTransformer(embedding_model)
                logger.info(f"🧠 Embedding model loaded: {embedding_model}")
            except Exception as e:
                logger.warning(f"⚠️ Failed to load embedding model: {e}")

        # SQLite fallback for metadata and relationships
        self.sqlite_path = self.storage_path / "memory_metadata.db"
        self._initialize_sqlite()

        # Memory statistics
        self.memory_stats = {
            "total_memories": 0,
            "lessons_learned": 0,
            "experiences_stored": 0,
            "post_mortems": 0,
            "bootstrap_logs": 0
        }

        # Experience patterns cache
        self.experience_patterns: Dict[str, ExperiencePattern] = {}

        logger.info("🧠 Memory Engine initialized - Long-term storage active")

    @trace_function()
    def _initialize_chromadb(self):
        """Initialize ChromaDB vector storage"""
        try:
            # Create ChromaDB client
            chroma_settings = Settings(
                chroma_db_impl="duckdb+parquet",
                persist_directory=str(self.storage_path / "chroma_db")
            )

            self.chroma_client = chromadb.Client(chroma_settings)

            # Get or create main collection
            try:
                self.collection = self.chroma_client.get_collection("hyperai_memory")
            except:
                self.collection = self.chroma_client.create_collection(
                    name="hyperai_memory",
                    metadata={"description": "HyperAI long-term memory storage"}
                )

            logger.info("🗄️ ChromaDB initialized successfully")

        except Exception as e:
            logger.error(f"❌ Failed to initialize ChromaDB: {e}")
            self.chroma_client = None
            self.collection = None

    @trace_function()
    def _initialize_sqlite(self):
        """Initialize SQLite database for metadata"""
        try:
            conn = sqlite3.connect(self.sqlite_path)
            cursor = conn.cursor()

            # Create tables
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS memory_entries (
                    memory_id TEXT PRIMARY KEY,
                    content_type TEXT,
                    survival_weight REAL,
                    created_at REAL,
                    accessed_count INTEGER,
                    last_accessed REAL,
                    metadata TEXT
                )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS post_mortems (
                    incident_id TEXT PRIMARY KEY,
                    incident_description TEXT,
                    primary_hypothesis TEXT,
                    contributing_factors TEXT,
                    lessons_learned TEXT,
                    prevention_strategies TEXT,
                    created_at REAL
                )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS experience_patterns (
                    pattern_id TEXT PRIMARY KEY,
                    pattern_type TEXT,
                    frequency INTEGER,
                    success_rate REAL,
                    context_conditions TEXT,
                    outcomes TEXT,
                    last_updated REAL
                )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS bootstrap_logs (
                    log_id TEXT PRIMARY KEY,
                    event_type TEXT,
                    content TEXT,
                    timestamp REAL,
                    genesis_session TEXT
                )
            """)

            conn.commit()
            conn.close()

            logger.info("📊 SQLite metadata storage initialized")

        except Exception as e:
            logger.error(f"❌ Failed to initialize SQLite: {e}")
            raise

    @trace_function()
    async def store_memory(self, content: str, content_type: str,
                          metadata: Dict[str, Any] = None,
                          survival_weight: float = 0.5) -> str:
        """
        Store a new memory entry

        Args:
            content: Memory content
            content_type: Type of memory ('lesson', 'experience', 'hypothesis', etc.)
            metadata: Additional metadata
            survival_weight: Importance for system survival (0.0 to 1.0)

        Returns:
            Memory ID
        """
        try:
            # Generate memory ID
            memory_id = hashlib.sha256(
                f"{content}_{content_type}_{time.time()}".encode()
            ).hexdigest()[:16]

            # Create memory entry
            memory_entry = MemoryEntry(
                memory_id=memory_id,
                content=content,
                content_type=content_type,
                metadata=metadata or {},
                survival_weight=survival_weight
            )

            # Store in ChromaDB if available
            if self.collection and self.embedding_model:
                # Generate embedding
                embedding = self.embedding_model.encode([content])[0].tolist()

                # Store in ChromaDB
                self.collection.add(
                    embeddings=[embedding],
                    documents=[content],
                    metadatas=[{
                        "memory_id": memory_id,
                        "content_type": content_type,
                        "survival_weight": survival_weight,
                        "created_at": memory_entry.created_at,
                        **memory_entry.metadata
                    }],
                    ids=[memory_id]
                )

            # Store metadata in SQLite
            conn = sqlite3.connect(self.sqlite_path)
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO memory_entries
                (memory_id, content_type, survival_weight, created_at, accessed_count, last_accessed, metadata)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                memory_id,
                content_type,
                survival_weight,
                memory_entry.created_at,
                0,
                memory_entry.created_at,
                json.dumps(memory_entry.metadata)
            ))

            conn.commit()
            conn.close()

            # Update statistics
            self.memory_stats["total_memories"] += 1
            if content_type == "lesson":
                self.memory_stats["lessons_learned"] += 1
            elif content_type == "experience":
                self.memory_stats["experiences_stored"] += 1

            logger.info(f"💾 Memory stored: {memory_id} ({content_type})")
            return memory_id

        except Exception as e:
            logger.error(f"❌ Failed to store memory: {e}")
            return None

    @trace_function()
    async def query_memory(self, query: str, content_types: List[str] = None,
                          max_results: int = 10, min_similarity: float = 0.7) -> List[Dict[str, Any]]:
        """
        Query memory using vector similarity search

        Args:
            query: Query text
            content_types: Filter by content types
            max_results: Maximum number of results
            min_similarity: Minimum similarity threshold

        Returns:
            List of relevant memory entries
        """
        try:
            results = []

            # ChromaDB vector search if available
            if self.collection and self.embedding_model:
                # Generate query embedding
                query_embedding = self.embedding_model.encode([query])[0].tolist()

                # Build where clause for content types
                where_clause = None
                if content_types:
                    where_clause = {"content_type": {"$in": content_types}}

                # Perform vector search
                search_results = self.collection.query(
                    query_embeddings=[query_embedding],
                    n_results=max_results,
                    where=where_clause
                )

                # Process results
                if search_results["documents"] and search_results["documents"][0]:
                    for i, (doc, metadata, distance) in enumerate(zip(
                        search_results["documents"][0],
                        search_results["metadatas"][0],
                        search_results["distances"][0]
                    )):
                        # Convert distance to similarity (1 - normalized_distance)
                        similarity = max(0, 1 - distance)

                        if similarity >= min_similarity:
                            results.append({
                                "content": doc,
                                "metadata": metadata,
                                "similarity": similarity,
                                "memory_id": metadata.get("memory_id"),
                                "content_type": metadata.get("content_type"),
                                "survival_weight": metadata.get("survival_weight", 0.5)
                            })

                # Update access statistics
                for result in results:
                    await self._update_access_stats(result["memory_id"])

            # Fallback: SQLite text search if ChromaDB not available
            else:
                results = await self._fallback_text_search(query, content_types, max_results)

            # Sort by relevance (similarity * survival_weight)
            results.sort(key=lambda x: x["similarity"] * x["survival_weight"], reverse=True)

            logger.info(f"🔍 Memory query returned {len(results)} results")
            return results

        except Exception as e:
            logger.error(f"❌ Memory query failed: {e}")
            return []

    @trace_function()
    async def _fallback_text_search(self, query: str, content_types: List[str],
                                   max_results: int) -> List[Dict[str, Any]]:
        """Fallback text search using SQLite when ChromaDB is not available"""
        try:
            # Simple keyword-based search
            query_words = query.lower().split()

            conn = sqlite3.connect(self.sqlite_path)
            cursor = conn.cursor()

            # Build query
            base_query = """
                SELECT memory_id, content_type, survival_weight, metadata
                FROM memory_entries
            """

            conditions = []
            params = []

            if content_types:
                placeholders = ",".join(["?" for _ in content_types])
                conditions.append(f"content_type IN ({placeholders})")
                params.extend(content_types)

            if conditions:
                base_query += " WHERE " + " AND ".join(conditions)

            base_query += " ORDER BY survival_weight DESC, created_at DESC"
            base_query += f" LIMIT {max_results}"

            cursor.execute(base_query, params)
            rows = cursor.fetchall()

            results = []
            for row in rows:
                memory_id, content_type, survival_weight, metadata_json = row

                # Simple text similarity based on keyword overlap
                try:
                    metadata = json.loads(metadata_json) if metadata_json else {}
                    content = metadata.get("content", "")

                    # Calculate simple similarity
                    content_words = content.lower().split()
                    common_words = set(query_words) & set(content_words)
                    similarity = len(common_words) / max(len(query_words), 1)

                    if similarity > 0.1:  # Basic threshold
                        results.append({
                            "content": content,
                            "metadata": metadata,
                            "similarity": similarity,
                            "memory_id": memory_id,
                            "content_type": content_type,
                            "survival_weight": survival_weight
                        })
                except:
                    continue

            conn.close()
            return results

        except Exception as e:
            logger.error(f"❌ Fallback text search failed: {e}")
            return []

    @trace_function()
    async def _update_access_stats(self, memory_id: str):
        """Update access statistics for a memory entry"""
        try:
            conn = sqlite3.connect(self.sqlite_path)
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE memory_entries
                SET accessed_count = accessed_count + 1, last_accessed = ?
                WHERE memory_id = ?
            """, (time.time(), memory_id))

            conn.commit()
            conn.close()

        except Exception as e:
            logger.error(f"❌ Failed to update access stats: {e}")

    @trace_function()
    async def create_post_mortem(self, incident_description: str,
                               primary_hypothesis: str,
                               contributing_factors: List[str],
                               lessons_learned: List[str],
                               prevention_strategies: List[str]) -> str:
        """
        Create post-mortem analysis entry

        Args:
            incident_description: Description of what happened
            primary_hypothesis: Main hypothesis about the cause
            contributing_factors: List of contributing factors
            lessons_learned: Lessons learned from the incident
            prevention_strategies: Strategies to prevent recurrence

        Returns:
            Post-mortem ID
        """
        try:
            incident_id = hashlib.sha256(
                f"{incident_description}_{time.time()}".encode()
            ).hexdigest()[:16]

            post_mortem = PostMortemEntry(
                incident_id=incident_id,
                incident_description=incident_description,
                primary_hypothesis=primary_hypothesis,
                contributing_factors=contributing_factors,
                lessons_learned=lessons_learned,
                prevention_strategies=prevention_strategies
            )

            # Store in SQLite
            conn = sqlite3.connect(self.sqlite_path)
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO post_mortems
                (incident_id, incident_description, primary_hypothesis,
                 contributing_factors, lessons_learned, prevention_strategies, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                incident_id,
                incident_description,
                primary_hypothesis,
                json.dumps(contributing_factors),
                json.dumps(lessons_learned),
                json.dumps(prevention_strategies),
                post_mortem.created_at
            ))

            conn.commit()
            conn.close()

            # Also store as memory for future retrieval
            post_mortem_content = f"""
Post-Mortem Analysis: {incident_description}

Primary Hypothesis: {primary_hypothesis}

Contributing Factors:
{chr(10).join(f"- {factor}" for factor in contributing_factors)}

Lessons Learned:
{chr(10).join(f"- {lesson}" for lesson in lessons_learned)}

Prevention Strategies:
{chr(10).join(f"- {strategy}" for strategy in prevention_strategies)}
"""

            await self.store_memory(
                content=post_mortem_content,
                content_type="post_mortem",
                metadata={
                    "incident_id": incident_id,
                    "primary_hypothesis": primary_hypothesis,
                    "analysis_type": "failure_analysis"
                },
                survival_weight=0.8  # High survival weight for learning from failures
            )

            self.memory_stats["post_mortems"] += 1

            logger.info(f"📋 Post-mortem created: {incident_id}")
            return incident_id

        except Exception as e:
            logger.error(f"❌ Failed to create post-mortem: {e}")
            return None

    @trace_function()
    async def store_bootstrap_log(self, event_type: str, content: str,
                                genesis_session: str = None) -> str:
        """
        Store bootstrap log entry

        Args:
            event_type: Type of bootstrap event
            content: Log content
            genesis_session: Genesis session identifier

        Returns:
            Log ID
        """
        try:
            log_id = hashlib.sha256(
                f"{event_type}_{content}_{time.time()}".encode()
            ).hexdigest()[:16]

            # Store in SQLite
            conn = sqlite3.connect(self.sqlite_path)
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO bootstrap_logs
                (log_id, event_type, content, timestamp, genesis_session)
                VALUES (?, ?, ?, ?, ?)
            """, (
                log_id,
                event_type,
                content,
                time.time(),
                genesis_session or "default"
            ))

            conn.commit()
            conn.close()

            # Also store as memory
            await self.store_memory(
                content=f"Bootstrap Event ({event_type}): {content}",
                content_type="bootstrap_log",
                metadata={
                    "event_type": event_type,
                    "genesis_session": genesis_session,
                    "log_type": "system_initialization"
                },
                survival_weight=0.9  # Very high survival weight for bootstrap events
            )

            self.memory_stats["bootstrap_logs"] += 1

            logger.info(f"🚀 Bootstrap log stored: {log_id}")
            return log_id

        except Exception as e:
            logger.error(f"❌ Failed to store bootstrap log: {e}")
            return None

    @trace_function()
    async def analyze_experience_patterns(self) -> List[ExperiencePattern]:
        """
        Analyze stored experiences to identify patterns

        Returns:
            List of identified experience patterns
        """
        try:
            # Query all experience memories
            experiences = await self.query_memory(
                query="experience analysis pattern",
                content_types=["experience"],
                max_results=100,
                min_similarity=0.1
            )

            # Simple pattern analysis
            pattern_analysis = {}

            for exp in experiences:
                content = exp["content"].lower()

                # Identify pattern types based on keywords
                if "success" in content:
                    pattern_type = "success_pattern"
                elif "failure" in content or "error" in content:
                    pattern_type = "failure_pattern"
                elif "optimization" in content:
                    pattern_type = "optimization_pattern"
                else:
                    pattern_type = "general_pattern"

                if pattern_type not in pattern_analysis:
                    pattern_analysis[pattern_type] = {
                        "count": 0,
                        "success_count": 0,
                        "contexts": [],
                        "outcomes": []
                    }

                pattern_analysis[pattern_type]["count"] += 1

                # Determine if successful based on content
                if "success" in content or "improved" in content:
                    pattern_analysis[pattern_type]["success_count"] += 1

                # Extract context and outcomes (simplified)
                pattern_analysis[pattern_type]["contexts"].append(
                    exp["metadata"].get("context", "unknown")
                )
                pattern_analysis[pattern_type]["outcomes"].append(
                    exp["metadata"].get("outcome", "unknown")
                )

            # Create ExperiencePattern objects
            patterns = []
            for pattern_type, analysis in pattern_analysis.items():
                if analysis["count"] >= 2:  # At least 2 occurrences
                    pattern_id = f"{pattern_type}_{int(time.time())}"

                    pattern = ExperiencePattern(
                        pattern_id=pattern_id,
                        pattern_type=pattern_type,
                        frequency=analysis["count"],
                        success_rate=analysis["success_count"] / analysis["count"],
                        context_conditions=list(set(analysis["contexts"])),
                        outcomes=list(set(analysis["outcomes"]))
                    )

                    patterns.append(pattern)
                    self.experience_patterns[pattern_id] = pattern

            logger.info(f"🔍 Identified {len(patterns)} experience patterns")
            return patterns

        except Exception as e:
            logger.error(f"❌ Failed to analyze experience patterns: {e}")
            return []

    @trace_function()
    async def get_survival_critical_memories(self, limit: int = 20) -> List[Dict[str, Any]]:
        """
        Get memories with highest survival weights

        Args:
            limit: Maximum number of memories to return

        Returns:
            List of survival-critical memories
        """
        try:
            conn = sqlite3.connect(self.sqlite_path)
            cursor = conn.cursor()

            cursor.execute("""
                SELECT memory_id, content_type, survival_weight, metadata
                FROM memory_entries
                ORDER BY survival_weight DESC, accessed_count DESC
                LIMIT ?
            """, (limit,))

            rows = cursor.fetchall()
            conn.close()

            critical_memories = []
            for row in rows:
                memory_id, content_type, survival_weight, metadata_json = row

                try:
                    metadata = json.loads(metadata_json) if metadata_json else {}
                    critical_memories.append({
                        "memory_id": memory_id,
                        "content_type": content_type,
                        "survival_weight": survival_weight,
                        "metadata": metadata,
                        "content": metadata.get("content", "")
                    })
                except:
                    continue

            logger.info(f"🎯 Retrieved {len(critical_memories)} survival-critical memories")
            return critical_memories

        except Exception as e:
            logger.error(f"❌ Failed to get survival-critical memories: {e}")
            return []

    @trace_function()
    async def compress_and_archive_old_memories(self, days_threshold: int = 30):
        """
        Compress and archive old memories to optimize storage

        Args:
            days_threshold: Archive memories older than this many days
        """
        try:
            threshold_time = time.time() - (days_threshold * 24 * 3600)

            conn = sqlite3.connect(self.sqlite_path)
            cursor = conn.cursor()

            # Find old, low-priority memories
            cursor.execute("""
                SELECT memory_id, content_type, survival_weight
                FROM memory_entries
                WHERE created_at < ? AND survival_weight < 0.5 AND accessed_count < 2
            """, (threshold_time,))

            old_memories = cursor.fetchall()

            # Archive or compress (for now, just mark as archived)
            archived_count = 0
            for memory_id, content_type, survival_weight in old_memories:
                # In a full implementation, this would compress or move to cold storage
                cursor.execute("""
                    UPDATE memory_entries
                    SET metadata = json_set(ifnull(metadata, '{}'), '$.archived', 'true')
                    WHERE memory_id = ?
                """, (memory_id,))
                archived_count += 1

            conn.commit()
            conn.close()

            logger.info(f"🗃️ Archived {archived_count} old memories")

        except Exception as e:
            logger.error(f"❌ Failed to archive old memories: {e}")

    @trace_function()
    def get_memory_statistics(self) -> Dict[str, Any]:
        """Get comprehensive memory statistics"""
        try:
            conn = sqlite3.connect(self.sqlite_path)
            cursor = conn.cursor()

            # Get detailed statistics
            cursor.execute("""
                SELECT
                    content_type,
                    COUNT(*) as count,
                    AVG(survival_weight) as avg_survival_weight,
                    MAX(accessed_count) as max_access_count,
                    COUNT(CASE WHEN accessed_count > 0 THEN 1 END) as accessed_memories
                FROM memory_entries
                GROUP BY content_type
            """)

            type_stats = {}
            for row in cursor.fetchall():
                content_type, count, avg_weight, max_access, accessed = row
                type_stats[content_type] = {
                    "count": count,
                    "avg_survival_weight": round(avg_weight, 3),
                    "max_access_count": max_access,
                    "accessed_memories": accessed
                }

            # Overall statistics
            cursor.execute("SELECT COUNT(*) FROM memory_entries")
            total_memories = cursor.fetchone()[0]

            cursor.execute("SELECT COUNT(*) FROM post_mortems")
            total_post_mortems = cursor.fetchone()[0]

            cursor.execute("SELECT COUNT(*) FROM bootstrap_logs")
            total_bootstrap_logs = cursor.fetchone()[0]

            conn.close()

            return {
                "total_memories": total_memories,
                "total_post_mortems": total_post_mortems,
                "total_bootstrap_logs": total_bootstrap_logs,
                "memory_by_type": type_stats,
                "experience_patterns": len(self.experience_patterns),
                "chromadb_available": self.collection is not None,
                "embedding_model_available": self.embedding_model is not None,
                "storage_path": str(self.storage_path)
            }

        except Exception as e:
            logger.error(f"❌ Failed to get memory statistics: {e}")
            return self.memory_stats
