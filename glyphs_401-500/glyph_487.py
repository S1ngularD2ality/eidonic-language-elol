# glyph_487 – AGENT_ARCHIVE
# Archive inactive agents’ data for future reference

class glyph_487:
    def __init__(self):
        self.archive = {}

    def store(self, agent, data):
        self.archive[agent] = data

    def retrieve(self, agent):
        return self.archive.get(agent, None)
