# glyph_547.py — Encrypt Dict
# -----------------------------------------------------------------------------
# ID:            547
# Pack:          Pack 006 (501–600)
# Name:          Encrypt Dict
# Class:         transform
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import json, hashlib, hmac, base64
from typing import Dict, Any, Tuple

def glyph_547(doc: Dict[str, Any], *, key: bytes) -> Tuple[bytes, str]:
    """
    Encrypt Dict — deterministic JSON pack + XOR stream + HMAC.

    Overview
    --------
    Serializes a dict to canonical JSON, applies SHA-256-derived XOR stream, and
    returns `(ciphertext, mac_hex)`. Use `glyph_548` to reverse and verify.

    Parameters
    ----------
    doc : Dict[str, Any]
        JSON-serializable mapping.
    key : bytes
        Secret key for stream derivation and MAC.

    Returns
    -------
    (bytes, str)
        Ciphertext bytes and HMAC-SHA256 hex over ciphertext.

    Examples
    --------
    >>> c, mac = glyph_547({"x":1}, key=b"k")
    >>> glyph_548(c, key=b"k", mac=mac) == {"x":1}
    True

    Exceptions
    ----------
    - TypeError : if doc is not JSON-serializable.

    Complexity
    ----------
    - Time  : O(N)
    - Space : O(N)
    """
    data = json.dumps(doc, sort_keys=True, separators=(",", ":")).encode("utf-8")
    stream = hashlib.sha256(key).digest()
    out = bytearray(data)
    for i in range(len(out)):
        out[i] ^= stream[i % len(stream)]
    mac = hmac.new(key, bytes(out), hashlib.sha256).hexdigest()
    return bytes(out), mac
