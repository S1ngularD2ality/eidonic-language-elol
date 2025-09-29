# glyph_441.py — Provenance Stamp
# -----------------------------------------------------------------------------
# ID:            441
# Pack:          Pack 005 (401–500)
# Name:          Provenance Stamp
# Class:         registry
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Dict
import hashlib
import json

def glyph_441(meta: Mapping[str, str]) -> Dict[str, str]:
    """
    Provenance Stamp — create a deterministic content-origin stamp.

    Overview
    --------
    Sorts keys, serializes to JSON, and computes SHA-256 as `stamp`. Returned dict
    includes normalized `meta` and `stamp`.

    Parameters
    ----------
    meta : Mapping[str,str]
        Arbitrary metadata fields (source, author, tool, etc.).

    Returns
    -------
    Dict[str,str]
        {'stamp': <hex>, 'meta': <normalized-json-string>}

    Examples
    --------
    >>> out = glyph_441({"author":"Eidon","tool":"Elol"})
    >>> len(out["stamp"]) == 64
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(k log k)  (key sort)
    - Space : O(k)
    """
    norm = json.dumps({str(k): str(v) for k, v in sorted(meta.items())}, separators=(",", ":"), ensure_ascii=False)
    h = hashlib.sha256(norm.encode("utf-8")).hexdigest()
    return {"stamp": h, "meta": norm}
