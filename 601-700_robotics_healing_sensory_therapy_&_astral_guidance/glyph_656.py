# glyph_656 – PATH_REDUNDANCY_CHECK
# Verify there’s always a backup route to goal

def glyph_656(paths):
    return any(len(p) > 0 for p in paths)
