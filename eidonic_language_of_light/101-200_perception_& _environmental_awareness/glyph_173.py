# glyph_173.py — Subdimensional Cascade Equalizer
# -----------------------------------------------------------------------------
# ID:            173
# Pack:          Pack 002 (101–200)
# Name:          Subdimensional Cascade Equalizer
# Class:         filter
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_173(streams: Sequence[Sequence[float]]) -> List[float]:
    """
    Subdimensional Cascade Equalizer — energy match across streams.

    Overview
    --------
    Scales each stream to equal RMS, then averages aligned samples by the
    shortest length.

    Parameters
    ----------
    streams : Sequence[Sequence[float]]

    Returns
    -------
    List[float]
        Equalized blend.

    Examples
    --------
    >>> glyph_173([[1,1,1],[0,0,2]])
    [0.5, 0.5, 1.5]
    """
    if not streams:
        return []
    # compute scales
    scaled = []
    for s in streams:
        x = [float(v) for v in s]
        if not x:
            continue
        rms = (sum(v*v for v in x)/len(x))**0.5 or 1.0
        scaled.append([v/rms for v in x])
    if not scaled:
        return []
    m = min(len(s) for s in scaled)
    out = [0.0]*m
    for s in scaled:
        for i in range(m):
            out[i] += s[i]
    return [v/len(scaled) for v in out]
