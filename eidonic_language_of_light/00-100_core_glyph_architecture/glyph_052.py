# glyph_052.py — Mirror Cascade Projector
# -----------------------------------------------------------------------------
# ID:            052
# Pack:          Pack 001 (000–100)
# Name:          Mirror Cascade Projector
# Class:         transform
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, List, Sequence

def glyph_052(text: str, rules: Sequence[Mapping[str, str]]) -> str:
    """
    Mirror Cascade Projector — apply a sequence of symmetric mirror maps.

    Overview
    --------
    For each mapping in `rules`, enforce involutive symmetry (if a→b but b→a missing,
    add it), then rewrite `text` using longest-first matching for multi-char keys,
    falling back to char-wise mirroring.

    Parameters
    ----------
    text : str
        Input text to transform.
    rules : Sequence[Mapping[str, str]]
        One or more mapping dictionaries.

    Returns
    -------
    str
        Transformed text.

    Examples
    --------
    >>> glyph_052("<ab>", [{"<": ">", ">": "<"}, {"ab": "ba"}])
    "><ba<"

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(K·|text|·log M)  (K maps; M keys per map; longest-first scan)
    - Space : O(|text| + M)
    """
    out = text
    for pairs in rules:
        sym = dict(pairs)
        for k, v in list(sym.items()):
            if sym.get(v) != k:
                sym[v] = k
        keys = sorted(sym.keys(), key=len, reverse=True)
        i = 0
        buf: List[str] = []
        while i < len(out):
            for k in keys:
                if k and out.startswith(k, i):
                    buf.append(sym[k])
                    i += len(k)
                    break
            else:
                ch = out[i]
                buf.append(sym.get(ch, ch))
                i += 1
        out = "".join(buf)
    return out
