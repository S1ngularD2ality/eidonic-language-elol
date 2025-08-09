# glyph_914 – EIDON_PHASE_SHIFT_CRYPT
"""
Eidon Phase-Shift Crypt

Time/phase-varying stream cipher: keystream samples from sin/cos phase map
hashed into bytes. Requires synchronized (t0, step, rounds) across endpoints.
"""

import math, hashlib

def phase_keystream(length: int, t0: float, step: float, rounds: int = 3) -> bytes:
    ks = b""
    t = t0
    for _ in range((length + 31)//32):
        x = 0.0
        for r in range(1, rounds+1):
            x += math.sin(t*r) + math.cos(t*r*r)
        h = hashlib.blake2b(str(x).encode(), digest_size=32).digest()
        ks += h
        t += step
    return ks[:length]

def psc_encrypt(data: bytes, t0: float, step: float, rounds: int = 3) -> bytes:
    ks = phase_keystream(len(data), t0, step, rounds)
    return bytes(a ^ b for a, b in zip(data, ks))

def psc_decrypt(cipher: bytes, t0: float, step: float, rounds: int = 3) -> bytes:
    return psc_encrypt(cipher, t0, step, rounds)
