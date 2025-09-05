# glyph_356 – TEMPORAL_MEMORY
# Store and retrieve past sensory states for short-term recall

class glyph_356:
    def __init__(self, max_len=100):
        self.memory = []

    def record(self, state):
        self.memory.append(state)
        if len(self.memory) > self.max_len:
            self.memory.pop(0)

    def recall(self, idx):
        return self.memory[idx] if idx < len(self.memory) else None
