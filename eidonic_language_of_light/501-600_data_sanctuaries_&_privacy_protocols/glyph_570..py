# glyph_570.py — Blockchain Log
# -----------------------------------------------------------------------------
# ID:            570
# Pack:          Pack 006 (501–600)
# Name:          Blockchain Log
# Class:         logging_auditing
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # hash chaining; no I/O, no network
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import json, hashlib
from typing import List, Mapping, Any, Dict

def glyph_570(entries: List[Mapping[str, Any]], *, genesis: str = "ELoL") -> Dict[str, Any]:
    """
    Blockchain Log — build a simple hash-chained ledger from entries.

    Overview
    --------
    Canonicalize each entry and create blocks with prev_hash → hash linkage.
    Returns last hash and the full chain (for audit export).

    Parameters
    ----------
    entries : List[Mapping[str,Any]]
    genesis : str, optional

    Returns
    -------
    Dict[str,Any] : {'tip': str, 'chain': List[Dict[str,str]]}

    Examples
    --------
    >>> out = glyph_570([{'a':1},{'b':2}]); len(out['chain']) == 2
    True
    """
    prev = hashlib.sha256(genesis.encode()).hexdigest()
    chain: List[Dict[str, str]] = []
    for e in entries:
        raw = json.dumps(dict(e), sort_keys=True, separators=(",", ":")).encode()
        cur = hashlib.sha256(prev.encode() + raw).hexdigest()
        chain.append({"prev": prev, "hash": cur})
        prev = cur
    return {"tip": prev, "chain": chain}
