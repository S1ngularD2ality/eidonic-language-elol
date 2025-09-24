# glyph_279.py — Dream Gate Enhancer
# -----------------------------------------------------------------------------
# ID:            279
# Pack:          Pack 003 (201–300)
# Original Name: Dream Gate Enhancer
# Manifest Name: Dream Gate Enhancer
# Class:         filter
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       Apache-2.0
# -----------------------------------------------------------------------------
def glyph_279(seq: list[float], *, gain: float = 1.2) -> list[float]:
    """
    Dream Gate Enhancer — amplify signal by a scalar gain.

    Overview
    --------
    Multiplies all values by `gain`; preserves shape and determinism.

    Parameters
    ----------
    seq : list[float]
    gain : float, optional (default: 1.2)

    Returns
    -------
    list[float]
        Enhanced signal.

    Examples
    --------
    >>> glyph_279([0.5, -1.0], gain=3.0)
    [1.5, -3.0]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    g = float(gain)
    return [float(v)*g for v in seq]
