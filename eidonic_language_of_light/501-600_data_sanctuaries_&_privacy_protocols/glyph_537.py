# glyph_537.py — Secure Token Rotate
# -----------------------------------------------------------------------------
# ID:            537
# Pack:          Pack 006 (501–600)
# Name:          Secure Token Rotate
# Class:         token_management
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # canonical JSON + deterministic seal
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import json
from typing import Mapping, Any, Dict

def glyph_537(claims: Mapping[str, Any], *, key: bytes, nonce: bytes) -> Dict[str, Any]:
    """
    Secure Token Rotate — issue a new sealed token from claims.

    Overview
    --------
    Canonicalize claims, seal bytes via `Data Seal` semantics.

    Parameters
    ----------
    claims : Mapping[str,Any]
    key    : bytes
    nonce  : bytes

    Returns
    -------
    Dict[str,Any] : {'claims': claims, 'sealed': {...}}

    Examples
    --------
    >>> out = glyph_537({'sub':'a'}, key=b'k', nonce=b'n')
    >>> 'sealed' in out and 'claims' in out
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n log n)
    - Space : O(n)
    """
    raw = json.dumps(dict(claims), sort_keys=True, separators=(",", ":")).encode()
    sealed = glyph_501(raw, key=key, nonce=nonce)  # type: ignore
    return {"claims": dict(claims), "sealed": sealed}
