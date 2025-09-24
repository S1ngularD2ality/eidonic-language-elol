# glyph_037.py — Harmonic Memory Balancer
# -----------------------------------------------------------------------------
# ID:            037
# Pack:          Pack 001 (000–100)
# Name:          Harmonic Memory Balancer
# Class:         transform
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
def glyph_037(values: list[float]) -> list[float]:
    """
    Harmonic Memory Balancer — center and scale to unit variance.

    Overview
    --------
    Applies y = (x - mean)/std with std fallback to 1 to avoid division by zero.

    Parameters
    ----------
    values : list[float]

    Returns
    -------
    list[float]
        Normalized values.
    """
    n=len(values)
    if n==0: return []
    m=sum(values)/n
    var=sum((v-m)**2 for v in values)/n
    s=(var**0.5) or 1.0
    return [(v-m)/s for v in values]
