# glyph_859 – ADAPTIVE_PEAK_PICK
# Adaptive threshold peak picking for 1D sequences.

def glyph_859(values, lookahead=5, alpha=1.2, min_dist=1):
    """
    values: list[float]
    lookahead: window for local mean
    alpha: multiplier above local mean
    min_dist: minimum index distance between peaks
    returns list of peak indices
    """
    n = len(values)
    peaks=[]
    last = -min_dist-1
    for i in range(n):
        lo = max(0, i - lookahead)
        hi = min(n, i + lookahead + 1)
        loc_mean = sum(values[lo:hi]) / (hi - lo)
        thr = loc_mean * alpha
        is_peak = values[i] > thr and (i == 0 or values[i] >= values[i-1]) and (i == n-1 or values[i] >= values[i+1])
        if is_peak and (i - last) > min_dist:
            peaks.append(i); last = i
    return peaks
