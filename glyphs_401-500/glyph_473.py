# glyph_473 – SIGNAL_THROTTLE
# Limit the frequency of signals to prevent overload

def glyph_473(signals, max_per_second):
    """
    signals: list of (timestamp, signal)
    max_per_second: int
    Returns: filtered list of signals
    """
    from collections import defaultdict
    per_second = defaultdict(list)
    for ts, sig in signals:
        per_second[int(ts)].append(sig)
    return [sigs[:max_per_second] for sigs in per_second.values()]
