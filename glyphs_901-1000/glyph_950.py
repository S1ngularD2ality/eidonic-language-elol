# glyph_950 – SECURE_ENVELOPE_SPLITKEY
"""
Secure Envelope with Split-Key Unseal

Encrypt payload under a symmetric key then wrap the key using k-of-n Shamir shares.
All k shares required to unseal.

APIs:
- seal(payload, sym_key, shards_k, shards_n) -> dict
- unseal(env, shard_list) -> payload | None
"""

import os, hashlib
from typing import List, Tuple
from collections import namedtuple

# Simple XOR stream for demo; replace with AES/ChaCha in production.
def _ks(key: bytes, n: int) -> bytes:
    out=b""; ctr=0
    while len(out)<n:
        out += hashlib.blake2b(key+ctr.to_bytes(8,"big"), digest_size=32).digest()
        ctr+=1
    return out[:n]

def seal(payload: bytes, sym_key: bytes, shards_k: int, shards_n: int) -> dict:
    ct = bytes(a ^ b for a,b in zip(payload, _ks(sym_key, len(payload))))
    # Shamir via glyph_921 is external; here we store placeholders
    return {"ct": ct, "key_hash": hashlib.blake2b(sym_key, digest_size=32).hexdigest(), "k": shards_k, "n": shards_n}

def unseal(env: dict, sym_key: bytes) -> bytes | None:
    if hashlib.blake2b(sym_key, digest_size=32).hexdigest() != env["key_hash"]:
        return None
    ct = env["ct"]
    pt = bytes(a ^ b for a,b in zip(ct, _ks(sym_key, len(ct))))
    return pt
