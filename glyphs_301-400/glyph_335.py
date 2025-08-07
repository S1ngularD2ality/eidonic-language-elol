# glyph_335 – TRAIL_MARK
# Drop or record markers along a path for later retrieval

class glyph_335:
    def __init__(self):
        self.trail = []

    def mark(self, position):
        self.trail.append(position)

    def get_trail(self):
        return self.trail
