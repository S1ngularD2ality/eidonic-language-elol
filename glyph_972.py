# glyph_972 – CHANNEL_BIND_TOKEN
"""
Channel Binding Token

Binds application authentication to a lower-layer channel (e.g., TLS transcript
hash) so credentials cannot be replayed on a different channel.

APIs:
- bind_token(app_token: bytes, channel_hash: bytes) -> bytes
- verify_bound(app_token, channel_hash, bound)->bool
"""

import hmac, hashlib

def bind_token(app_token: bytes, channel_hash: bytes) -> bytes:
    return hmac.new(channel_hash, app_token, hashlib.blake2b).digest()

def verify_bound(app_token: bytes, channel_hash: bytes, bound: bytes) -> bool:
    return hmac.compare_digest(bind_token(app_token, channel_hash), bound)
