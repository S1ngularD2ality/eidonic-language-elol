# glyph_824 – DODECA_PALINDROME_HASH
# 12-fold palindromic rolling hash (lightweight, stable across folds).

def glyph_824(text: str) -> int:
    """
    Returns a 64-bit hash emphasizing 12-fold symmetry.
    """
    mod = (1 << 64) - 1
    h1, h2 = 1469598103934665603, 1099511628211
    for i, ch in enumerate(text):
        c = ord(ch)
        # forward fold
        h1 ^= (c + (i % 12))
        h1 = (h1 * 1099511628211) & mod
        # reverse fold
        j = len(text) - 1 - i
        h2 ^= (c + (j % 12))
        h2 = (h2 * 1469598103934665603) & mod
    return (h1 ^ ((h2 << 1) | (h2 >> 63))) & mod
