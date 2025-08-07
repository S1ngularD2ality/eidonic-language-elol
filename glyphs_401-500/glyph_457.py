# glyph_457 – SIGNAL_LOG
# Record all incoming/outgoing signals for audit or replay

class glyph_457:
    def __init__(self):
        self.log = []

    def record(self, signal):
        self.log.append(signal)

    def replay(self):
        return self.log
