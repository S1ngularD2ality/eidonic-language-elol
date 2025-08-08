# glyph_761 – PERSISTENT_AUDIT_LOG
# Immutable, append-only system log for auditing.

import time
import hashlib

class glyph_761:
    def __init__(self):
        self.log = []

    def append(self, event):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        entry = f"{timestamp} | {event}"
        checksum = hashlib.sha256(entry.encode()).hexdigest()
        self.log.append((entry, checksum))

    def get_log(self):
        return list(self.log)
