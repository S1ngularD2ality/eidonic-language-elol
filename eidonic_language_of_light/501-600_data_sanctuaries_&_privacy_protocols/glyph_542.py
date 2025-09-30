# glyph_542.py — Intrusion Pattern
# -----------------------------------------------------------------------------
# ID:            542
# Pack:          Pack 006 (501–600)
# Name:          Intrusion Pattern
# Class:         analyzer
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Dict, Any
from collections import Counter

def glyph_542(events: Sequence[str], *, ngram: int = 3, topk: int = 5) -> Dict[str, Any]:
    """
    Intrusion Pattern — detect repetitive n-gram motifs in event streams.

    Overview
    --------
    Computes frequency of contiguous n-grams (default 3) across an event sequence and
    returns the top motifs plus a **rarity score** per event (inverse frequency of its n-grams).
    Useful for surfacing suspicious bursts, scans, or credential-stuffing loops.

    Parameters
    ----------
    events : Sequence[str]
        Normalized event tokens (e.g., "LOGIN_FAIL", "GET_/admin").
    ngram : int, optional (default: ``3``)
        Contiguous window size.
    topk : int, optional (default: ``5``)
        Number of top motifs to return.

    Returns
    -------
    Dict[str, Any]
        { "motifs": List[(tuple, count)], "rarity": List[float] }

    Examples
    --------
    >>> out = glyph_542(["A","B","A","B","A","C"], ngram=2)
    >>> out["motifs"][0][0]
    ('A','B')

    Exceptions
    ----------
    - ValueError : if `ngram < 1` or `ngram > len(events)` when events are non-empty.

    Complexity
    ----------
    - Time  : O(E)
    - Space : O(E)
    """
    n = len(events)
    if n == 0:
        return {"motifs": [], "rarity": []}
    if ngram < 1 or ngram > n:
        raise ValueError("ngram must be in [1, len(events)]")
    grams = [tuple(events[i:i+ngram]) for i in range(0, n - ngram + 1)]
    freq = Counter(grams)
    motifs = sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))[:topk]
    # rarity per position using average inverse frequency of n-grams covering that event
    cover_counts = [0]*n
    cover_scores = [0.0]*n
    for i, g in enumerate(grams):
        f = freq[g]
        score = 1.0 / float(f)
        for j in range(i, i+ngram):
            cover_counts[j] += 1
            cover_scores[j] += score
    rarity = [ (cover_scores[i] / cover_counts[i]) if cover_counts[i] else 0.0 for i in range(n) ]
    return {"motifs": motifs, "rarity": rarity}
