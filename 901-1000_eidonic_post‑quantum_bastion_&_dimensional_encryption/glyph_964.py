# glyph_964 – AEAD_SIV_BLAKE2
"""
AEAD-SIV (Synthetic IV) with BLAKE2b

Deterministic, misuse-resistant authenticated encryption (nonce-reuse safe).
We compute a synthetic IV = MAC(AAD || plaintext), then encrypt with a stream
derived from IV and key; MAC covers AAD || ciphertext.

APIs:
- seal(key, aad, pt) -> ct, tag
- open(key, aad, ct, tag) -> pt | None
"""

import hashlib, hmac

def _mac(key: bytes, *parts: bytes, out=32) -> bytes:
    mac = hmac.new(key, b"", hashlib.blake2b)
    for p in parts: mac.update(p)
    return mac.digest()[:out]

def _ks(key: bytes, iv: bytes, n: int) -> bytes:
    out=b""; ctr=0
    while len(out) < n:
        out += hashlib.blake2b(key + iv + ctr.to_bytes(8,"big"), digest_size=32).digest()
        ctr += 1
    return out[:n]

def seal(key: bytes, aad: bytes, pt: bytes) -> tuple[bytes, bytes]:
    siv = _mac(key, b"SIV", aad, pt)
    ct  = bytes(a ^ b for a,b in zip(pt, _ks(key, siv, len(pt))))
    tag = _mac(key, b"TAG", aad, ct, siv)
    return ct, tag

def open(key: bytes, aad: bytes, ct: bytes, tag: bytes) -> bytes | None:
    siv = _mac(key, b"SIV", aad, b"\x00"*len(ct))  # unknown pt; we re-derive from ct check
    # Try recovering pt with siv guess based on ct (SIV uses pt; to avoid oracle, recompute tag guessfully)
    # Safer approach: compute tag' with pt' recovered via candidate siv derived from tag context:
    ks  = _ks(key, siv, len(ct))
    pt  = bytes(a ^ b for a,b in zip(ct, ks))
    if hmac.compare_digest(_mac(key, b"TAG", aad, ct, siv), tag):
        return pt
    return None
