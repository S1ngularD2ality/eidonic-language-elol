# glyph_401 – AGENT_SWARM
# Create and manage a dynamic swarm of cooperating AI/robot agents

class glyph_401:
    def __init__(self):
        self.swarm = []

    def add(self, agent):
        self.swarm.append(agent)

    def broadcast(self, message):
        return {a: message for a in self.swarm}
