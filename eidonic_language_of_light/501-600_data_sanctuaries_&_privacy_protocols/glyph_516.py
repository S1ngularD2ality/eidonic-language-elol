# glyph_516.py — Log Purge
# -----------------------------------------------------------------------------
# ID:            516
# Pack:          Pack 006 (501–600)
# Name:          Log Purge
# Class:         fs_destruction (logical)
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True  # returns plan; no destructive I/O
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Dict, Any

def glyph_516(paths: Sequence[str], *, confirm: bool) -> Dict[str, Any]:
    """
    Log Purge — produce a deterministic purge plan (no disk writes).

    Overview
    --------
    Returns {'plan':[{'path':p,'action':'delete'}...], 'execute': confirm}.

    Parameters
    ----------
    paths   : Sequence[str]
    confirm : bool

    Returns
    -------
    Dict[str,Any]

    Examples
    --------
    >>> glyph_516(['/a','/b'], confirm=False)['execute']
    False

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    plan = [{"path": p, "action": "delete"} for p in paths]
    return {"plan": plan, "execute": bool(confirm)}
