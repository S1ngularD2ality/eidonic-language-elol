# glyph_492.py — Exponential Backoff
# -----------------------------------------------------------------------------
# ID:            492
# Pack:          Pack 005 (401–500)
# Name:          Exponential Backoff
# Class:         scheduler
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
def glyph_492(attempt: int, *, base_ms: float = 100.0, factor: float = 2.0, jitter: float = 0.0) -> float:
    """
    Exponential Backoff — compute delay for attempt with optional bounded jitter.

    Overview
    --------
    delay = base_ms * factor**attempt; if jitter>0, multiply by (1 - jitter) .. (1 + jitter)
    using a deterministic hash of attempt.

    Parameters
    ----------
    attempt : int
    base_ms : float, optional (default: 100.0)
    factor  : float, optional (default: 2.0)
    jitter  : float, optional (default: 0.0)

    Returns
    -------
    float : delay_ms

    Examples
    --------
    >>> glyph_492(2, base_ms=100, factor=2, jitter=0)
    400.0

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    import hashlib
    d = float(base_ms) * (float(factor) ** int(attempt))
    if jitter <= 0:
        return d
    h = hashlib.sha256(str(attempt).encode()).hexdigest()
    r = (int(h[:8], 16) / 0xFFFFFFFF) * 2.0 - 1.0  # [-1,1]
    return d * (1.0 + float(jitter) * r)
