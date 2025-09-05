# glyph_885 – ZERO_CROSS_RATE
# Frame-wise zero-crossing rate.

import numpy as np

def glyph_885(signal, frame=1024, hop=512):
    x = np.asarray(signal, float)
    rates = []
    for i in range(0, len(x)-frame+1, hop):
        seg = x[i:i+frame]
        zc = np.sum(np.abs(np.diff(np.signbit(seg)))) / 2.0
        rates.append(zc / frame)
    return rates
