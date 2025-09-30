# glyph_545.py — Data Fingerprint
# -----------------------------------------------------------------------------
# ID:            545
# Pack:          Pack 006 (501–600)
# Name:          Data Fingerprint
# Class:         analyzer
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import hashlib, json
from typing import Any

def glyph_545(obj: Any) -> str:
    """
    Data Fingerprint — canonicalize then hash with SHA-256.

    Overview
    --------
    Converts Python primitives (str, bytes, int, float, bool, None, list, dict) into a
    **canonical JSON** form (sorted keys, compact separators), then returns the
    SHA-256 hex digest.

    Parameters
    ----------
    obj : Any
        Supported primitive/container types.

    Returns
    -------
    str
        64-char lowercase hex digest.

    Examples
    --------
    >>> glyph_545({"b":1,"a":2}) == glyph_545({"a":2,"b":1})
    True

    Exceptions
    ----------
    - TypeError : if an unsupported type is encountered.

    Complexity
    ----------
    - Time  : O(N)
    - Space : O(N)
    """
    if isinstance(obj, bytes):
        data = obj
    else:
        try:
            data = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode("utf-8")
        except TypeError as e:
            raise TypeError("unsupported type for canonical hashing") from e
    return hashlib.sha256(data).hexdigest()
