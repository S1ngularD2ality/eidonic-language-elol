# glyph_731 – ADVERSARIAL_FUZZER
# Generate simple adversarial text variants for robustness testing.

import random
import string

def glyph_731(text: str, n=10):
    """
    Returns list of n mutated strings: case flips, homoglyph-like swaps, noise insertions.
    """
    def mutate(s):
        ops = []
        if s:
            # case flip
            i = random.randrange(len(s))
            s = s[:i] + (s[i].swapcase()) + s[i+1:]
            ops.append("case")
        # noise insert
        pos = random.randrange(len(s)+1)
        s = s[:pos] + random.choice(string.punctuation) + s[pos:]
        ops.append("noise")
        return s

    return [mutate(text) for _ in range(n)]
