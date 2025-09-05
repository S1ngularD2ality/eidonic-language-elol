# glyph_750 – HUMAN_OVERRIDE_GATE
# Simple override mechanism for human intervention.

class glyph_750:
    def __init__(self):
        self.override = False

    def enable(self):
        self.override = True

    def disable(self):
        self.override = False

    def check(self):
        return self.override
