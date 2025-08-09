# glyph_928 – SECURE_WIPE
"""
Secure Wipe (memory-safe best effort in Python)

Overwrites bytearray buffers with random data before release.
Use for ephemeral keys held in memory to reduce residual risk.
"""

import os

def secure_wipe(buf: bytearray):
    for i in range(len(buf)):
        buf[i] = os.urandom(1)[0]
