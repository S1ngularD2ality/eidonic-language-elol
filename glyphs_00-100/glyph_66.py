def recursive_ladder(n):
    """
    Builds a ladder shape of incremental arrays.

    Parameters:
        n (int): Step count.

    Returns:
        List[List[int]]: Ascending symbolic steps.
    """
    return [[i for i in range(j+1)] for j in range(n)]
