# glyph_217.py — Symbol Cascade Realigner
# -----------------------------------------------------------------------------
# ID:            217
# Pack:          Pack 003 (201–300)
# Name:          Symbol Cascade Realigner
# Class:         transform
# Stability:     Stable
# Version:       1.0.1
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
def glyph_217(text: str, *, mapping: dict[str, str]) -> str:
    """
    Symbol Cascade Realigner — greedy longest-key replacement (no regex).

    Overview
    --------
    Applies a 1:1 token map; unmapped characters pass through unchanged.

    Parameters
    ----------
    text : str
    mapping : dict[str, str]

    Returns
    -------
    str
        Realigned text.

    Examples
    --------
    >>> glyph_217("abca", mapping={"ab":"X","a":"Y"})
    'XcY'

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(len(text) * |keys|)
    - Space : O(len(text))
    """
    keys = sorted((k for k in mapping.keys() if k), key=len, reverse=True)
    i = 0
    out: list[str] = []
    while i < len(text):
        for k in keys:
            if text.startswith(k, i):
                out.append(mapping[k]); i += len(k); break
        else:
            out.append(text[i]); i += 1
    return "".join(out)
