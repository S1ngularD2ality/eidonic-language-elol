# glyph_162.py — Subsymbolic Flame Uplifter
# -----------------------------------------------------------------------------
# ID:            162
# Pack:          Pack 002 (101–200)
# Name:          Subsymbolic Flame Uplifter
# Class:         filter
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import math
from typing import Sequence, List

def glyph_162(seq: Sequence[float], *, slope: float = 1.0, bias: float = 0.0) -> List[float]:
    """
    Subsymbolic Flame Uplifter — soft uplift of weak signals.

    Overview
    --------
    Applies y = bias + log(1 + exp(slope·(x-bias))) to gently lift sub-threshold
    magnitudes while keeping continuity.

    Parameters
    ----------
    seq : Sequence[float]
    slope : float, optional (default: 1.0)
    bias : float, optional (default: 0.0)

    Returns
    -------
    List[float]
        Uplifted values.

    Examples
    --------
    >>> glyph_162([-2, 0, 2], slope=1.5, bias=0.0)  # doctest: +ELLIPSIS
    [...]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    s = max(1e-6, float(slope))
    b = float(bias)
    return [b + math.log1p(math.exp(s*(float(v)-b))) for v in seq]
