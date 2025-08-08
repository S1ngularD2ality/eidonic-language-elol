# glyph_874 – DTW_DISTANCE
# Dynamic Time Warping distance between two sequences (Euclidean).

import numpy as np

def glyph_874(a, b):
    A = np.asarray(a, float)
    B = np.asarray(b, float)
    NA, NB = len(A), len(B)
    D = np.full((NA+1, NB+1), np.inf)
    D[0,0] = 0.0
    for i in range(1, NA+1):
        for j in range(1, NB+1):
            cost = (A[i-1] - B[j-1])**2
            D[i,j] = cost + min(D[i-1,j], D[i,j-1], D[i-1,j-1])
    return float(np.sqrt(D[NA, NB]))
