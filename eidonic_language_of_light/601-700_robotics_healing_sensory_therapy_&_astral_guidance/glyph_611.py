# glyph_611.py — SENSOR_FUSION_MAP
# -----------------------------------------------------------------------------
# ID:            611
# Pack:          Pack 007 (601–700)
# Name:          SENSOR_FUSION_MAP
# Class:         coordination_comms
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # weighted merge; no devices
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_611(grids: Sequence[Sequence[Sequence[float]]],
              weights: Sequence[float]) -> List[List[float]]:
    """
    SENSOR_FUSION_MAP — normalize weights and blend scalar grids cell-wise.

    Returns
    -------
    List[List[float]]
    """
    if not grids:
        return []
    H = len(grids[0]); W = len(grids[0][0]) if H else 0
    wsum = sum(max(0.0, w) for w in weights) or 1.0
    norm = [max(0.0, w)/wsum for w in weights]
    out = [[0.0]*W for _ in range(H)]
    for g, w in zip(grids, norm):
        for r in range(H):
            for c in range(W):
                out[r][c] += float(g[r][c]) * w
    return out
