# glyph_160.py — Soul Key Converter
# -----------------------------------------------------------------------------
# ID:            160
# Pack:          Pack 002 (101–200)
# Name:          Soul Key Converter
# Class:         transform
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
def glyph_160(key: str, *, base: str = "0123456789ABCDEF", target: str = "0123456789") -> str:
    """
    Soul Key Converter — convert a key's digits between custom alphabets.

    Overview
    --------
    Treats `key` as a string of symbols in `base` and maps each symbol by position
    into `target` (lengths may differ). Unknown symbols pass through unchanged.

    Parameters
    ----------
    key : str
    base : str, optional (default: hexadecimal alphabet)
    target : str, optional (default: decimal alphabet)

    Returns
    -------
    str
        Converted key.

    Examples
    --------
    >>> glyph_160("FACE", base="ABCDEF", target="abcdef")
    'face'
    """
    table = {b: target[i % len(target)] for i, b in enumerate(base)}
    return "".join(table.get(ch, ch) for ch in key)
