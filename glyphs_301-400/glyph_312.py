# glyph_312 – MOTION_SENSE
# Detect and classify moving objects within a scene

def glyph_312(frame_sequence):
    """
    frame_sequence: list of image frames
    Returns: list of moving object coordinates
    """
    moving_objects = []
    for idx, frame in enumerate(frame_sequence[:-1]):
        # Compare to next frame
        diff = abs(frame_sequence[idx+1]['pixels'] - frame['pixels'])
        if diff.sum() > 100:  # Threshold example
            moving_objects.append(frame['coords'])
    return moving_objects
