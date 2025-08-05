from collections import Counter

def echo_density(arr):
    """
    Measures the repetition density of each symbol.

    Parameters:
        arr (List[int]): Symbol array.

    Returns:
        Dict[int, int]: Symbol frequencies.
    """
    return dict(Counter(arr))
