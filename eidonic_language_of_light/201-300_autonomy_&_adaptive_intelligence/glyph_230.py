# glyph_230.py — Subconscious Flow Disruptor
# -----------------------------------------------------------------------------
# ID:            230
# Pack:          Pack 003 (201–300)
# Name:          Subconscious Flow Disruptor
# Class:         filter
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
def glyph_230(x: float, *, jitter: float = 0.1) -> float:
    """
    Subconscious Flow Disruptor — deterministic micro-jitter.

    Overview
    --------
    Adds a tiny, sign-alternating offset based on a fixed hash of the value index.
    (Stateless, pseudo-random but deterministic given inputs.)

    Parameters
    ----------
    x : float
    jitter : float, optional (default: 0.1)

    Returns
    -------
    float
        Disrupted value.

    Examples
    --------
    >>> glyph_230(1.0, jitter=0.5)
    1.5
    """
    j = float(jitter)
    # simple deterministic flip by value parity
    return float(x) + (j if int(abs(x)*1e6) % 2 == 0 else -j)
