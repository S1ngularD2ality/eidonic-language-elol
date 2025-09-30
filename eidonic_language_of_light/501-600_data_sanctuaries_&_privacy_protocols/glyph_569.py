# glyph_569.py — Secure Random String
# -----------------------------------------------------------------------------
# ID:            569
# Pack:          Pack 006 (501–600)
# Name:          Secure Random String
# Class:         prf_stream
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # PRF-based; no OS RNG
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import hashlib, base64

def glyph_569(length: int, *, key: bytes, nonce: bytes) -> str:
    """
    Secure Random String — deterministic URL-safe base64 string from PRF stream.

    Parameters
    ----------
    length : int
    key    : bytes
    nonce  : bytes

    Returns
    -------
    str : requested length (truncated)

    Examples
    --------
    >>> s = glyph_569(10, key=b'k', nonce=b'n'); len(s) == 10
    True
    """
    if length < 0:
        raise ValueError("length must be >= 0")
    out = bytearray()
    i = 0
    while len(out) < (length * 2):  # overproduce for base64 expansion
        out.extend(hashlib.sha256(key + nonce + i.to_bytes(8, "big")).digest())
        i += 1
    s = base64.urlsafe_b64encode(bytes(out)).decode().rstrip("=")
    return s[:length]
