# glyph_886 – RMS_ENERGY
# Frame-wise RMS energy.

import numpy as np

def glyph_886(signal, frame=1024, hop=512):
    x = np.asarray(signal, float)
    out = []
    for i in range(0, len(x)-frame+1, hop):
        seg = x[i:i+frame]
        out.append(float(np.sqrt(np.mean(seg*seg))))
    return out
