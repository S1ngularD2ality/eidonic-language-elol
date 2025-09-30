# glyph_653.py — ASSISTIVE_TOOL_SWAP
# -----------------------------------------------------------------------------
# ID:            653
# Pack:          Pack 007 (601–700)
# Name:          ASSISTIVE_TOOL_SWAP
# Class:         coordination_comms
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # scoring only
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Mapping, Any, Tuple, List

def glyph_653(tools: Sequence[Mapping[str, Any]], task: Mapping[str, Any]) -> Tuple[str, float]:
    """
    ASSISTIVE_TOOL_SWAP — choose best tool for the task with gentle bias.

    Overview
    --------
    Score = fit*0.6 + availability*0.3 + fragility_care*0.1 (all 0..1).

    Parameters
    ----------
    tools : Sequence[{'id':str,'fit':float,'availability':float,'fragility_care':float}]
    task  : Mapping[str, Any]  # unused placeholder for future expansion

    Returns
    -------
    (tool_id, score)

    Examples
    --------
    >>> glyph_653([{'id':'soft','fit':0.9,'availability':1.0,'fragility_care':1.0}], {})[0]
    'soft'

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(1)
    """
    best = ("", -1.0)
    for t in tools:
        sc = 0.6*float(t.get("fit", 0.0)) + 0.3*float(t.get("availability", 0.0)) + 0.1*float(t.get("fragility_care", 0.0))
        tid = str(t.get("id", ""))
        if sc > best[1]:
            best = (tid, sc)
    return best
