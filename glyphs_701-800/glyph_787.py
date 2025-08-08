# glyph_787 – SENTINEL_GATEKEEPER
# Controls access to critical operations.

class glyph_787:
    def __init__(self, allowed_keys):
        self.allowed_keys = set(allowed_keys)

    def authorize(self, key):
        return key in self.allowed_keys
