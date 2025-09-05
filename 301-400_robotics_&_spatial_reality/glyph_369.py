# glyph_369 – MEMORY_ANCHOR
# Anchor specific spatial points for easy recall/navigation later

class glyph_369:
    def __init__(self):
        self.anchors = {}

    def set_anchor(self, label, position):
        self.anchors[label] = position

    def get_anchor(self, label):
        return self.anchors.get(label, None)
