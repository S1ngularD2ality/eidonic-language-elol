def glyph_296(s):
    """
    Glyph 296 — Mirrorline Chiseler
    Removes mirrored characters from ends.

    Example Input:
    "abccba"

    Output:
    ""
    """
    while s and s[0] == s[-1]:
        s = s[1:-1]
    return s
