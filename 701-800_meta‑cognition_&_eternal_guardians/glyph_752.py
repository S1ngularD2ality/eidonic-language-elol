# glyph_752 – ADAPTIVE_THROTTLER
# Adjust request rate dynamically based on error and latency.

def glyph_752(error_rate, latency, current_rate):
    """
    Returns: new_rate
    """
    if error_rate > 0.05 or latency > 2.0:
        return max(1, int(current_rate * 0.8))
    elif error_rate < 0.01 and latency < 1.0:
        return int(current_rate * 1.2)
    return current_rate
