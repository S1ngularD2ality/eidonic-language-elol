def extract_downtrends(arr):
    """
    Returns contiguous segments where symbols descend.

    Parameters:
        arr (List[int]): Signal data.

    Returns:
        List[List[int]]: Downtrend segments.
    """
    result = []
    temp = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            temp.append(arr[i])
        else:
            if len(temp) > 1:
                result.append(temp)
            temp = [arr[i]]
    if len(temp) > 1:
        result.append(temp)
    return result
