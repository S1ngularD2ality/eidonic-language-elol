# glyph_879 – RANSAC_LINE_2D
# Robust 2D line fitting y = mx + b via RANSAC.

import random
import numpy as np

def glyph_879(points, iters=200, tol=0.01, seed=None):
    pts = np.asarray(points, float)
    if len(pts) < 2:
        raise ValueError("Need >= 2 points.")
    rng = random.Random(seed)
    best_m, best_b, best_in = 0.0, 0.0, []
    for _ in range(iters):
        i, j = rng.sample(range(len(pts)), 2)
        (x1, y1), (x2, y2) = pts[i], pts[j]
        if x2 == x1:  # vertical; skip
            continue
        m = (y2 - y1) / (x2 - x1)
        b = y1 - m*x1
        d = np.abs(pts[:,1] - (m*pts[:,0] + b)) / (np.sqrt(m*m + 1))
        inliers = np.where(d < tol)[0].tolist()
        if len(inliers) > len(best_in):
            best_in = inliers; best_m, best_b = m, b
    return {"m": float(best_m), "b": float(best_b), "inliers": best_in}
