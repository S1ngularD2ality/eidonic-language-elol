def anchor_reverse(arr):
    """
    Anchors the last element, reverses all before.

    Parameters:
        arr (List[int]): Input stream.

    Returns:
        List[int]: Reversed tail-anchored array.
    """
    if not arr:
        return []
    return arr[:-1][::-1] + [arr[-1]]
