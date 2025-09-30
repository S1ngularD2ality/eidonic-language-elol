# glyph_664.py — BOT_TO_BOT_SIGNAL
# -----------------------------------------------------------------------------
# ID:            664
# Pack:          Pack 007 (601–700)
# Name:          BOT_TO_BOT_SIGNAL
# Class:         coordination_comms
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import hashlib
from typing import Mapping, Any, Dict

def glyph_664(message: Mapping[str, Any], *, channel: bytes = b"ELoL") -> Dict[str, bytes | str]:
    """
    BOT_TO_BOT_SIGNAL — create a deterministic, compact handoff token.

    Overview
    --------
    Canonicalize the dict (sorted JSON) and hash with channel label to produce
    an opaque payload for later transport (no I/O here).

    Parameters
    ----------
    message : Mapping[str, Any]
    channel : bytes, optional

    Returns
    -------
    {'label': str, 'digest': bytes}

    Examples
    --------
    >>> glyph_664({'a':1})['label']
    'ELoL'

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n) w.r.t. serialized length
    - Space : O(1)
    """
    import json
    canon = json.dumps(dict(message), sort_keys=True, separators=(",", ":")).encode()
    dig = hashlib.sha256(channel + b"|" + canon).digest()
    return {"label": channel.decode(errors="ignore") if isinstance(channel, (bytes, bytearray)) else str(channel),
            "digest": dig}
