# glyph_888 – NORMALIZE_PEAK
# Normalize signal to target peak.

import numpy as np

def glyph_888(signal, target=0.99):
    x = np.asarray(signal, float)
    peak = np.max(np.abs(x)) + 1e-12
    return (x * (target/peak)).astype(np.float32)
