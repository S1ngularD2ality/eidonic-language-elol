# glyph_822 – FIBONACCI_SMOOTHER
# Smooth a sequence using a Fibonacci-weighted moving window.

def glyph_822(values, radius=2):
    """
    values: list[float], radius >= 1
    Returns smoothed list.
    """
    if not values:
        return []
    # Build Fibonacci weights: e.g., radius=2 -> [1,1,2,3,5] mirrored around center
    fib = [1, 1]
    for _ in range(2, radius+1):
        fib.append(fib[-1] + fib[-2])
    left = fib[:-1]
    weights = left[::-1] + [fib[-1]] + fib[:-1]
    wsum = sum(weights)
    n = len(values)
    out = []
    for i in range(n):
        acc = 0.0
        for k, w in enumerate(weights, start=-radius):
            j = max(0, min(n-1, i + k))
            acc += values[j] * w
        out.append(acc / wsum)
    return out
