# glyph_274.py — Recursive Thoughtform Shifter
# -----------------------------------------------------------------------------
# ID:            274
# Pack:          Pack 003 (201–300)
# Original Name: Recursive Thoughtform Shifter
# Manifest Name: Recursive Thoughtform Shifter
# Class:         transform
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       Apache-2.0
# -----------------------------------------------------------------------------
def glyph_274(seq: list[float], *, window: int = 3) -> list[float]:
    """
    Recursive Thoughtform Shifter — moving average with reflection edges.

    Overview
    --------
    Applies an odd-length mean filter; preserves length and determinism.

    Parameters
    ----------
    seq : list[float]
    window : int, optional (default: 3)

    Returns
    -------
    list[float]
        Shifted (smoothed) signal.

    Examples
    --------
    >>> glyph_274([0, 1, 0, 1, 0], window=3)
    [~0.33, ~0.67, ~0.67, ~0.67, ~0.33]  # approximate

    Exceptions
    ----------
    - ValueError : if `window` is not odd or < 1.

    Complexity
    ----------
    - Time  : O(window·n)
    - Space : O(n)
    """
    if window < 1 or window % 2 == 0:
        raise ValueError("window must be odd and >=1")
    n = len(seq)
    if n == 0: 
        return []
    k = window // 2
    pad = seq[k:0:-1] + seq + seq[-2:-k-2:-1] if n > 1 else seq * (2*k + 1)
    out = []
    for i in range(n):
        out.append(sum(float(pad[i+j]) for j in range(window)) / window)
    return out
