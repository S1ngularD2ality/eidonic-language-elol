# glyph_724 – PROVENANCE_TAGGER
# Attach provenance tags to objects (immutable tuple tags).

def glyph_724(obj, *tags):
    """
    Returns a (obj, tags_tuple) pair for simple provenance tracking.
    """
    return obj, tuple(tags)
