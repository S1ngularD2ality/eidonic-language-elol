# glyph_881 – CROSS_CORR_LAG
# Find best lag between two signals via normalized cross-correlation.

import numpy as np

def glyph_881(x, y, max_lag=None):
    x = np.asarray(x, float); y = np.asarray(y, float)
    n = max(len(x), len(y))
    X = np.fft.rfft(np.pad(x, (0, n - len(x))))
    Y = np.fft.rfft(np.pad(y, (0, n - len(y))))
    c = np.fft.irfft(X * np.conj(Y))
    c = np.concatenate((c[-(n-1):], c[:n]))  # wrap negative lags first
    lags = np.arange(-(n-1), n)
    if max_lag is not None:
        m = int(max_lag)
        mid = len(c)//2
        c = c[mid-m:mid+m+1]
        lags = lags[mid-m:mid+m+1]
    # normalize
    denom = np.linalg.norm(x) * np.linalg.norm(y) + 1e-12
    c = c / denom
    k = int(np.argmax(c))
    return int(lags[k]), float(c[k])
