# glyph_728 – CANARY_ROLLOUT
# Decide whether to promote, hold, or rollback a canary based on metrics.

def glyph_728(canary_metrics, baseline_metrics, tolerances):
    """
    Each metrics dict contains keys like 'error_rate','latency_p95','cpu'.
    tolerances: dict key->max_allowed_ratio (canary/baseline)
    Returns: 'promote'|'hold'|'rollback'
    """
    decision = "promote"
    for k, max_ratio in tolerances.items():
        b = max(1e-9, float(baseline_metrics.get(k, 1.0)))
        c = float(canary_metrics.get(k, b))
        ratio = c / b
        if ratio > max_ratio:
            return "rollback"
        if ratio > max_ratio * 0.9:
            decision = "hold"
    return decision
