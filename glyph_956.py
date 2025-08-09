# glyph_956 – SESSION_TRANSCRIPT_BIND
"""
Session Transcript Binding

Binds all session messages into a single MAC so they cannot be reordered or
selectively omitted without detection.

APIs:
- bind_transcript(messages: List[bytes], key: bytes) -> bytes
"""

import hmac, hashlib
from typing import List

def bind_transcript(messages: List[bytes], key: bytes) -> bytes:
    mac = hmac.new(key, b"", hashlib.blake2b)
    for m in messages:
        mac.update(len(m).to_bytes(8,"big")); mac.update(m)
    return mac.digest()
