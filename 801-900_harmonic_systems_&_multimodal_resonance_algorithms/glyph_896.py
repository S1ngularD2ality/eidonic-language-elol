# glyph_896 – WAVESHAPER_TANH
# Nonlinear waveshaper using tanh drive and output gain.

import numpy as np

def glyph_896(signal, drive=2.0, out_gain=1.0):
    x = np.asarray(signal, float)
    y = np.tanh(drive * x)
    return (y * out_gain).astype(np.float32)
