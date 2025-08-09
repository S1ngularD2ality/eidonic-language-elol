# glyph_937 – PASSWORD_HASH_PBKDF2
"""
Password Hashing (PBKDF2-HMAC-SHA256)

Use high iteration counts; consider Argon2/scrypt (external libs) in production.

APIs:
- hash_password(pw: str, iters=600_000) -> (salt, digest)
- verify_password(pw, salt, digest, iters) -> bool
"""

import os, hashlib, hmac
from typing import Tuple

def hash_password(pw: str, iters: int = 600_000) -> Tuple[bytes, bytes]:
    salt = os.urandom(16)
    dig = hashlib.pbkdf2_hmac("sha256", pw.encode(), salt, iters, dklen=32)
    return salt, dig

def verify_password(pw: str, salt: bytes, digest: bytes, iters: int = 600_000) -> bool:
    test = hashlib.pbkdf2_hmac("sha256", pw.encode(), salt, iters, dklen=32)
    return hmac.compare_digest(test, digest)
