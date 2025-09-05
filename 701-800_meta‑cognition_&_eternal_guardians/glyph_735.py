# glyph_735 – MEMORY_LEAK_WATCHER
# Track object counts over time and flag growth trends.

import gc

class glyph_735:
    def __init__(self, window=5):
        self.window = window
        self.samples = []

    def sample(self):
        gc.collect()
        counts = {}
        for obj in gc.get_objects():
            t = type(obj).__name__
            counts[t] = counts.get(t, 0) + 1
        self.samples.append(sum(counts.values()))
        if len(self.samples) > self.window:
            self.samples.pop(0)
        return self.samples[-1]

    def leaking(self):
        return len(self.samples) == self.window and self.samples[-1] > self.samples[0]
