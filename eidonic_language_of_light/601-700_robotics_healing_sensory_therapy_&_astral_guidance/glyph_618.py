# glyph_618.py — TASK_PRIORITY_MANAGER
# -----------------------------------------------------------------------------
# ID:            618
# Pack:          Pack 007 (601–700)
# Name:          TASK_PRIORITY_MANAGER
# Class:         coordination_comms
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # weighted priority; no scheduler I/O
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Mapping, Any, List, Tuple

def glyph_618(tasks: Sequence[Mapping[str, Any]]) -> List[Tuple[str, float]]:
    """
    TASK_PRIORITY_MANAGER — compute scores and return sorted plan.

    Parameters
    ----------
    tasks : each item may have: {'id': str, 'urgency': float, 'importance': float}

    Returns
    -------
    List[Tuple[str,float]]  # (id, score), highest first
    """
    scored = []
    for t in tasks:
        u = float(t.get("urgency", 0.0)); im = float(t.get("importance", 0.0))
        scored.append((str(t.get("id","")), 0.6*u + 0.4*im))
    return sorted(scored, key=lambda x: x[1], reverse=True)
