def radial_bloom(n):
    """
    Creates radial layers of increasing symbolic intensity.

    Parameters:
        n (int): Size of grid (odd preferred for symmetry).

    Returns:
        List[List[int]]: Radial pattern grid.
    """
    center = n // 2
    return [[max(abs(i-center), abs(j-center)) for j in range(n)] for i in range(n)]
