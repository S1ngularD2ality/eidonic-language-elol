# glyph_490.py — Mesh Envelope
# -----------------------------------------------------------------------------
# ID:            490
# Pack:          Pack 005 (401–500)
# Name:          Mesh Envelope
# Class:         packer
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import json
from typing import Mapping, Any, Dict

def glyph_490(meta: Mapping[str, Any], body: Mapping[str, Any]) -> Dict[str, Any]:
    """
    Mesh Envelope — deterministic envelope {'meta':..,'body':..,'digest':..}.

    Overview
    --------
    Digest is SHA-256 of canonical JSON of {'meta':meta,'body':body}.

    Parameters
    ----------
    meta : Mapping[str,Any]
    body : Mapping[str,Any]

    Returns
    -------
    Dict[str,Any]

    Examples
    --------
    >>> glyph_490({'a':1},{'b':2})['digest'][:6].isalnum()
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n log n)
    - Space : O(n)
    """
    import hashlib
    payload = {"meta": dict(meta), "body": dict(body)}
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), default=str).encode("utf-8")
    return {"meta": payload["meta"], "body": payload["body"], "digest": hashlib.sha256(raw).hexdigest()}
