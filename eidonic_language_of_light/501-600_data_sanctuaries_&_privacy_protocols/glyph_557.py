# glyph_557.py — Secure Broadcast
# -----------------------------------------------------------------------------
# ID:            557
# Pack:          Pack 006 (501–600)
# Name:          Secure Broadcast
# Class:         container
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import hashlib, hmac
from typing import Dict, List

def glyph_557(payload: bytes, recipients: Dict[str, bytes]) -> List[Dict[str, str | int]]:
    """
    Secure Broadcast — per-recipient sealed envelopes (no network).

    Overview
    --------
    For each recipient id → key, builds an envelope with size, sha256, and HMAC over
    `(recipient_id || payload)`. No I/O; returns the list of envelopes.

    Parameters
    ----------
    payload : bytes
        Bytes to “broadcast”.
    recipients : Dict[str, bytes]
        Mapping of recipient id → shared key.

    Returns
    -------
    List[Dict[str, str | int]]
        One envelope per recipient.

    Examples
    --------
    >>> envs = glyph_557(b"x", {"a":b"k"})
    >>> envs[0]["recipient"]
    'a'
    """
    envs = []
    for rid, key in sorted(recipients.items()):
        mac = hmac.new(key, rid.encode("utf-8") + payload, hashlib.sha256).hexdigest()
        envs.append({
            "recipient": rid,
            "size": len(payload),
            "sha256": hashlib.sha256(payload).hexdigest(),
            "hmac": mac,
        })
    return envs
