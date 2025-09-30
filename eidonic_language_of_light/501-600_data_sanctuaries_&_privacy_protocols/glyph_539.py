# glyph_539.py — Encrypt Config
# -----------------------------------------------------------------------------
# ID:            539
# Pack:          Pack 006 (501–600)
# Name:          Encrypt Config
# Class:         config_crypto
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # canonical JSON + seal
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import json
from typing import Mapping, Any, Dict

def glyph_539(cfg: Mapping[str, Any], *, key: bytes, nonce: bytes) -> Dict[str, bytes]:
    """
    Encrypt Config — seal canonical JSON configuration.

    Overview
    --------
    Canonical JSON → bytes → deterministic seal.

    Parameters
    ----------
    cfg   : Mapping[str,Any]
    key   : bytes
    nonce : bytes

    Returns
    -------
    Dict[str,bytes] : {'nonce','ct','tag'}

    Examples
    --------
    >>> env = glyph_539({'a':1}, key=b'k', nonce=b'n')
    >>> set(env).issuperset({'ct','tag','nonce'})
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n log n)
    - Space : O(n)
    """
    raw = json.dumps(dict(cfg), sort_keys=True, separators=(",", ":")).encode()
    return glyph_501(raw, key=key, nonce=nonce)  # type: ignore
