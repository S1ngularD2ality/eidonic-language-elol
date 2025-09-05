# glyph_741 – CONTINUOUS_ALIGNMENT_CHECK
# Continuously verify AI outputs against evolving alignment criteria.

class glyph_741:
    def __init__(self, alignment_fn):
        """
        alignment_fn: callable(output) -> bool
        """
        self.alignment_fn = alignment_fn
        self.history = []

    def check(self, output):
        aligned = self.alignment_fn(output)
        self.history.append((output, aligned))
        return aligned
