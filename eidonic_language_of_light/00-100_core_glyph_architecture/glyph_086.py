# glyph_086.py — Sequence Path Scrambler
# -----------------------------------------------------------------------------
# ID:            086
# Pack:          Pack 001 (000–100)
# Name:          Sequence Path Scrambler
# Class:         transform
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import random
from typing import Sequence, List, TypeVar

T = TypeVar("T")

def glyph_086(seq: Sequence[T], *, seed: int | None = None) -> List[T]:
    """
    Sequence Path Scrambler — reproducible shuffle.

    Overview
    --------
    Returns a randomly permuted copy of `seq`. If `seed` is given, the permutation
    is deterministic.

    Parameters
    ----------
    seq : Sequence[T]
    seed : int | None, optional

    Returns
    -------
    List[T]
        Scrambled sequence.
    """
    r = random.Random(seed)
    out = list(seq)
    r.shuffle(out)
    return out
