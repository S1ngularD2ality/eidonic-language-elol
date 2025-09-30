# glyph_549.py — Access Alert
# -----------------------------------------------------------------------------
# ID:            549
# Pack:          Pack 006 (501–600)
# Name:          Access Alert
# Class:         analyzer
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Dict, Any

def glyph_549(subject: str, resource: str, decision: str, *, policy_id: str = "default") -> Dict[str, Any]:
    """
    Access Alert — create a tamper-evident alert record when policy denies.

    Overview
    --------
    Emits a normalized alert dict (subject, resource, decision, policy) plus a
    SHA-256 of the canonical record to allow downstream attestation.

    Parameters
    ----------
    subject : str
        Actor/user identifier.
    resource : str
        Target of access.
    decision : str
        "allow" or "deny".
    policy_id : str, optional (default: ``"default"``)
        Policy identifier.

    Returns
    -------
    Dict[str, Any]
        The alert record (includes "hash" field).

    Examples
    --------
    >>> rec = glyph_549("alice", "/admin", "deny")
    >>> "hash" in rec
    True
    """
    import json, hashlib
    rec = {
        "type": "AccessAlert",
        "subject": subject,
        "resource": resource,
        "decision": decision.lower(),
        "policy": policy_id,
    }
    s = json.dumps(rec, sort_keys=True, separators=(",", ":")).encode("utf-8")
    rec["hash"] = hashlib.sha256(s).hexdigest()
    return rec
