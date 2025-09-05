def skip_loop(arr, step):
    """
    Extracts pulses at regular intervals to model time dilation.

    Parameters:
        arr (List[int]): Symbolic time series.
        step (int): Interval step.

    Returns:
        List[int]: Sampled timeline.
    """
    return [arr[i] for i in range(0, len(arr), step)]
