# glyph_607.py — OBSTACLE_CLASSIFICATION
# -----------------------------------------------------------------------------
# ID:            607
# Pack:          Pack 007 (601–700)
# Name:          OBSTACLE_CLASSIFICATION
# Class:         navigation_safety
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # geometry-only, no CV dependency
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Tuple, Dict, Any

def glyph_607(points: Sequence[Tuple[float,float]], *,
              size_thresh_m: float = 0.3) -> Dict[str, Any]:
    """
    OBSTACLE_CLASSIFICATION — coarse type: 'small' vs 'large' clusters.

    Overview
    --------
    Treats each point as an obstacle; computes bounding box and labels by
    size threshold. Purely illustrative and deterministic.

    Returns
    -------
    {'bbox': ((minx,miny),(maxx,maxy)), 'label': 'small'|'large', 'count': int}
    """
    if not points:
        return {"bbox": ((0.0,0.0),(0.0,0.0)), "label":"small", "count":0}
    xs = [p[0] for p in points]; ys = [p[1] for p in points]
    w = (max(xs) - min(xs)); h = (max(ys) - min(ys))
    label = "large" if max(w, h) >= size_thresh_m else "small"
    return {"bbox": ((min(xs), min(ys)), (max(xs), max(ys))), "label": label, "count": len(points)}
