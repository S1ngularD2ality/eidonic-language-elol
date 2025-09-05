# glyph_328 – PATH_MEMORY
# Remember and replay navigation paths; allow route retracing

class glyph_328:
    def __init__(self):
        self.paths = []

    def record(self, path):
        self.paths.append(path)

    def replay(self, index):
        return self.paths[index] if index < len(self.paths) else None
