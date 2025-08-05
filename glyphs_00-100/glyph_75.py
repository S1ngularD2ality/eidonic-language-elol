def reverse_spiral(arr):
    """
    Builds a spiral of nested reversals.

    Parameters:
        arr (List[int])

    Returns:
        List[List[int]]
    """
    return [[*reversed(arr[:i+1])] for i in range(len(arr))]
