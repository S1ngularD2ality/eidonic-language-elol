# glyph_863 – PHASE_UNWRAP
# Unwrap phase along axis=0 for [frames, bins] radian phases.

import numpy as np

def glyph_863(phase_matrix):
    P = np.asarray(phase_matrix, dtype=float).copy()
    return np.unwrap(P, axis=0)
