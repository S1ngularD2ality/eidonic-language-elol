# glyph_999 – QUANTUM_ATTACK_EARLY_WARNING
"""
Quantum Attack Early Warning (QAEW)

Heuristic monitor combining:
- unusual decryption request rates,
- multiple failed predicate checks,
- entropy source anomalies.

Produces a risk score in [0, 100].

APIs:
- score(dec_rate, fail_predicates, entropy_jitter) -> float
"""

def score(dec_rate: float, fail_predicates: int, entropy_jitter: float) -> float:
    # Normalize crude heuristics
    r = min(dec_rate / 100.0, 1.0) * 50.0            # rate pressure
    f = min(fail_predicates / 10.0, 1.0) * 35.0      # gate failures
    e = (1.0 - max(min(entropy_jitter, 1.0), 0.0)) * 15.0  # low jitter suspicious
    return min(r + f + e, 100.0)
