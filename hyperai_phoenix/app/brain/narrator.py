"""
HyperAI Phoenix - System Narrator
Centralized logging with structured output and Vietnamese language support
"""

import logging
import json
from datetime import datetime
from typing import Dict, Any, Optional
import os

class VietnameseFormatter(logging.Formatter):
    """Custom formatter for Vietnamese logging"""

    def __init__(self):
        super().__init__(
            fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

    def format(self, record):
        # Add Vietnamese level names
        level_names_vi = {
            'DEBUG': 'GỠ LỖI',
            'INFO': 'THÔNG TIN',
            'WARNING': 'CẢNH BÁO',
            'ERROR': 'LỖI',
            'CRITICAL': 'NGHIÊM TRỌNG'
        }

        original_levelname = record.levelname
        record.levelname = level_names_vi.get(original_levelname, original_levelname)

        formatted = super().format(record)
        record.levelname = original_levelname  # Restore original

        return formatted

class SystemNarrator:
    """Centralized system logging and narration"""

    def __init__(self, log_dir: str = "data/logs", enable_vietnamese: bool = True):
        self.log_dir = log_dir
        self.enable_vietnamese = enable_vietnamese

        # Ensure log directory exists
        os.makedirs(log_dir, exist_ok=True)

        # Setup main logger
        self.logger = logging.getLogger('HyperAI_Phoenix')
        self.logger.setLevel(logging.INFO)

        # Remove existing handlers
        for handler in self.logger.handlers[:]:
            self.logger.removeHandler(handler)

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        if enable_vietnamese:
            console_handler.setFormatter(VietnameseFormatter())
        else:
            console_handler.setFormatter(logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            ))

        self.logger.addHandler(console_handler)

        # File handler for structured logs
        log_file = os.path.join(log_dir, f"hyperai_{datetime.now().strftime('%Y%m%d')}.log")
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        ))

        self.logger.addHandler(file_handler)

        # Event log file (JSON structured)
        self.event_log_file = os.path.join(log_dir, f"events_{datetime.now().strftime('%Y%m%d')}.jsonl")

        # Story tracking
        self.current_story = None
        self.story_events = []

    def start_story(self, story_title: str, context: Dict[str, Any] = None):
        """Begin a new story/session narrative"""
        self.current_story = {
            'title': story_title,
            'start_time': datetime.now(),
            'context': context or {},
            'events': []
        }

        self.story_events = []

        message = f"🌟 Bắt đầu chương mới: {story_title}"
        self.logger.info(message)

        self._write_event({
            'type': 'story_start',
            'story_title': story_title,
            'context': context,
            'timestamp': datetime.now().isoformat()
        })

    def narrate_event(self, event_type: str, message: str,
                     details: Dict[str, Any] = None, level: str = "info"):
        """Narrate a system event with context"""

        # Vietnamese event type translations
        event_types_vi = {
            'initialization': 'khởi tạo',
            'directive_received': 'nhận lệnh',
            'thinking': 'suy nghĩ',
            'execution': 'thực thi',
            'completion': 'hoàn thành',
            'error': 'lỗi',
            'warning': 'cảnh báo',
            'memory_action': 'thao tác bộ nhớ',
            'system_action': 'thao tác hệ thống',
            'user_interaction': 'tương tác người dùng'
        }

        vi_event_type = event_types_vi.get(event_type, event_type)

        # Format message for Vietnamese if enabled
        if self.enable_vietnamese:
            formatted_message = f"[{vi_event_type.upper()}] {message}"
        else:
            formatted_message = f"[{event_type.upper()}] {message}"

        # Log based on level
        if level == "debug":
            self.logger.debug(formatted_message)
        elif level == "info":
            self.logger.info(formatted_message)
        elif level == "warning":
            self.logger.warning(formatted_message)
        elif level == "error":
            self.logger.error(formatted_message)
        elif level == "critical":
            self.logger.critical(formatted_message)

        # Write structured event
        event_data = {
            'type': event_type,
            'message': message,
            'details': details or {},
            'level': level,
            'timestamp': datetime.now().isoformat(),
            'story_title': self.current_story['title'] if self.current_story else None
        }

        self._write_event(event_data)

        # Add to current story
        if self.current_story:
            self.story_events.append(event_data)

    def narrate_directive_flow(self, directive_id: str, stage: str,
                              details: Dict[str, Any] = None):
        """Narrate the flow of a directive through the system"""
        stage_descriptions = {
            'received': 'Đã nhận được lệnh từ người dùng',
            'analyzing': 'Đang phân tích ý định và thực thể',
            'council_voting': 'Hội đồng đang bỏ phiếu',
            'planning': 'Đang lập kế hoạch thực hiện',
            'executing': 'Đang thực thi kế hoạch',
            'completed': 'Đã hoàn thành thành công',
            'failed': 'Thực hiện thất bại',
            'escalated': 'Đã chuyển lên cấp cao hơn'
        }

        description = stage_descriptions.get(stage, f"Giai đoạn: {stage}")
        message = f"Lệnh {directive_id}: {description}"

        self.narrate_event('directive_flow', message, details or {'directive_id': directive_id})

    def narrate_performance(self, metrics: Dict[str, float],
                           comparison: Optional[Dict[str, float]] = None):
        """Narrate performance metrics"""
        avg_duration = metrics.get('avg_duration', 0.0)
        error_rate = metrics.get('error_rate', 0.0)

        performance_msg = f"Hiệu suất hiện tại: thời gian trung bình {avg_duration:.2f}s, tỷ lệ lỗi {error_rate:.2%}"

        if comparison:
            prev_duration = comparison.get('avg_duration', 0.0)
            prev_error_rate = comparison.get('error_rate', 0.0)

            if avg_duration < prev_duration:
                performance_msg += f" (cải thiện tốc độ {prev_duration - avg_duration:.2f}s)"
            elif avg_duration > prev_duration:
                performance_msg += f" (chậm hơn {avg_duration - prev_duration:.2f}s)"

            if error_rate < prev_error_rate:
                performance_msg += f" (giảm lỗi {prev_error_rate - error_rate:.2%})"
            elif error_rate > prev_error_rate:
                performance_msg += f" (tăng lỗi {error_rate - prev_error_rate:.2%})"

        self.narrate_event('system_action', performance_msg, metrics,
                          level="info" if error_rate < 0.1 else "warning")

    def narrate_memory_action(self, action_type: str, count: int,
                             details: Dict[str, Any] = None):
        """Narrate memory-related actions"""
        action_descriptions = {
            'compaction': f'Nén bộ nhớ: {count} sự kiện được lưu trữ lạnh',
            'retrieval': f'Truy xuất bộ nhớ: tìm thấy {count} kết quả',
            'storage': f'Lưu trữ: {count} mục được thêm vào tri thức',
            'cleanup': f'Dọn dẹp: {count} mục cũ được xóa'
        }

        message = action_descriptions.get(action_type, f'{action_type}: {count} mục')
        self.narrate_event('memory_action', message, details)

    def narrate_error(self, error_type: str, error_message: str,
                     context: Dict[str, Any] = None, recovery_action: str = None):
        """Narrate errors with context"""
        message = f"Lỗi {error_type}: {error_message}"

        if recovery_action:
            message += f" | Hành động khôi phục: {recovery_action}"

        self.narrate_event('error', message, context or {'error_type': error_type}, level="error")

    def complete_story(self, summary: str = None):
        """Complete the current story and generate summary"""
        if not self.current_story:
            return

        end_time = datetime.now()
        duration = end_time - self.current_story['start_time']

        self.current_story.update({
            'end_time': end_time,
            'duration_seconds': duration.total_seconds(),
            'total_events': len(self.story_events),
            'summary': summary or self._generate_auto_summary()
        })

        completion_msg = f"🏁 Hoàn thành: {self.current_story['title']} (thời gian: {duration.total_seconds():.1f}s, {len(self.story_events)} sự kiện)"
        self.logger.info(completion_msg)

        # Write story completion event
        self._write_event({
            'type': 'story_complete',
            'story': self.current_story,
            'timestamp': end_time.isoformat()
        })

        # Reset current story
        self.current_story = None
        self.story_events = []

    def _generate_auto_summary(self) -> str:
        """Generate automatic summary of story events"""
        if not self.story_events:
            return "Không có sự kiện nào được ghi nhận"

        event_types = {}
        error_count = 0

        for event in self.story_events:
            event_type = event.get('type', 'unknown')
            event_types[event_type] = event_types.get(event_type, 0) + 1

            if event.get('level') == 'error':
                error_count += 1

        summary_parts = [
            f"Tổng cộng {len(self.story_events)} sự kiện",
            f"Loại sự kiện: {', '.join([f'{k}: {v}' for k, v in event_types.items()])}"
        ]

        if error_count > 0:
            summary_parts.append(f"Có {error_count} lỗi xảy ra")
        else:
            summary_parts.append("Không có lỗi")

        return ". ".join(summary_parts)

    def _write_event(self, event_data: Dict[str, Any]):
        """Write structured event to JSON lines file"""
        try:
            with open(self.event_log_file, 'a', encoding='utf-8') as f:
                f.write(json.dumps(event_data, ensure_ascii=False) + '\n')
        except Exception as e:
            # Fallback to regular logging if file write fails
            self.logger.error(f"Failed to write event to file: {e}")

    def get_recent_events(self, hours: int = 24) -> list:
        """Get recent events from the JSON log"""
        try:
            events = []
            cutoff_time = datetime.now().timestamp() - (hours * 3600)

            with open(self.event_log_file, 'r', encoding='utf-8') as f:
                for line in f:
                    try:
                        event = json.loads(line.strip())
                        event_time = datetime.fromisoformat(event['timestamp']).timestamp()

                        if event_time >= cutoff_time:
                            events.append(event)
                    except (json.JSONDecodeError, KeyError, ValueError):
                        continue

            return sorted(events, key=lambda x: x['timestamp'])

        except FileNotFoundError:
            return []

    def create_daily_chronicle(self, date: str = None) -> Dict[str, Any]:
        """Create a daily chronicle of events"""
        if date is None:
            date = datetime.now().strftime('%Y%m%d')

        event_file = os.path.join(self.log_dir, f"events_{date}.jsonl")

        if not os.path.exists(event_file):
            return {'date': date, 'events': [], 'summary': 'Không có sự kiện'}

        try:
            events = []
            with open(event_file, 'r', encoding='utf-8') as f:
                for line in f:
                    try:
                        event = json.loads(line.strip())
                        events.append(event)
                    except json.JSONDecodeError:
                        continue

            # Analyze events
            stories = {}
            event_types = {}
            error_events = []

            for event in events:
                # Group by story
                story_title = event.get('story_title', 'Unknown')
                if story_title not in stories:
                    stories[story_title] = []
                stories[story_title].append(event)

                # Count event types
                event_type = event.get('type', 'unknown')
                event_types[event_type] = event_types.get(event_type, 0) + 1

                # Collect errors
                if event.get('level') == 'error':
                    error_events.append(event)

            # Generate summary
            summary_parts = [
                f"Ngày {date}: {len(events)} sự kiện, {len(stories)} câu chuyện"
            ]

            if error_events:
                summary_parts.append(f"{len(error_events)} lỗi")
            else:
                summary_parts.append("Không có lỗi")

            if event_types:
                top_events = sorted(event_types.items(), key=lambda x: x[1], reverse=True)[:3]
                summary_parts.append(f"Sự kiện chính: {', '.join([f'{k} ({v})' for k, v in top_events])}")

            chronicle = {
                'date': date,
                'total_events': len(events),
                'stories': stories,
                'event_types': event_types,
                'error_events': error_events,
                'summary': '. '.join(summary_parts),
                'generated_at': datetime.now().isoformat()
            }

            return chronicle

        except Exception as e:
            return {
                'date': date,
                'events': [],
                'summary': f'Lỗi tạo biên niên sử: {e}',
                'error': str(e)
            }

# Singleton narrator instance
narrator = SystemNarrator()

if __name__ == "__main__":
    # Test the narrator
    narrator.start_story("Test Session", {'test_mode': True})

    narrator.narrate_event('initialization', 'System starting up', {'version': '1.0'})
    narrator.narrate_directive_flow('test_directive_001', 'received', {'content': 'test command'})
    narrator.narrate_directive_flow('test_directive_001', 'completed')

    narrator.narrate_performance({'avg_duration': 2.5, 'error_rate': 0.02})
    narrator.narrate_memory_action('compaction', 150)

    narrator.complete_story("Test session completed successfully")

    # Get recent events
    recent = narrator.get_recent_events(1)
    print(f"Recent events: {len(recent)}")

    # Create chronicle
    chronicle = narrator.create_daily_chronicle()
    print(f"Today's chronicle: {chronicle['summary']}")
