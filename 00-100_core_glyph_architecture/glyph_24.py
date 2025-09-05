from collections import Counter

def frequency_count(arr):
    """
    Counts symbolic occurrences within a sequence.

    Parameters:
        arr (List[int]): Symbolic array.

    Returns:
        Dict[int, int]: Frequency mapping.
    """
    return dict(Counter(arr))
