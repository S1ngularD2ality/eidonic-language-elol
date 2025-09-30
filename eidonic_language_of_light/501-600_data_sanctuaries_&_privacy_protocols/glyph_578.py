# glyph_578.py — Encrypt Database
# -----------------------------------------------------------------------------
# ID:            578
# Pack:          Pack 006 (501–600)
# Name:          Encrypt Database
# Class:         data_crypto
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # canonical JSON + seal; no DB I/O
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import json
from typing import List, Dict, Any

def glyph_578(rows: List[Dict[str, Any]], *, key: bytes, nonce: bytes) -> Dict[str, bytes]:
    """
    Encrypt Database — seal a list of row dicts (schema-agnostic).

    Overview
    --------
    Canonicalize list-of-dicts with sorted keys; seal bytes. Offline only.

    Parameters
    ----------
    rows  : List[Dict[str,Any]]
    key   : bytes
    nonce : bytes

    Returns
    -------
    Dict[str,bytes]

    Examples
    --------
    >>> env = glyph_578([{'id':1,'name':'x'}], key=b'k', nonce=b'n'); 'ct' in env
    True
    """
    raw = json.dumps([dict(r) for r in rows], sort_keys=True, separators=(",", ":")).encode()
    return glyph_501(raw, key=key, nonce=nonce)  # type: ignore
