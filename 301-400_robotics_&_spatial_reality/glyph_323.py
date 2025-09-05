# glyph_323 – FOCUS_RING
# Isolate, highlight, and lock onto a single object in a complex field

def glyph_323(objects, target_features):
    """
    objects: list of object dicts
    target_features: dict of key features to match
    Returns: object matching features or None
    """
    for obj in objects:
        if all(obj.get(k) == v for k, v in target_features.items()):
            return obj
    return None
