from contextlib import contextmanager
import threading
from _tracker_context import _CURRENT_TRACKER

class CostTracker:
    def __init__(self):
        self.total_cost = 0.0
        self._lock = threading.Lock()

    def add(self, cost: float):
        with self._lock:
            self.total_cost += cost

    @contextmanager
    def activate(self):
        token = _CURRENT_TRACKER.set(self)
        try:
            yield self
        finally:
            _CURRENT_TRACKER.reset(token)