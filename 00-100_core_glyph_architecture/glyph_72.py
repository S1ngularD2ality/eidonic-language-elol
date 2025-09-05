def symbol_fold(arr):
    """
    Folds the symbolic stream at center.

    Parameters:
        arr (List[int])

    Returns:
        List[Tuple[int, int]]
    """
    mid = len(arr)//2
    return list(zip(arr[:mid], reversed(arr[-mid:])))
