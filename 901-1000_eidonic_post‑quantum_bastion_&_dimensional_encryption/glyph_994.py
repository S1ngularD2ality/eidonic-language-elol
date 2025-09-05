# glyph_994 – REKEY_ON_TRANSFER
"""
Rekey-on-Transfer

Derives a fresh per-transfer encryption key from a root + transfer ID + context.
Prevents key reuse across messages/channels.

APIs:
- derive(root: bytes, transfer_id: bytes, context: bytes, out_len=32)->bytes
"""

import hashlib

def derive(root: bytes, transfer_id: bytes, context: bytes, out_len: int = 32) -> bytes:
    return hashlib.blake2b(root + transfer_id + context, digest_size=out_len).digest()
