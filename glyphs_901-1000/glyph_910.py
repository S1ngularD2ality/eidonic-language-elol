# glyph_910 – RESONANCE_KEY_EXCHANGE
"""
Resonance Key Exchange (RKE) – Demonstrator

Both parties compute a shared key by hashing their ephemeral secrets combined
with a shared 'resonance tag'. Use proper PAKE/KEM in production; this is a
conceptual scaffold for resonance-bound derivations.
"""

import hashlib, hmac

def rke_derive(local_secret: bytes, remote_hint: bytes, resonance_tag: bytes) -> bytes:
    seed = hashlib.sha3_512(local_secret + remote_hint + resonance_tag).digest()
    return hmac.new(seed, b"RKE", hashlib.blake2b).digest()
