"""
HyperAI Phoenix - Memory Engine
Dual storage system with SQLite (structured data) + ChromaDB (semantic search)
Implements memory compaction and cold storage for immortal memory
"""

import sqlite3
import json
import gzip
import os
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple
import pandas as pd
import chromadb
from sentence_transformers import SentenceTransformer
import logging

class MemoryEngine:
    def __init__(self, db_path: str = "data/databases/hyperai.db",
                 chroma_path: str = "data/databases/knowledge_base",
                 archive_path: str = "data/logs/archive"):
        self.db_path = db_path
        self.chroma_path = chroma_path
        self.archive_path = archive_path

        # Ensure directories exist
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        os.makedirs(chroma_path, exist_ok=True)
        os.makedirs(archive_path, exist_ok=True)

        # Initialize SQLite
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.init_sql_tables()

        # Initialize ChromaDB with offline-friendly configuration
        try:
            self.chroma_client = chromadb.PersistentClient(path=chroma_path)
            # Use a simple offline embedding function that doesn't require internet
            from .tools.offline_embeddings import OfflineEmbeddingFunction
            # Use a new collection name to avoid conflicts
            collection_name = "knowledge_base_offline"
            self.knowledge_collection = self.chroma_client.get_or_create_collection(
                name=collection_name,
                metadata={"description": "Semantic knowledge storage with offline embeddings"},
                embedding_function=OfflineEmbeddingFunction()
            )
            self.logger.info(f"ChromaDB initialized with offline embeddings: {collection_name}")
        except Exception as e:
            # Initialize logger if not already done (backup safety)
            if not hasattr(self, 'logger'):
                self.logger = logging.getLogger(__name__)
            self.logger.warning(f"ChromaDB initialization failed: {e}. Using SQLite fallback.")
            self.chroma_client = None
            self.knowledge_collection = None

        # Initialize embedding model with proper fallback for Vietnamese support
        try:
            # Try multilingual model that supports Vietnamese well
            self.encoder = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
            self.logger.info("Loaded multilingual embedding model for Vietnamese support")
        except Exception as e:
            try:
                # Fallback to smaller multilingual model
                self.encoder = SentenceTransformer('paraphrase-multilingual-mpnet-base-v2')
                self.logger.info("Loaded multilingual MPNet model as fallback")
            except Exception as e2:
                try:
                    # Final fallback to basic English model
                    self.encoder = SentenceTransformer('all-MiniLM-L6-v2')
                    self.logger.warning("Using English-only model - Vietnamese semantic search may be limited")
                except Exception as e3:
                    self.logger.error(f"No embedding model available - semantic search disabled: {e3}")
                    self.encoder = None

    def init_sql_tables(self):
        """Initialize SQLite database tables"""
        cursor = self.conn.cursor()

        # Events table for structured logging
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            session_id TEXT,
            event_type TEXT NOT NULL,
            source TEXT,
            details TEXT,
            duration REAL,
            success BOOLEAN,
            alignment_score REAL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        ''')

        # Summaries table for compacted memories
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS summaries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT UNIQUE NOT NULL,
            event_count INTEGER,
            summary_text TEXT,
            key_learnings TEXT,
            performance_metrics TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        ''')

        # Performance metrics table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS metrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            metric_name TEXT NOT NULL,
            metric_value REAL NOT NULL,
            session_id TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        ''')

        # Phase 2: Agents table for multi-agent coordination
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS agents (
            name TEXT PRIMARY KEY,
            status TEXT NOT NULL DEFAULT 'idle',
            last_active DATETIME,
            performance_score REAL DEFAULT 1.0,
            alignment_score REAL DEFAULT 1.0,
            total_tasks INTEGER DEFAULT 0,
            successful_tasks INTEGER DEFAULT 0,
            average_execution_time REAL DEFAULT 0.0,
            efficiency_factor REAL DEFAULT 1.0,
            capabilities TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        ''')

        # Phase 2: Tools table for advanced tool registry
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS tools (
            name TEXT PRIMARY KEY,
            description TEXT,
            category TEXT,
            last_used DATETIME,
            success_rate REAL DEFAULT 1.0,
            api_calls_count INTEGER DEFAULT 0,
            total_executions INTEGER DEFAULT 0,
            average_duration REAL DEFAULT 0.0,
            alignment_check_passed INTEGER DEFAULT 0,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        ''')

        # Phase 2: Enhanced performance_metrics table with additional columns
        # Check if columns exist before adding them
        try:
            cursor.execute('''
            ALTER TABLE events ADD COLUMN ma30 REAL
            ''')
        except sqlite3.OperationalError as e:
            if "duplicate column name" not in str(e):
                raise

        try:
            cursor.execute('''
            ALTER TABLE events ADD COLUMN ma100 REAL
            ''')
        except sqlite3.OperationalError as e:
            if "duplicate column name" not in str(e):
                raise

        try:
            cursor.execute('''
            ALTER TABLE events ADD COLUMN p90_latency REAL
            ''')
        except sqlite3.OperationalError as e:
            if "duplicate column name" not in str(e):
                raise

        try:
            cursor.execute('''
            ALTER TABLE events ADD COLUMN false_positive BOOLEAN DEFAULT 0
            ''')
        except sqlite3.OperationalError as e:
            if "duplicate column name" not in str(e):
                raise

        # Knowledge fallback table for when ChromaDB is unavailable
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS knowledge_fallback (
            id TEXT PRIMARY KEY,
            content TEXT NOT NULL,
            metadata TEXT,
            timestamp TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        ''')

        self.conn.commit()

    def log_event(self, event_type: str, source: str = None, details: str = None,
                  duration: float = None, success: bool = True,
                  alignment_score: float = None, session_id: str = None) -> int:
        """Log an event to SQLite"""
        cursor = self.conn.cursor()
        timestamp = datetime.now().isoformat()

        cursor.execute('''
        INSERT INTO events (timestamp, session_id, event_type, source, details,
                           duration, success, alignment_score)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (timestamp, session_id, event_type, source, details,
              duration, success, alignment_score))

        self.conn.commit()
        event_id = cursor.lastrowid
        self.logger.info(f"Event logged: {event_type} (ID: {event_id})")
        return event_id

    def store_knowledge(self, content: str, metadata: Dict[str, Any] = None,
                       doc_id: str = None) -> str:
        """Store knowledge in ChromaDB for semantic search"""
        if doc_id is None:
            doc_id = f"doc_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}"

        # Generate embedding if encoder available
        embedding = None
        if self.encoder is not None:
            embedding = self.encoder.encode(content).tolist()

        # Prepare metadata
        if metadata is None:
            metadata = {}
        metadata.update({
            "timestamp": datetime.now().isoformat(),
            "content_length": len(content),
            "language": "vi"
        })

        # Store in ChromaDB with fallback handling
        try:
            if not self.knowledge_collection:
                # Store in SQLite fallback
                cursor = self.conn.cursor()
                cursor.execute('''
                INSERT INTO knowledge_fallback (id, content, metadata, timestamp)
                VALUES (?, ?, ?, ?)
                ''', (doc_id, content, json.dumps(metadata), datetime.now().isoformat()))
                self.conn.commit()
                self.logger.info(f"Knowledge stored in SQLite fallback: {doc_id}")
                return doc_id

            if embedding is not None:
                self.knowledge_collection.add(
                    documents=[content],
                    metadatas=[metadata],
                    ids=[doc_id],
                    embeddings=[embedding]
                )
            else:
                # Store without embedding if encoder not available
                self.knowledge_collection.add(
                    documents=[content],
                    metadatas=[metadata],
                    ids=[doc_id]
                )

            self.logger.info(f"Knowledge stored in ChromaDB: {doc_id}")
            return doc_id

        except Exception as e:
            self.logger.warning(f"ChromaDB storage failed, using SQLite fallback: {e}")
            # Fallback to SQLite
            cursor = self.conn.cursor()
            cursor.execute('''
            INSERT INTO knowledge_fallback (id, content, metadata, timestamp)
            VALUES (?, ?, ?, ?)
            ''', (doc_id, content, json.dumps(metadata), datetime.now().isoformat()))
            self.conn.commit()
            return doc_id

    def semantic_search(self, query: str, n_results: int = 5) -> List[Dict[str, Any]]:
        """Search knowledge using semantic similarity"""
        try:
            if not self.knowledge_collection:
                # Fallback to SQLite text search
                return self._search_knowledge_fallback(query, n_results)

            if self.encoder is None:
                self.logger.warning("Semantic search unavailable - no embedding model, using text search")
                return self._search_knowledge_fallback(query, n_results)

            query_embedding = self.encoder.encode(query).tolist()

            results = self.knowledge_collection.query(
                query_embeddings=[query_embedding],
                n_results=n_results,
                include=['documents', 'metadatas', 'distances']
            )

            # Format results
            formatted_results = []
            for i in range(len(results['ids'][0])):
                formatted_results.append({
                    'id': results['ids'][0][i],
                    'content': results['documents'][0][i],
                    'metadata': results['metadatas'][0][i],
                    'similarity': 1 - results['distances'][0][i]  # Convert distance to similarity
                })

            return formatted_results

        except Exception as e:
            self.logger.warning(f"ChromaDB search failed, using fallback: {e}")
            return self._search_knowledge_fallback(query, n_results)

    def _search_knowledge_fallback(self, query: str, n_results: int = 5) -> List[Dict[str, Any]]:
        """Fallback search using SQLite LIKE queries"""
        cursor = self.conn.cursor()

        # Simple text search with LIKE
        query_lower = query.lower()
        cursor.execute('''
        SELECT id, content, metadata, timestamp
        FROM knowledge_fallback
        WHERE LOWER(content) LIKE ?
        ORDER BY timestamp DESC
        LIMIT ?
        ''', (f'%{query_lower}%', n_results))

        results = cursor.fetchall()
        formatted_results = []

        for row in results:
            try:
                metadata = json.loads(row[2]) if row[2] else {}
            except:
                metadata = {}

            formatted_results.append({
                'id': row[0],
                'content': row[1],
                'metadata': metadata,
                'similarity': 0.5  # Default similarity for text search
            })

        return formatted_results

    def get_recent_events(self, hours: int = 24, session_id: str = None) -> List[Dict]:
        """Get recent events from SQLite"""
        cursor = self.conn.cursor()
        since = (datetime.now() - timedelta(hours=hours)).isoformat()

        if session_id:
            cursor.execute('''
            SELECT * FROM events
            WHERE timestamp > ? AND session_id = ?
            ORDER BY timestamp DESC
            ''', (since, session_id))
        else:
            cursor.execute('''
            SELECT * FROM events
            WHERE timestamp > ?
            ORDER BY timestamp DESC
            ''', (since,))

        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]

        return [dict(zip(columns, row)) for row in rows]

    def record_metric(self, metric_name: str, value: float, session_id: str = None):
        """Record a performance metric"""
        cursor = self.conn.cursor()
        timestamp = datetime.now().isoformat()

        cursor.execute('''
        INSERT INTO metrics (timestamp, metric_name, metric_value, session_id)
        VALUES (?, ?, ?, ?)
        ''', (timestamp, metric_name, value, session_id))

        self.conn.commit()

    def get_performance_metrics(self, days: int = 7) -> Dict[str, float]:
        """Calculate aggregated performance metrics"""
        cursor = self.conn.cursor()
        since = (datetime.now() - timedelta(days=days)).isoformat()

        # Average duration
        cursor.execute('''
        SELECT AVG(duration) FROM events
        WHERE timestamp > ? AND duration IS NOT NULL
        ''', (since,))
        avg_duration = cursor.fetchone()[0] or 0.0

        # Error rate
        cursor.execute('''
        SELECT
            COUNT(*) as total,
            SUM(CASE WHEN success = 0 THEN 1 ELSE 0 END) as errors
        FROM events
        WHERE timestamp > ?
        ''', (since,))
        total, errors = cursor.fetchone()
        error_rate = (errors / total) if total > 0 else 0.0

        # Alignment score
        cursor.execute('''
        SELECT AVG(alignment_score) FROM events
        WHERE timestamp > ? AND alignment_score IS NOT NULL
        ''', (since,))
        alignment_score = cursor.fetchone()[0] or 0.8

        return {
            'avg_duration': avg_duration,
            'error_rate': error_rate,
            'alignment_score': alignment_score,
            'total_events': total or 0
        }

    def compact_memories(self, days_old: int = 7) -> Dict[str, int]:
        """Compact old memories to cold storage (MOP Protocol)"""
        cursor = self.conn.cursor()
        cutoff_date = (datetime.now() - timedelta(days=days_old)).date().isoformat()

        # Get events to archive
        cursor.execute('''
        SELECT * FROM events
        WHERE DATE(timestamp) < ?
        ORDER BY timestamp
        ''', (cutoff_date,))

        events = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        events_data = [dict(zip(columns, row)) for row in events]

        if not events_data:
            return {'archived_events': 0, 'summaries_created': 0}

        # Group by date and create summaries
        daily_groups = {}
        for event in events_data:
            date = datetime.fromisoformat(event['timestamp']).date().isoformat()
            if date not in daily_groups:
                daily_groups[date] = []
            daily_groups[date].append(event)

        summaries_created = 0
        for date, day_events in daily_groups.items():
            # Create daily summary
            summary_text = self._create_daily_summary(day_events)
            key_learnings = self._extract_key_learnings(day_events)
            metrics = self._calculate_daily_metrics(day_events)

            # Store summary
            cursor.execute('''
            INSERT OR REPLACE INTO summaries
            (date, event_count, summary_text, key_learnings, performance_metrics)
            VALUES (?, ?, ?, ?, ?)
            ''', (date, len(day_events), summary_text,
                  json.dumps(key_learnings), json.dumps(metrics)))
            summaries_created += 1

            # Archive to cold storage
            archive_file = os.path.join(self.archive_path, f"events_{date}.json.gz")
            with gzip.open(archive_file, 'wt', encoding='utf-8') as f:
                json.dump(day_events, f, ensure_ascii=False, indent=2)

        # Delete archived events
        cursor.execute('DELETE FROM events WHERE DATE(timestamp) < ?', (cutoff_date,))
        self.conn.commit()

        self.logger.info(f"Memory compaction completed: {len(events_data)} events archived, {summaries_created} summaries created")

        return {
            'archived_events': len(events_data),
            'summaries_created': summaries_created
        }

    def _create_daily_summary(self, events: List[Dict]) -> str:
        """Create a textual summary of daily events"""
        if not events:
            return ""

        event_types = {}
        total_duration = 0
        success_count = 0

        for event in events:
            event_type = event.get('event_type', 'unknown')
            event_types[event_type] = event_types.get(event_type, 0) + 1

            if event.get('duration'):
                total_duration += event['duration']
            if event.get('success'):
                success_count += 1

        summary_parts = [
            f"Tổng cộng {len(events)} sự kiện",
            f"Tỷ lệ thành công: {success_count}/{len(events)} ({success_count/len(events)*100:.1f}%)",
        ]

        if total_duration > 0:
            summary_parts.append(f"Thời gian xử lý trung bình: {total_duration/len(events):.2f}s")

        if event_types:
            summary_parts.append("Loại sự kiện: " + ", ".join([f"{k}: {v}" for k, v in event_types.items()]))

        return ". ".join(summary_parts)

    def _extract_key_learnings(self, events: List[Dict]) -> List[str]:
        """Extract key learnings from daily events"""
        learnings = []

        # Identify patterns
        error_events = [e for e in events if not e.get('success', True)]
        if error_events:
            error_types = [e.get('event_type', 'unknown') for e in error_events]
            learnings.append(f"Các lỗi phổ biến: {', '.join(set(error_types))}")

        # Performance insights
        durations = [e.get('duration', 0) for e in events if e.get('duration')]
        if durations:
            avg_duration = sum(durations) / len(durations)
            if avg_duration > 10:
                learnings.append("Hiệu suất cần cải thiện - thời gian xử lý cao")

        return learnings

    def _calculate_daily_metrics(self, events: List[Dict]) -> Dict[str, float]:
        """Calculate daily performance metrics"""
        total = len(events)
        if total == 0:
            return {}

        success_count = sum(1 for e in events if e.get('success', True))
        durations = [e.get('duration', 0) for e in events if e.get('duration')]
        alignment_scores = [e.get('alignment_score') for e in events if e.get('alignment_score') is not None]

        metrics = {
            'total_events': total,
            'success_rate': success_count / total,
            'error_rate': 1 - (success_count / total)
        }

        if durations:
            metrics['avg_duration'] = sum(durations) / len(durations)
            metrics['max_duration'] = max(durations)

        if alignment_scores:
            metrics['avg_alignment_score'] = sum(alignment_scores) / len(alignment_scores)

        return metrics

    def implant_will_and_fasr(self, will_data: Dict, fasr_data: Dict):
        """Implant system will and FASR state into memory (Genesis Protocol)"""
        # Store will as knowledge
        will_content = json.dumps(will_data, ensure_ascii=False, indent=2)
        self.store_knowledge(
            content=will_content,
            metadata={
                "type": "system_will",
                "importance": "critical",
                "immutable": True
            },
            doc_id="system_will_v1"
        )

        # Store FASR state
        fasr_content = json.dumps(fasr_data, ensure_ascii=False, indent=2)
        self.store_knowledge(
            content=fasr_content,
            metadata={
                "type": "fasr_state",
                "importance": "high",
                "mutable": True
            },
            doc_id="fasr_state_current"
        )

        # Log the implantation
        self.log_event(
            event_type="genesis_implantation",
            source="system",
            details="Will and FASR state implanted successfully",
            success=True,
            alignment_score=1.0
        )

        self.logger.info("Will and FASR state implanted into memory")

    # Phase 2: Multi-Agent System Support Methods
    def update_agent_metrics(self, agent_name: str, metrics: Dict[str, Any]):
        """Update agent performance metrics"""
        cursor = self.conn.cursor()

        # Insert or update agent record
        cursor.execute('''
        INSERT OR REPLACE INTO agents
        (name, status, last_active, performance_score, alignment_score,
         total_tasks, successful_tasks, average_execution_time, efficiency_factor, capabilities, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
        ''', (
            agent_name,
            metrics.get('status', 'idle'),
            datetime.now().isoformat(),
            metrics.get('performance_score', 1.0),
            metrics.get('alignment_score', 1.0),
            metrics.get('total_tasks', 0),
            metrics.get('successful_tasks', 0),
            metrics.get('average_execution_time', 0.0),
            metrics.get('efficiency_factor', 1.0),
            json.dumps(metrics.get('capabilities', []))
        ))

        self.conn.commit()

    def get_agent_metrics(self, agent_name: str = None) -> Dict[str, Any]:
        """Get agent performance metrics"""
        cursor = self.conn.cursor()

        if agent_name:
            cursor.execute('SELECT * FROM agents WHERE name = ?', (agent_name,))
            row = cursor.fetchone()
            if row:
                columns = [desc[0] for desc in cursor.description]
                return dict(zip(columns, row))
            return {}
        else:
            cursor.execute('SELECT * FROM agents ORDER BY last_active DESC')
            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
            return [dict(zip(columns, row)) for row in rows]

    def update_tool_metrics(self, tool_name: str, metrics: Dict[str, Any]):
        """Update tool performance metrics"""
        cursor = self.conn.cursor()

        cursor.execute('''
        INSERT OR REPLACE INTO tools
        (name, description, category, last_used, success_rate, api_calls_count,
         total_executions, average_duration, alignment_check_passed, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
        ''', (
            tool_name,
            metrics.get('description', ''),
            metrics.get('category', 'general'),
            datetime.now().isoformat(),
            metrics.get('success_rate', 1.0),
            metrics.get('api_calls_count', 0),
            metrics.get('total_executions', 0),
            metrics.get('average_duration', 0.0),
            metrics.get('alignment_check_passed', 0)
        ))

        self.conn.commit()

    def get_tool_metrics(self, tool_name: str = None) -> Dict[str, Any]:
        """Get tool performance metrics"""
        cursor = self.conn.cursor()

        if tool_name:
            cursor.execute('SELECT * FROM tools WHERE name = ?', (tool_name,))
            row = cursor.fetchone()
            if row:
                columns = [desc[0] for desc in cursor.description]
                return dict(zip(columns, row))
            return {}
        else:
            cursor.execute('SELECT * FROM tools ORDER BY last_used DESC')
            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
            return [dict(zip(columns, row)) for row in rows]

    def log_agent_task(self, agent_name: str, task_type: str, success: bool,
                      execution_time: float, details: str = None):
        """Log agent task execution"""
        self.log_event(
            event_type="agent_task_completed",
            source=f"agent_{agent_name}",
            details=f"Task: {task_type}, Success: {success}, Details: {details or 'N/A'}",
            duration=execution_time,
            success=success,
            alignment_score=1.0 if success else 0.5
        )

    def log_tool_execution(self, tool_name: str, success: bool, execution_time: float,
                          api_calls: int = 0, alignment_passed: bool = True):
        """Log tool execution"""
        self.log_event(
            event_type="tool_executed",
            source=f"tool_{tool_name}",
            details=f"Tool: {tool_name}, API calls: {api_calls}, Alignment: {alignment_passed}",
            duration=execution_time,
            success=success,
            alignment_score=1.0 if alignment_passed else 0.7
        )

    def batch_process_false_positives(self, false_positives: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Batch process false positive events for improvement"""
        cursor = self.conn.cursor()

        # Mark events as false positives
        for fp in false_positives:
            event_id = fp.get('event_id')
            if event_id:
                cursor.execute('''
                UPDATE events SET false_positive = 1 WHERE id = ?
                ''', (event_id,))

        self.conn.commit()

        # Log batch processing
        self.log_event(
            event_type="false_positive_batch_processed",
            source="self_improver",
            details=f"Processed {len(false_positives)} false positives",
            success=True,
            alignment_score=1.0
        )

        return {
            'processed_count': len(false_positives),
            'batch_id': f"batch_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            'timestamp': datetime.now().isoformat()
        }

    def calculate_moving_averages(self, metric_name: str, window_30: int = 30,
                                 window_100: int = 100) -> Dict[str, float]:
        """Calculate moving averages for performance metrics"""
        cursor = self.conn.cursor()

        # Get recent events with the metric
        if metric_name == 'duration':
            cursor.execute('''
            SELECT duration FROM events
            WHERE duration IS NOT NULL
            ORDER BY timestamp DESC
            LIMIT ?
            ''', (window_100,))
        elif metric_name == 'alignment_score':
            cursor.execute('''
            SELECT alignment_score FROM events
            WHERE alignment_score IS NOT NULL
            ORDER BY timestamp DESC
            LIMIT ?
            ''', (window_100,))
        else:
            return {}

        values = [row[0] for row in cursor.fetchall()]

        if not values:
            return {}

        ma30 = sum(values[:window_30]) / min(len(values), window_30) if values else 0
        ma100 = sum(values[:window_100]) / min(len(values), window_100) if values else 0

        return {
            'ma30': ma30,
            'ma100': ma100,
            'data_points': len(values)
        }

    def calculate_p90_latency(self, hours: int = 24) -> float:
        """Calculate P90 latency from recent events"""
        cursor = self.conn.cursor()
        since = (datetime.now() - timedelta(hours=hours)).isoformat()

        cursor.execute('''
        SELECT duration FROM events
        WHERE timestamp > ? AND duration IS NOT NULL
        ORDER BY duration
        ''', (since,))

        durations = [row[0] for row in cursor.fetchall()]

        if len(durations) < 10:
            return 0.0

        p90_index = int(len(durations) * 0.9)
        return durations[p90_index]

    def get_performance_trends(self, days: int = 7) -> Dict[str, Any]:
        """Get comprehensive performance trends for Phase 2 analysis"""
        metrics = self.get_performance_metrics(days)

        # Add moving averages
        duration_ma = self.calculate_moving_averages('duration')
        alignment_ma = self.calculate_moving_averages('alignment_score')

        # Add P90 latency
        p90_latency = self.calculate_p90_latency(24)

        trends = {
            **metrics,
            'duration_ma30': duration_ma.get('ma30', 0),
            'duration_ma100': duration_ma.get('ma100', 0),
            'alignment_ma30': alignment_ma.get('ma30', 0.8),
            'alignment_ma100': alignment_ma.get('ma100', 0.8),
            'p90_latency': p90_latency,
            'analysis_timestamp': datetime.now().isoformat()
        }

        return trends

    def close(self):
        """Safely close all connections"""
        if hasattr(self, 'conn') and self.conn:
            self.conn.close()
        self.logger.info("Memory engine closed safely")

if __name__ == "__main__":
    # Test the memory engine
    memory = MemoryEngine()

    # Test event logging
    event_id = memory.log_event("test_event", "system", "Testing memory engine", 1.5, True, 0.9)
    print(f"Logged event ID: {event_id}")

    # Test knowledge storage
    doc_id = memory.store_knowledge("Đây là kiến thức thử nghiệm về HyperAI Phoenix")
    print(f"Stored knowledge ID: {doc_id}")

    # Test semantic search
    results = memory.semantic_search("HyperAI")
    print(f"Search results: {len(results)}")

    # Test metrics
    memory.record_metric("test_metric", 42.0)
    metrics = memory.get_performance_metrics()
    print(f"Performance metrics: {metrics}")

    memory.close()
    # Test metrics
    memory.record_metric("test_metric", 42.0)
    metrics = memory.get_performance_metrics()
    print(f"Performance metrics: {metrics}")

    memory.close()
