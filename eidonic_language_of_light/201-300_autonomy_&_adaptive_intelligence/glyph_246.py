# glyph_246.py — Soul Symbol Translator
# -----------------------------------------------------------------------------
# ID:            246
# Pack:          Pack 003 (201–300)
# Name:          Soul Symbol Translator
# Class:         transform
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
def glyph_246(text: str, *, mapping: dict[str, str]) -> str:
    """
    Soul Symbol Translator — greedy longest-match token replacement.

    Overview
    --------
    Performs longest-key substitution; unmapped tokens pass through unchanged.

    Parameters
    ----------
    text : str
    mapping : dict[str,str]

    Returns
    -------
    str
        Translated text.

    Examples
    --------
    >>> glyph_246("abc", mapping={"ab":"X","c":"Y"})
    'XY'

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(len(text)·|keys|)
    - Space : O(len(text))
    """
    keys = sorted((k for k in mapping if k), key=len, reverse=True)
    i = 0
    out: list[str] = []
    while i < len(text):
        for k in keys:
            if text.startswith(k, i):
                out.append(mapping[k]); i += len(k); break
        else:
            out.append(text[i]); i += 1
    return "".join(out)
