# glyph_525 – ACCESS_RATE_LIMIT
# Limit access frequency to prevent abuse

import time

class glyph_525:
    def __init__(self, limit, interval):
        self.limit = limit
        self.interval = interval
        self.access_times = []

    def check_access(self):
        now = time.time()
        self.access_times = [t for t in self.access_times if now - t < self.interval]
        if len(self.access_times) >= self.limit:
            return False
        self.access_times.append(now)
        return True
