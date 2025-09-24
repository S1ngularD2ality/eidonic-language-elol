# glyph_232.py — Recursive Symbol Unfolder
# -----------------------------------------------------------------------------
# ID:            232
# Pack:          Pack 003 (201–300)
# Name:          Recursive Symbol Unfolder
# Class:         generator
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
def glyph_232(seed: str, *, depth: int = 2, rule: str = "AB") -> str:
    """
    Recursive Symbol Unfolder — simple L-system style expansion.

    Overview
    --------
    S(0)=seed; S(d)=expand(S(d-1)), where expand does a 1-to-many map by `rule`:
    each 'A' → rule, others unchanged.

    Parameters
    ----------
    seed : str
    depth : int, optional (default: 2)
    rule : str, optional (default: "AB")

    Returns
    -------
    str
        Unfolded string.

    Examples
    --------
    >>> glyph_232("A", depth=2, rule="AB")
    'ABAB'
    """
    out = seed
    for _ in range(max(0, depth)):
        tmp = []
        for ch in out:
            tmp.append(rule if ch == "A" else ch)
        out = "".join(tmp)
    return out
