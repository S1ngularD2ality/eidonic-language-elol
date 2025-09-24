# glyph_208.py — Subconscious Logic Collapser
# -----------------------------------------------------------------------------
# ID:            208
# Pack:          Pack 003 (201–300)
# Name:          Subconscious Logic Collapser
# Class:         analyzer
# Stability:     Stable
# Version:       1.0.1
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Tuple

def glyph_208(facts: Mapping[str, bool]) -> Tuple[bool, int]:
    """
    Subconscious Logic Collapser — evaluate conjunctive truth and contradictions.

    Overview
    --------
    Returns (all_true, contradictions), where contradictions counts paired keys
    like 'A' and 'not A'.

    Parameters
    ----------
    facts : Mapping[str, bool]
        Boolean assignments for propositions.

    Returns
    -------
    (bool, int)
        (conjunction, contradiction_count)

    Examples
    --------
    >>> glyph_208({"A": True, "not A": True})
    (False, 1)

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(1)
    """
    conj = all(bool(v) for v in facts.values()) if facts else False
    negations = sum(
        1 for k in facts
        if ("not " + k) in facts and facts[k] and facts["not " + k]
    )
    return conj and (negations == 0), negations
