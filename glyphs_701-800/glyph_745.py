# glyph_745 – SYSTEM_HEALTH_PREDICTOR
# Predicts system health score based on recent metrics.

import statistics

def glyph_745(metrics):
    """
    metrics: list of {'cpu':0..1, 'mem':0..1, 'errors':int}
    Returns: predicted health score (0..1)
    """
    if not metrics:
        return 1.0
    cpu = statistics.mean(m['cpu'] for m in metrics)
    mem = statistics.mean(m['mem'] for m in metrics)
    err = statistics.mean(m['errors'] for m in metrics)
    score = max(0.0, 1.0 - (cpu + mem)/2 - (err/100))
    return round(score, 3)
