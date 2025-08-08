# glyph_880 – ROBUST_ZSCORE_OUTLIERS
# Flag outliers using median and MAD (robust z-score).

import numpy as np

def glyph_880(values, thresh=3.5):
    x = np.asarray(values, float)
    med = np.median(x)
    mad = np.median(np.abs(x - med)) + 1e-12
    z = 0.6745 * (x - med) / mad
    idx = np.where(np.abs(z) > thresh)[0].tolist()
    return {"z": z.tolist(), "outliers": idx}
