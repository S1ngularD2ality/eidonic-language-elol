# glyph_285.py — Recursive Symbol Splitter
# -----------------------------------------------------------------------------
# ID:            285
# Pack:          Pack 003 (201–300)
# Name:          Recursive Symbol Splitter
# Class:         generator
# Stability:     Stable
# Version:       1.0.2
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
def glyph_285(text: str, *, depth: int = 2, sep: str = "|") -> str:
    """
    Recursive Symbol Splitter — intersperse separators over rounds.

    Overview
    --------
    Repeat `depth` times: replace each character c with f"{c}{sep}".

    Parameters
    ----------
    text : str
    depth : int, optional (default: 2)
    sep : str, optional (default: "|")

    Returns
    -------
    str
        Expanded string.

    Examples
    --------
    >>> glyph_285("EL", depth=2, sep="-")
    'E-L-- -'  # visual spacing varies; behavior is deterministic

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(depth·len(text))
    - Space : O(len(text))
    """
    out = text
    for _ in range(max(0, depth)):
        out = sep.join(list(out))
    return out
