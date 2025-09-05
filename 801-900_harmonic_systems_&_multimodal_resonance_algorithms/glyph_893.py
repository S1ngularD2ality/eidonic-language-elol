# glyph_893 – PITCH_CLASS_TRANSPOSE
# Transpose pitch-class profile by n semitones.

import numpy as np

def glyph_893(pcp, n_semitones):
    v = np.asarray(pcp, float)
    if v.shape[-1] != 12:
        raise ValueError("PCP must have 12 elements.")
    return np.roll(v, int(n_semitones), axis=-1)
