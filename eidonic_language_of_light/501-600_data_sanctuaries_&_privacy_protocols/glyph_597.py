# glyph_597.py — Secure Auth Chain
# -----------------------------------------------------------------------------
# ID:            597
# Pack:          Pack 006 (501–600)
# Name:          Secure Auth Chain
# Class:         logging_auditing
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # hash-chained attest; no I/O
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import json, hashlib, hmac
from typing import List, Mapping, Any, Dict

def glyph_597(steps: List[Mapping[str, Any]], *, mac_key: bytes, genesis: str = "ELoL-AUTH") -> Dict[str, Any]:
    """
    Secure Auth Chain — build an authenticated, hash-linked sign-in trail.

    Overview
    --------
    Canonicalize each step, chain hashes with a genesis, and attach per-step HMACs.

    Returns
    -------
    {'tip': str, 'chain': List[{'hash':str,'prev':str,'mac':str}]}
    """
    prev = hashlib.sha256(genesis.encode()).hexdigest()
    chain: List[Dict[str, str]] = []
    for s in steps:
        raw = json.dumps(dict(s), sort_keys=True, separators=(",", ":")).encode()
        cur = hashlib.sha256(prev.encode() + raw).hexdigest()
        mac = hmac.new(mac_key, raw + cur.encode(), hashlib.sha256).hexdigest()
        chain.append({"prev": prev, "hash": cur, "mac": mac})
        prev = cur
    return {"tip": prev, "chain": chain}
