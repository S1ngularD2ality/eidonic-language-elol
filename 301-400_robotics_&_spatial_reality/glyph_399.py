# glyph_399 – MICRO_MOTION
# Perform precise, minuscule adjustments for delicate tasks

def glyph_399(current, target, step=0.01):
    """
    current: current value
    target: target value
    step: smallest increment
    Returns: next move value
    """
    if abs(target - current) < step:
        return target
    return current + step if target > current else current - step
