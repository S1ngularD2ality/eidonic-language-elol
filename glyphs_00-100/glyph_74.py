def build_shell(n):
    """
    Creates a dimensional shell of increasing integers.

    Parameters:
        n (int)

    Returns:
        List[List[int]]
    """
    return [[j for j in range(i+1)] for i in range(n)]
