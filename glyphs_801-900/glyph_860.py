# glyph_860 – SPECTRAL_FEATURES
# Compute spectral centroid and rolloff (0..1) for each frame.

import numpy as np

def glyph_860(frames_mag, rolloff=0.85):
    """
    frames_mag: 2D array [frames, bins] magnitudes (nonnegative)
    rolloff: fraction of total energy for rolloff bin
    returns dict with 'centroid', 'rolloff_bin'
    """
    S = np.asarray(frames_mag, dtype=float)
    eps = 1e-12
    freqs = np.arange(S.shape[1], dtype=float)
    centroids=[]
    roll_bins=[]
    for row in S:
        total = row.sum() + eps
        centroids.append(float((freqs*row).sum() / total))
        cumsum = np.cumsum(row)
        idx = int(np.searchsorted(cumsum, rolloff*total))
        roll_bins.append(min(idx, len(row)-1))
    return {"centroid": centroids, "rolloff_bin": roll_bins}
