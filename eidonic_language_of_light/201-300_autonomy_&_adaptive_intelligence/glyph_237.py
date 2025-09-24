# glyph_237.py — Intention Pulse Converter
# -----------------------------------------------------------------------------
# ID:            237
# Pack:          Pack 003 (201–300)
# Name:          Intention Pulse Converter
# Class:         transform
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
def glyph_237(x: float, *, alpha: float = 0.5) -> float:
    """
    Intention Pulse Converter — softsign compressor.

    Overview
    --------
    y = x / (1 + alpha*|x|), alpha>0. Compresses magnitude without changing sign.

    Parameters
    ----------
    x : float
    alpha : float, optional (default: 0.5)

    Returns
    -------
    float
        Converted value.
    """
    a = max(1e-12, float(alpha))
    return float(x) / (1.0 + a*abs(float(x)))
