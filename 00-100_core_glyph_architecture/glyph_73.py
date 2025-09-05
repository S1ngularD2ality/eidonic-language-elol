def delta_cascade(arr):
    """
    Transforms array into delta progression.

    Parameters:
        arr (List[int])

    Returns:
        List[int]: Delta-encoded stream.
    """
    return [arr[i+1] - arr[i] for i in range(len(arr)-1)]
