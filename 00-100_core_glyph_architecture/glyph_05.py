def opposite_poles(arr):
    """
    Detects all element pairs in a list whose sum is zero (nullifying polarities).

    Parameters:
        arr (List[int]): A list of integers to evaluate.

    Returns:
        List[Tuple[int, int]]: Pairs of opposite values that cancel each other out.
    """
    return [(i, j) for i in arr for j in arr if i + j == 0]
