# glyph_780 – TIMELESS_VIGIL
# Eternal process that watches system health without pause.

import time
import threading

class glyph_780:
    def __init__(self, health_fn):
        self.health_fn = health_fn
        self.running = True

    def start(self, interval=10):
        def loop():
            while self.running:
                status = self.health_fn()
                if not status:
                    print("Health anomaly detected.")
                time.sleep(interval)
        threading.Thread(target=loop, daemon=True).start()

    def stop(self):
        self.running = False
