# glyph_949 – MOVING_TARGET_PORT_HOP
"""
Moving Target Defense: Port Hopping

Computes time-varying service port from shared secret and epoch window.
Blocks scanners and static firewall rules.

APIs:
- port_for(secret: bytes, epoch_s: int, base=1024, span=40000) -> int
"""

import hashlib

def port_for(secret: bytes, epoch_s: int, base: int = 1024, span: int = 40000) -> int:
    h = hashlib.blake2b(secret + epoch_s.to_bytes(8,"big"), digest_size=8).digest()
    return base + (int.from_bytes(h, "big") % span)
