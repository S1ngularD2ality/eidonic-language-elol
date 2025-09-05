# glyph_455 – AGENT_TIMELINE
# Track agent activity over time

class glyph_455:
    def __init__(self):
        self.timeline = []

    def log(self, agent, activity):
        self.timeline.append((agent, activity))

    def history(self):
        return self.timeline
