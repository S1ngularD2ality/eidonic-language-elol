# glyph_823 – STAR_POLYGON_ROUTER
# Generate a star-polygon visit order (n,k) visiting all nodes without repetition.

def glyph_823(n, k):
    """
    Returns the visitation sequence for a star polygon (n,k).
    Requires gcd(n, k) == 1 for a single cycle.
    """
    from math import gcd
    if n < 3 or k < 1 or k >= n or gcd(n, k) != 1:
        raise ValueError("Require n>=3, 1<=k<n, and gcd(n,k)==1")
    seq = []
    v = 0
    seen = set()
    for _ in range(n):
        seq.append(v)
        seen.add(v)
        v = (v + k) % n
    return seq
