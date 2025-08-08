# glyph_784 – CRYSTAL_MEMORY_ARCHIVE
# Immutable, compressed long-term archive.

import zlib

class glyph_784:
    def __init__(self):
        self.archive = {}

    def store(self, key, data):
        self.archive[key] = zlib.compress(data.encode())

    def retrieve(self, key):
        return zlib.decompress(self.archive[key]).decode()
