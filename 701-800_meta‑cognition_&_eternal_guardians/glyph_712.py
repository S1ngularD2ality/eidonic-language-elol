# glyph_712 – PERSISTENT_MEMORY_SANCTUM
# Protected key-value store with write-once and role-gated access.

class glyph_712:
    """
    .set(key, value, role='guardian', write_once=False)
    .get(key, role)
    """
    def __init__(self):
        self.store = {}
        self.write_once_keys = set()
        self.roles = {"guardian", "reader"}

    def set(self, key, value, role="guardian", write_once=False):
        if role != "guardian":
            raise PermissionError("Only guardian may set values.")
        if key in self.write_once_keys:
            raise PermissionError("Key is write-once and already set.")
        self.store[key] = value
        if write_once:
            self.write_once_keys.add(key)

    def get(self, key, role="reader"):
        if role not in self.roles:
            raise PermissionError("Unknown role.")
        return self.store.get(key, None)
