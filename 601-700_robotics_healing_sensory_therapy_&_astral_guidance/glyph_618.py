# glyph_618 – BIO_SCAN_AVOID
# Avoid sensitive biological zones (nests, habitats, gardens)

def glyph_618(path, bio_zones):
    return [node for node in path if node not in bio_zones]
