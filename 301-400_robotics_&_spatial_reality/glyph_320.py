# glyph_320 – TOUCH_MAP
# Build a tactile map of surfaces and textures encountered

class glyph_320:
    def __init__(self):
        self.tactile_map = {}

    def update(self, position, texture):
        self.tactile_map[position] = texture

    def get_texture(self, position):
        return self.tactile_map.get(position, None)
