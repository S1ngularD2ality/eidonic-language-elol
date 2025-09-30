# glyph_530.py — Obfuscate Data
# -----------------------------------------------------------------------------
# ID:            530
# Pack:          Pack 006 (501–600)
# Name:          Obfuscate Data
# Class:         privacy_transform
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # keyed HMAC labels
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import hmac, hashlib
from typing import Mapping, Any, Dict

def glyph_530(record: Mapping[str, Any], *, salt: bytes) -> Dict[str, Any]:
    """
    Obfuscate Data — keyed hash of string values (format-preserving hint).

    Overview
    --------
    For string values, replace with 8-hex prefix of HMAC(salt, key||value), keeping
    leading character for readability; passthrough non-strings.

    Parameters
    ----------
    record : Mapping[str,Any]
    salt   : bytes

    Returns
    -------
    Dict[str,Any]

    Examples
    --------
    >>> glyph_530({'email':'a@example.com','age':9}, salt=b's')['email'].startswith('a…')
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(k)
    - Space : O(k)
    """
    out: Dict[str, Any] = {}
    for k, v in record.items():
        if isinstance(v, str):
            tag = hmac.new(salt, (str(k)+":"+v).encode(), hashlib.sha256).hexdigest()[:8]
            out[k] = f"{v[:1]}…{tag}"
        else:
            out[k] = v
    return out
