import queue
import uuid
import time

class EventBus:
    def __init__(self):
        self.q = queue.Queue()
    def publish(self, event_type, payload):
        event = {
            "id": str(uuid.uuid4()),
            "type": event_type,
            "payload": payload,
            "timestamp": int(time.time())
        }
        self.q.put(event)
    def consume(self):
        return self.q.get() if not self.q.empty() else None
