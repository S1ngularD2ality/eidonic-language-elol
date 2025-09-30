# glyph_513.py — Session Mask
# -----------------------------------------------------------------------------
# ID:            513
# Pack:          Pack 006 (501–600)
# Name:          Session Mask
# Class:         masking_anonymization
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # pure dict transform
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Any, Dict

def glyph_513(session: Mapping[str, Any]) -> Dict[str, Any]:
    """
    Session Mask — redact volatile identifiers to stable placeholders.

    Overview
    --------
    Replaces keys commonly considered volatile ('ip','ua','device_id') with placeholders
    if present; leaves other fields intact.

    Parameters
    ----------
    session : Mapping[str,Any]

    Returns
    -------
    Dict[str,Any]

    Examples
    --------
    >>> glyph_513({'user':'a','ip':'1.2.3.4'})['ip']
    '***'

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(k)
    - Space : O(k)
    """
    out = dict(session)
    for k in ("ip", "ua", "device_id"):
        if k in out:
            out[k] = "***"
    return out
