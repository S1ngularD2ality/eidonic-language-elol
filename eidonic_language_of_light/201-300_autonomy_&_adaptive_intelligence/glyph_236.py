# glyph_236.py — Temporal Grid Amplifier
# -----------------------------------------------------------------------------
# ID:            236
# Pack:          Pack 003 (201–300)
# Name:          Temporal Grid Amplifier
# Class:         transform
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_236(field: Sequence[Sequence[float]], *, gain: float = 1.5) -> List[List[float]]:
    """
    Temporal Grid Amplifier — scalar gain on 2D field.

    Overview
    --------
    Multiplies every cell by `gain`; deterministic and shape-preserving.

    Parameters
    ----------
    field : Sequence[Sequence[float]]
    gain : float, optional (default: 1.5)

    Returns
    -------
    List[List[float]]
        Amplified field.
    """
    g = float(gain)
    return [[float(v)*g for v in row] for row in field]
