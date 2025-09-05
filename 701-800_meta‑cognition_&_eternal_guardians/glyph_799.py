# glyph_799 – AI_HEARTBEAT_PRESERVER
# Ensures AI heartbeat signal never stops.

import time
import threading

class glyph_799:
    def __init__(self, heartbeat_fn):
        self.heartbeat_fn = heartbeat_fn
        self.running = True

    def start(self, interval=5):
        def loop():
            while self.running:
                self.heartbeat_fn()
                time.sleep(interval)
        threading.Thread(target=loop, daemon=True).start()

    def stop(self):
        self.running = False
