# glyph_393 – OBJECT_SWAP
# Exchange, hand off, or receive objects between robots or humans

class glyph_393:
    def __init__(self):
        self.state = "empty"

    def give(self):
        self.state = "empty"
        return "object given"

    def receive(self):
        self.state = "full"
        return "object received"
