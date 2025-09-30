# glyph_553.py — Encrypt List
# -----------------------------------------------------------------------------
# ID:            553
# Pack:          Pack 006 (501–600)
# Name:          Encrypt List
# Class:         transform
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import json, hashlib, hmac
from typing import List, Any, Tuple

def glyph_553(items: List[Any], *, key: bytes) -> Tuple[bytes, str]:
    """
    Encrypt List — canonical JSON, XOR stream, and HMAC for arrays.

    Overview
    --------
    Same construction as `glyph_547`, specialized for JSON arrays.

    Parameters
    ----------
    items : List[Any]
        JSON-serializable list.
    key : bytes
        Secret key.

    Returns
    -------
    (bytes, str)
        Ciphertext and MAC hex.

    Examples
    --------
    >>> c, m = glyph_553([1,2,3], key=b"k")
    >>> glyph_554(c, key=b"k", mac=m)
    [1, 2, 3]
    """
    data = json.dumps(items, sort_keys=True, separators=(",", ":")).encode("utf-8")
    stream = hashlib.sha256(key).digest()
    out = bytearray(data)
    for i in range(len(out)):
        out[i] ^= stream[i % len(stream)]
    mac = hmac.new(key, bytes(out), hashlib.sha256).hexdigest()
    return bytes(out), mac
