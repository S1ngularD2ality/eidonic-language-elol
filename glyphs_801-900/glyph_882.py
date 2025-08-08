# glyph_882 – SPECTRAL_FLATNESS
# Compute spectral flatness (geometric/arith mean) per frame.

import numpy as np

def glyph_882(frames_mag, eps=1e-12):
    S = np.asarray(frames_mag, float)
    S = np.maximum(S, eps)
    geo = np.exp(np.mean(np.log(S), axis=1))
    ari = np.mean(S, axis=1) + eps
    return (geo / ari).tolist()
