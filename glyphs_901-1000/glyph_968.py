# glyph_968 – TOTP_RFC6238
"""
TOTP (RFC 6238) – Time-based One-Time Passwords

Default: 30-second step, 6 digits, HMAC-SHA1-equivalent using BLAKE2b (demo).
Swap digest for SHA1 if strict RFC compatibility is required.

APIs:
- totp(secret: bytes, time_step: int=30, digits: int=6, t0: int=0, algo='blake2b') -> str
"""

import time, hmac, hashlib

def _digest(algo: str):
    return getattr(hashlib, algo)

def totp(secret: bytes, time_step: int=30, digits: int=6, t0: int=0, algo: str='blake2b') -> str:
    counter = int((int(time.time()) - t0) / time_step)
    msg = counter.to_bytes(8, "big")
    mac = hmac.new(secret, msg, _digest(algo)).digest()
    off = mac[-1] & 0x0F
    code = ((mac[off] & 0x7f) << 24) | (mac[off+1] << 16) | (mac[off+2] << 8) | mac[off+3]
    return str(code % (10 ** digits)).zfill(digits)
