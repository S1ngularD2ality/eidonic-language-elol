# glyph_973 – HASH_KEM_WRAP
"""
Hash-Based KEM (Toy Encapsulation)

Encapsulates a random symmetric key with a recipient's public identifier (hash).
Recipient derives the same by hashing (id || nonce). No public-key math—suited
for sealed channels with pre-shared identity hashes.

APIs:
- encaps(recipient_id_hash: bytes) -> (nonce, enc_key, tag)
- decaps(recipient_id_hash: bytes, nonce: bytes, tag: bytes) -> enc_key
"""

import os, hashlib, hmac

def encaps(recipient_id_hash: bytes) -> tuple[bytes, bytes, bytes]:
    nonce = os.urandom(32)
    key   = hashlib.blake2b(recipient_id_hash + nonce, digest_size=32).digest()
    tag   = hmac.new(key, b"KEM", hashlib.blake2b).digest()
    return nonce, key, tag

def decaps(recipient_id_hash: bytes, nonce: bytes, tag: bytes) -> bytes | None:
    key = hashlib.blake2b(recipient_id_hash + nonce, digest_size=32).digest()
    return key if hmac.compare_digest(hmac.new(key, b"KEM", hashlib.blake2b).digest(), tag) else None
