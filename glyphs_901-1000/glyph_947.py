# glyph_947 – DUAL_KEY_DENIABLE_LAYER
"""
Dual-Key Deniable Encryption Layer (Toy)

Encrypt content under (real_key, decoy_key). Decryption with decoy_key yields
a plausible decoy message; with real_key yields true content.

APIs:
- encrypt(real: bytes, decoy: bytes, real_key: bytes, decoy_key: bytes) -> bytes
- decrypt(blob, key) -> bytes
"""

import hashlib, hmac, os

def _keystream(key: bytes, n: int) -> bytes:
    out=b""; ctr=0
    while len(out)<n:
        out += hashlib.blake2b(key+ctr.to_bytes(8,"big"), digest_size=32).digest()
        ctr+=1
    return out[:n]

def encrypt(real: bytes, decoy: bytes, real_key: bytes, decoy_key: bytes) -> bytes:
    # store both ciphertexts with MACs; order ambiguous
    c1 = bytes(a ^ b for a,b in zip(real, _keystream(real_key, len(real))))
    c2 = bytes(a ^ b for a,b in zip(decoy,_keystream(decoy_key,len(decoy))))
    mac1 = hmac.new(real_key, c1, hashlib.blake2b).digest()
    mac2 = hmac.new(decoy_key, c2, hashlib.blake2b).digest()
    # layout: len1|len2|c1|mac1|c2|mac2
    return len(c1).to_bytes(4,"big")+len(c2).to_bytes(4,"big")+c1+mac1+c2+mac2

def decrypt(blob: bytes, key: bytes) -> bytes:
    l1 = int.from_bytes(blob[:4],"big"); l2 = int.from_bytes(blob[4:8],"big")
    off = 8
    c1 = blob[off:off+l1]; off+=l1
    mac1 = blob[off:off+64]; off+=64
    c2 = blob[off:off+l2]; off+=l2
    mac2 = blob[off:off+64]
    if hmac.compare_digest(hmac.new(key,c1,hashlib.blake2b).digest(), mac1):
        return bytes(a ^ b for a,b in zip(c1,_keystream(key,len(c1))))
    if hmac.compare_digest(hmac.new(key,c2,hashlib.blake2b).digest(), mac2):
        return bytes(a ^ b for a,b in zip(c2,_keystream(key,len(c2))))
    return b""
