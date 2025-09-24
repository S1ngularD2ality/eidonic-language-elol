# glyph_144.py — Light Symbol Transcoder
# -----------------------------------------------------------------------------
# ID:            144
# Pack:          Pack 002 (101–200)
# Name:          Light Symbol Transcoder
# Class:         transform
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
def glyph_144(text: str, *, mapping: dict[str, str]) -> str:
    """
    Light Symbol Transcoder — apply a simple 1-1 token map (no regex).

    Overview
    --------
    Replaces keys with values using longest-key-first greedy matching; unmapped
    characters pass through unchanged.

    Parameters
    ----------
    text : str
    mapping : dict[str, str]

    Returns
    -------
    str
        Transcoded text.

    Examples
    --------
    >>> glyph_144("ab", mapping={"a":"α","b":"β"})
    'αβ'
    """
    keys = sorted((k for k in mapping.keys() if k), key=len, reverse=True)
    i = 0; out = []
    while i < len(text):
        for k in keys:
            if text.startswith(k, i):
                out.append(mapping[k]); i += len(k); break
        else:
            out.append(text[i]); i += 1
    return "".join(out)
