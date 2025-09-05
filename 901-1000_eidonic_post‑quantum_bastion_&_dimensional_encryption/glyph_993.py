# glyph_993 – SECURE_TMP_VAULT
"""
Secure Temp Vault

Stores secrets in a temp file-like buffer and wipes on close/revoke.
In-memory bytearray with controlled access.

APIs:
- class TempVault(secret: bytes).read()->bytes|None; wipe()->None
"""

class TempVault:
    def __init__(self, secret: bytes):
        self._buf = bytearray(secret)
        self._alive = True

    def read(self) -> bytes | None:
        return bytes(self._buf) if self._alive else None

    def wipe(self):
        for i in range(len(self._buf)):
            self._buf[i] = 0
        self._alive = False
