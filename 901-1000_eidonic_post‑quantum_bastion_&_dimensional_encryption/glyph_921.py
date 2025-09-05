# glyph_921 – SHAMIR_SECRET_SHARING_GF256
"""
Shamir Secret Sharing (GF(256), k-of-n)

Splits a secret into n shares so that any k reconstruct, but fewer reveal nothing.
- Field: GF(256) with AES polynomial (0x11b)
- Use for distributing master keys across guardians / machines.

APIs:
- split(secret: bytes, k: int, n: int) -> List[(x, share_bytes)]
- combine(shares: List[(x, share_bytes)]) -> secret: bytes

Notes:
- x indices must be unique in 1..255.
- All shares are same length as secret.
"""

import os
from typing import List, Tuple

_POLY = 0x11b

def _gf_mul(a: int, b: int) -> int:
    p = 0
    for _ in range(8):
        if b & 1: p ^= a
        hi = a & 0x80
        a = (a << 1) & 0xFF
        if hi: a ^= _POLY
        b >>= 1
    return p

def _gf_pow(a: int, n: int) -> int:
    res = 1
    while n:
        if n & 1: res = _gf_mul(res, a)
        a = _gf_mul(a, a)
        n >>= 1
    return res

def _gf_inv(a: int) -> int:
    assert a != 0
    return _gf_pow(a, 254)

def _poly_eval(coeffs: List[int], x: int) -> int:
    y = 0
    for c in reversed(coeffs):
        y = _gf_mul(y, x) ^ c
    return y

def split(secret: bytes, k: int, n: int) -> List[Tuple[int, bytes]]:
    assert 2 <= k <= n <= 255
    L = len(secret)
    shares = [(i, bytearray(L)) for i in range(1, n+1)]
    for j, s in enumerate(secret):
        coeffs = [s] + list(os.urandom(k-1))
        for idx, (x, buf) in enumerate(shares):
            buf[j] = _poly_eval(coeffs, x)
    return [(x, bytes(buf)) for x, buf in shares]

def combine(shares: List[Tuple[int, bytes]]) -> bytes:
    assert len(shares) >= 2
    L = len(shares[0][1])
    for _, b in shares: assert len(b) == L
    xs = [x for x, _ in shares]
    out = bytearray(L)
    for j in range(L):
        y = 0
        for i, (xi, bi) in enumerate(shares):
            # Lagrange basis Li(0)
            num = 1
            den = 1
            for m, (xm, _) in enumerate(shares):
                if m == i: continue
                num = _gf_mul(num, xm)
                den = _gf_mul(den, xi ^ xm)
            li0 = _gf_mul(num, _gf_inv(den))
            y ^= _gf_mul(li0, bi[j])
        out[j] = y
    return bytes(out)
