# glyph_734 – MODEL_SELECTION_ARBITER
# Select model by weighted score of metrics.

def glyph_734(candidates, weights=None):
    """
    candidates: dict model_name -> {'accuracy':..., 'latency':..., 'cost':...}
    weights: dict metric->weight (positive higher is better, negative lower is better)
    Returns: best_model, scores
    """
    if weights is None:
        weights = {'accuracy': 1.0, 'latency': -0.1, 'cost': -0.05}
    scores = {}
    for name, m in candidates.items():
        s = 0.0
        for k, w in weights.items():
            s += w * float(m.get(k, 0.0))
        scores[name] = s
    best = max(scores, key=scores.get) if scores else None
    return best, scores
