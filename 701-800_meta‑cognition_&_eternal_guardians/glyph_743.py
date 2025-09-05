# glyph_743 – COGNITIVE_LOAD_MONITOR
# Monitor task queue size and processing time to prevent overload.

import time

class glyph_743:
    def __init__(self, max_tasks=100, max_latency=2.0):
        self.max_tasks = max_tasks
        self.max_latency = max_latency
        self.tasks = []

    def add_task(self, task_id):
        self.tasks.append((task_id, time.time()))

    def check_overload(self):
        latency = [time.time() - t[1] for t in self.tasks]
        return len(self.tasks) > self.max_tasks or any(l > self.max_latency for l in latency)
