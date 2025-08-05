def drift_average(arr):
    """
    Computes average between adjacent symbols for smoothing.

    Parameters:
        arr (List[int]): Symbol stream.

    Returns:
        List[float]: Smoothed values.
    """
    return [(arr[i] + arr[i+1]) / 2 for i in range(len(arr)-1)]
