# glyph_887 – SILENCE_TRIM
# Trim leading/trailing silence below threshold (in RMS).

import numpy as np

def glyph_887(signal, threshold=1e-3, frame=1024, hop=256):
    x = np.asarray(signal, float)
    rms = []
    idx = []
    for i in range(0, max(1, len(x)-frame+1), hop):
        seg = x[i:i+frame]
        r = np.sqrt(np.mean(seg*seg)) if len(seg) else 0.0
        rms.append(r); idx.append(i)
    nz = [i for i, r in enumerate(rms) if r >= threshold]
    if not nz:
        return x[:0]
    start = idx[nz[0]]
    end   = min(idx[nz[-1]] + frame, len(x))
    return x[start:end]
