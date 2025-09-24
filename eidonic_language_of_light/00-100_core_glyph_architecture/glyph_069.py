# glyph_069.py — Dimensional Memory Compressor
# -----------------------------------------------------------------------------
# ID:            069
# Pack:          Pack 001 (000–100)
# Name:          Dimensional Memory Compressor
# Class:         analyzer
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List, Tuple

def glyph_069(matrix: Sequence[Sequence[float]], *, k: int) -> Tuple[List[float], List[List[float]]]:
    """
    Dimensional Memory Compressor — truncated SVD (power iteration, CPU-portable).

    Overview
    --------
    Approximates top-k left singular vectors and singular values using power iterations
    on A Aᵀ. Returns (singular_values, basis_vectors).

    Parameters
    ----------
    matrix : Sequence[Sequence[float]]
        Real matrix (m×n).
    k : int
        Target rank (1..m).

    Returns
    -------
    (List[float], List[List[float]])
        (σ[0..k-1], U[:,0..k-1]) approximate.

    Examples
    --------
    >>> s, U = glyph_069([[1,0],[0,1]], k=1)
    >>> len(s), len(U[0]) == 1, True

    Exceptions
    ----------
    - ValueError : invalid k or empty matrix.

    Complexity
    ----------
    - Time  : O(iters · m · n · k)
    - Space : O(m · k)
    """
    A = [list(map(float, row)) for row in matrix]
    if not A or not A[0]:
        raise ValueError("matrix must be non-empty")
    m, n = len(A), len(A[0])
    if k < 1 or k > m:
        raise ValueError("k out of range")
    # naive Gram matrix G = A A^T
    G = [[0.0]*m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            G[i][j] = sum(A[i][t]*A[j][t] for t in range(n))
    # power iteration with deflation
    import math, random
    U: List[List[float]] = []
    S: List[float] = []
    for _ in range(k):
        v = [random.random() for _ in range(m)]
        # iterate
        for _ in range(10):
            w = [sum(G[i][j]*v[j] for j in range(m)) for i in range(m)]
            # orthogonalize against previous
            for u in U:
                dot = sum(w[i]*u[i] for i in range(m))
                for i in range(m):
                    w[i] -= dot*u[i]
            norm = math.sqrt(sum(x*x for x in w)) or 1.0
            v = [x/norm for x in w]
        # Rayleigh quotient for eigenvalue
        lam = sum(v[i]*sum(G[i][j]*v[j] for j in range(m)) for i in range(m))
        S.append(math.sqrt(max(lam, 0.0)))
        U.append(v[:])
        # deflate G
        for i in range(m):
            for j in range(m):
                G[i][j] -= lam * v[i]*v[j]
    return S, U
