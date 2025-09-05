def descent_map(n):
    """
    Creates a triangular descent path.

    Returns:
        List[List[int]]
    """
    return [[j for j in range(i+1)] for i in range(n)]
