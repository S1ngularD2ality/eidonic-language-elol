# glyph_716 – EMERGENT_BEHAVIOR_LOGGER
# Capture surprising outputs via predicate triggers.

import time

class glyph_716:
    """
    .log_if(output, predicate) -> logs when predicate(output) is True.
    .entries -> returns list of dict entries.
    """
    def __init__(self):
        self._entries = []

    def log_if(self, output, predicate):
        try:
            if predicate(output):
                self._entries.append({"ts": time.time(), "output": output})
                return True
        except Exception:
            self._entries.append({"ts": time.time(), "output": output, "error": "predicate_failed"})
            return True
        return False

    def entries(self):
        return list(self._entries)
