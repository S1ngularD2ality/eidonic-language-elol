# glyph_954 – SECRET_HANDSHAKE_PSK
"""
Secret Handshake (PSK-based, SIGMA-lite Demonstrator)

Mutual authentication using pre-shared key with nonces and MACs.
Not a full SIGMA; educational handshake for air-gapped/agent meshes.

APIs:
- client_hello(psk)->(c_nonce, c_tag)
- server_reply(psk,c_nonce)->(s_nonce, s_tag)
- client_verify(psk,s_nonce,c_nonce,s_tag)->bool
- server_verify(psk,c_nonce,s_nonce,c_tag)->bool
"""

import os, hmac, hashlib

def client_hello(psk: bytes):
    c_nonce = os.urandom(32)
    c_tag = hmac.new(psk, b"CH"+c_nonce, hashlib.blake2b).digest()
    return c_nonce, c_tag

def server_reply(psk: bytes, c_nonce: bytes):
    s_nonce = os.urandom(32)
    s_tag = hmac.new(psk, b"SR"+c_nonce+s_nonce, hashlib.blake2b).digest()
    return s_nonce, s_tag

def client_verify(psk: bytes, s_nonce: bytes, c_nonce: bytes, s_tag: bytes) -> bool:
    ref = hmac.new(psk, b"SR"+c_nonce+s_nonce, hashlib.blake2b).digest()
    return hmac.compare_digest(ref, s_tag)

def server_verify(psk: bytes, c_nonce: bytes, s_nonce: bytes, c_tag: bytes) -> bool:
    ref = hmac.new(psk, b"CH"+c_nonce, hashlib.blake2b).digest()
    return hmac.compare_digest(ref, c_tag)
