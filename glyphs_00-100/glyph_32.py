def mutate_frame(arr):
    """
    Applies symbolic mutation by incrementing every second symbol.

    Parameters:
        arr (List[int]): Genetic-like pattern.

    Returns:
        List[int]: Mutated frame.
    """
    return [x+1 if i % 2 else x for i, x in enumerate(arr)]
