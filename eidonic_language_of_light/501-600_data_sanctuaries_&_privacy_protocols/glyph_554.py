# glyph_554.py — Decrypt List
# -----------------------------------------------------------------------------
# ID:            554
# Pack:          Pack 006 (501–600)
# Name:          Decrypt List
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
from typing import List, Any

def glyph_554(cipher: bytes, *, key: bytes, mac: str) -> List[Any]:
    """
    Decrypt List — verify and restore an encrypted JSON array.

    Overview
    --------
    Validates MAC then inverts the XOR stream to decode the list.

    Parameters
    ----------
    cipher : bytes
        Encrypted payload from `glyph_553`.
    key : bytes
        Secret key.
    mac : str
        Expected MAC hex.

    Returns
    -------
    List[Any]
        Restored array.

    Examples
    --------
    >>> c, m = glyph_553(["a","b"], key=b"k")
    >>> glyph_554(c, key=b"k", mac=m)
    ['a', 'b']
    """
    if hmac.new(key, cipher, hashlib.sha256).hexdigest() != mac:
        raise ValueError("MAC verification failed")
    stream = hashlib.sha256(key).digest()
    out = bytearray(cipher)
    for i in range(len(out)):
        out[i] ^= stream[i % len(stream)]
    return json.loads(out.decode("utf-8"))
