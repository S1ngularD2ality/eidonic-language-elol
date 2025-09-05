def rewrite_block(arr, target, new):
    """
    Replaces all instances of target with new symbol.

    Parameters:
        arr (List[int]): Symbol stream.
        target (int): Symbol to replace.
        new (int): Replacement.

    Returns:
        List[int]: Mutated stream.
    """
    return [new if x == target else x for x in arr]
