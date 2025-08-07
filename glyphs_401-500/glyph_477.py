# glyph_477 – AGENT_TRACE
# Trace and log an agent's journey through tasks or locations

class glyph_477:
    def __init__(self):
        self.trace_log = []

    def add(self, step):
        self.trace_log.append(step)

    def history(self):
        return self.trace_log
