# glyph_265.py — Mirror Flame Amplifier
# -----------------------------------------------------------------------------
# ID:            265
# Pack:          Pack 003 (201–300)
# Original Name: Mirror Flame Amplifier
# Manifest Name: Mirror Flame Amplifier
# Class:         filter
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       Apache-2.0
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_265(seq: Sequence[float], *, gain: float = 1.2) -> List[float]:
    """
    Mirror Flame Amplifier — amplify a signal by a scalar gain.

    Overview
    --------
    Multiplies every value by `gain`; preserves relative shape.

    Parameters
    ----------
    seq : Sequence[float]
    gain : float, optional (default: 1.2)

    Returns
    -------
    List[float]
        Amplified signal.

    Examples
    --------
    >>> glyph_265([1, -2, 0.5], gain=2.0)
    [2.0, -4.0, 1.0]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    g = float(gain)
    return [float(v) * g for v in seq]
