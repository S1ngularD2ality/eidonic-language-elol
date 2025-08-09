# glyph_935 – FPE_FEISTEL_DECIMAL
"""
Format-Preserving Encryption for numeric strings (toy Feistel)

Encrypts a decimal string while preserving length and digit set [0-9].
Use a secure Feistel PRF and strong rounds; demo uses blake2b-based PRF.

APIs:
- fpe_enc(num_str: str, key: bytes, rounds: int=8) -> str
- fpe_dec(cipher_str: str, key: bytes, rounds: int=8) -> str
"""

import hashlib

def _F(key: bytes, data: str, round_no: int) -> int:
    h = hashlib.blake2b(key + data.encode() + round_no.to_bytes(2,"big"), digest_size=8).digest()
    return int.from_bytes(h, "big")

def fpe_enc(num_str: str, key: bytes, rounds: int = 8) -> str:
    assert num_str.isdigit()
    n = len(num_str)
    L = num_str[:n//2]; R = num_str[n//2:]
    for r in range(rounds):
        F = _F(key, R, r) % (10 ** len(L))
        L, R = R, str((int(L) + F) % (10 ** len(L))).zfill(len(L))
    return L + R

def fpe_dec(cipher_str: str, key: bytes, rounds: int = 8) -> str:
    assert cipher_str.isdigit()
    n = len(cipher_str)
    L = cipher_str[:n//2]; R = cipher_str[n//2:]
    for r in reversed(range(rounds)):
        F = _F(key, L, r) % (10 ** len(L))
        L, R = str((int(R) - F) % (10 ** len(R))).zfill(len(R)), L
    return L + R
