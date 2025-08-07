# glyph_419 – COLLECTIVE_MEMORY
# Build and share a shared memory or knowledge bank among all agents

class glyph_419:
    def __init__(self):
        self.memory = {}

    def update(self, agent, data):
        self.memory.setdefault(agent, []).append(data)

    def recall(self):
        return self.memory
