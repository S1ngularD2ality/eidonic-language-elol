# glyph_456.py — Duty Pager
# -----------------------------------------------------------------------------
# ID:            456
# Pack:          Pack 005 (401–500)
# Name:          Duty Pager
# Class:         scheduler
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence

def glyph_456(agents: Sequence[str], *, tick: int) -> str:
    """
    Duty Pager — pick the on-call agent for a given tick (round-robin).

    Overview
    --------
    Returns agents[tick % len(agents)] or '' if no agents.

    Parameters
    ----------
    agents : Sequence[str]
    tick   : int

    Returns
    -------
    str

    Examples
    --------
    >>> glyph_456(["a","b"], tick=3)
    'b'

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    if not agents:
        return ""
    return agents[int(tick) % len(agents)]
