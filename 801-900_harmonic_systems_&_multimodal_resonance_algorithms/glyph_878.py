# glyph_878 – KABSCH_ALIGN
# Compute optimal 3D rotation+translation aligning A->B (least squares).

import numpy as np

def glyph_878(A, B):
    """
    A,B: [N,3] corresponding 3D points
    Returns dict(R,t) where x' = R@x + t
    """
    A = np.asarray(A, float); B = np.asarray(B, float)
    if A.shape != B.shape or A.shape[0] < 3:
        raise ValueError("Need at least 3 corresponding 3D points.")
    cA = A.mean(axis=0); cB = B.mean(axis=0)
    AA = A - cA; BB = B - cB
    H = AA.T @ BB
    U, S, Vt = np.linalg.svd(H)
    R = Vt.T @ U.T
    if np.linalg.det(R) < 0:
        Vt[-1, :] *= -1
        R = Vt.T @ U.T
    t = cB - R @ cA
    return {"R": R, "t": t}
