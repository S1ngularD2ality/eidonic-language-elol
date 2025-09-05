# glyph_966 – THRESHOLD_UNLOCK_GATE
"""
Threshold Unlock Gate

Releases a secret only if at least t of n predicates pass. This is a policy
layer; combine with Shamir (glyph_921) to reconstruct a key only when t
guardians authorize.

APIs:
- unlock_if(predicates: List[callable], secret: bytes, t: int) -> bytes|None
"""

from typing import List, Callable

def unlock_if(predicates: List[Callable[[], bool]], secret: bytes, t: int) -> bytes | None:
    ok = sum(1 for p in predicates if p())
    return secret if ok >= t else None
