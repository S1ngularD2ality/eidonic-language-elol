# glyph_381 – AUTONOMY_LOCK
# Prevent outside override; ensure full self-control in critical moments

class glyph_381:
    def __init__(self):
        self.locked = False

    def activate(self):
        self.locked = True

    def deactivate(self):
        self.locked = False
