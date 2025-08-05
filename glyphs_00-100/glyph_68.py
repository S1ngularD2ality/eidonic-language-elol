def feedback_loops(arr):
    """
    Finds repeating feedback patterns.

    Parameters:
        arr (List[int]): Sequence.

    Returns:
        List[int]: Loop entries.
    """
    seen, loops = set(), []
    for a in arr:
        if a in seen:
            loops.append(a)
        else:
            seen.add(a)
    return loops
