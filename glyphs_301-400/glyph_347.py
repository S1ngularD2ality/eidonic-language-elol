# glyph_347 – MIMIC_MOVE
# Copy a demonstrated movement sequence (for learning or adaptation)

class glyph_347:
    def __init__(self):
        self.memory = []

    def record(self, movement_sequence):
        self.memory.append(movement_sequence)

    def replay(self, idx):
        return self.memory[idx] if idx < len(self.memory) else []
