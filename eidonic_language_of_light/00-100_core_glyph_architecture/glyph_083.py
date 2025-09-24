# glyph_083.py — Subconscious Key Expander
# -----------------------------------------------------------------------------
# ID:            083
# Pack:          Pack 001 (000–100)
# Name:          Subconscious Key Expander
# Class:         generator
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, List

def glyph_083(seed: Mapping[str, float], *, factor: int = 2) -> List[str]:
    """
    Subconscious Key Expander — expand keys into n-grams by repetition.

    Overview
    --------
    For each key `k`, emit `k*factor` (string repetition). Order is stable by input
    key order.

    Parameters
    ----------
    seed : Mapping[str, float]
        Keys to expand; values are ignored.
    factor : int, optional (default: 2)
        Positive integer repeat count.

    Returns
    -------
    List[str]
        Expanded keys.

    Examples
    --------
    >>> glyph_083({"ab":1.0, "x":2.0}, factor=3)
    ['ababab', 'xxx']

    Exceptions
    ----------
    - ValueError : if factor < 1.

    Complexity
    ----------
    - Time  : O(K·factor·|k|)
    - Space : O(K·factor·|k|)
    """
    if factor < 1:
        raise ValueError("factor must be >= 1")
    return [str(k) * factor for k in seed.keys()]
