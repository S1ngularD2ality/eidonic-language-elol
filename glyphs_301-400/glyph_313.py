# glyph_313 – SHAPE_RECALL
# Store and recall distinct object shapes from experience

class glyph_313:
    def __init__(self):
        self.shape_memory = {}

    def remember(self, shape_id, features):
        self.shape_memory[shape_id] = features

    def recall(self, shape_id):
        return self.shape_memory.get(shape_id, None)
