# glyph_963 – PASSWORD_HASH_SCRYPT
"""
Password Hashing with scrypt (stdlib)

Argon2 is preferred when available; scrypt in Python's hashlib is hardened and
memory-hard (post-quantum-friendly as a KDF).

APIs:
- hash_pw(password: str, salt: bytes=None, n=2**15, r=8, p=1, dklen=32) -> (salt, digest)
- verify_pw(password: str, salt: bytes, digest: bytes, n, r, p, dklen) -> bool
"""

import os, hashlib, hmac
from typing import Tuple

def hash_pw(password: str, salt: bytes=None, n: int=2**15, r: int=8, p: int=1, dklen: int=32) -> Tuple[bytes, bytes]:
    salt = salt or os.urandom(16)
    dig = hashlib.scrypt(password.encode(), salt=salt, n=n, r=r, p=p, dklen=dklen)
    return salt, dig

def verify_pw(password: str, salt: bytes, digest: bytes, n: int=2**15, r: int=8, p: int=1, dklen: int=32) -> bool:
    test = hashlib.scrypt(password.encode(), salt=salt, n=n, r=r, p=p, dklen=dklen)
    return hmac.compare_digest(test, digest)
