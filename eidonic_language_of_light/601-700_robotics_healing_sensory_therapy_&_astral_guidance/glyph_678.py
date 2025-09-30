# glyph_678.py — BOT_RECOVERY_ASSIST
# -----------------------------------------------------------------------------
# ID:            678
# Pack:          Pack 007 (601–700)
# Name:          BOT_RECOVERY_ASSIST
# Class:         coordination_comms
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # envelope only
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import json, hashlib
from typing import Mapping, Any, Dict

def glyph_678(state: Mapping[str, Any]) -> Dict[str, Any]:
    """
    BOT_RECOVERY_ASSIST — craft a minimal recovery request envelope.

    Overview
    --------
    Canonicalizes `state` (sorted keys), embeds a compact integrity hash, and
    returns bytes payload plus human-readable summary. No I/O.

    Parameters
    ----------
    state : Mapping[str, Any]

    Returns
    -------
    {'payload': bytes, 'hash': str}

    Examples
    --------
    >>> out = glyph_678({'pose':[0,0,0],'fault':'stalled'})
    >>> isinstance(out['payload'], (bytes, bytearray))
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(1)
    """
    canon = json.dumps(dict(state), sort_keys=True, separators=(",", ":")).encode()
    h = hashlib.sha256(canon).hexdigest()
    return {"payload": b"ELoL-RCV1|" + canon, "hash": h}
