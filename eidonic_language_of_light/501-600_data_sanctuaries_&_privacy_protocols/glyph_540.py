# glyph_540.py — Decrypt Config
# -----------------------------------------------------------------------------
# ID:            540
# Pack:          Pack 006 (501–600)
# Name:          Decrypt Config
# Class:         config_crypto
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # unwrap + parse JSON
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import json
from typing import Mapping, Any

def glyph_540(sealed: Mapping[str, bytes], *, key: bytes) -> Mapping[str, Any]:
    """
    Decrypt Config — unseal and parse a configuration blob.

    Overview
    --------
    Authenticates with tag, decrypts deterministically, returns dict.

    Parameters
    ----------
    sealed : Mapping[str,bytes]
    key    : bytes

    Returns
    -------
    Mapping[str,Any]

    Examples
    --------
    >>> s = glyph_539({'x':1}, key=b'k', nonce=b'n')
    >>> glyph_540(s, key=b'k')['x']
    1

    Exceptions
    ----------
    - ValueError : if authentication fails.

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    raw = glyph_502(dict(sealed), key=key)  # type: ignore
    return json.loads(raw.decode())
