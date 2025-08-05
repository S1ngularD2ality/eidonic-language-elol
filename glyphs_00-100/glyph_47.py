def time_cross_section(frames, index):
    """
    Extracts the nth element from each frame (time slice).

    Parameters:
        frames (List[List[int]]): Sequence of frames.
        index (int): Index to extract.

    Returns:
        List[int]: Cross-sectional timeline.
    """
    return [frame[index] for frame in frames if index < len(frame)]
