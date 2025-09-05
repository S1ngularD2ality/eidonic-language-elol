# glyph_631 – CLEAN_SURFACE_SCAN
# Scan and identify surfaces before cleaning to avoid damage

def glyph_631(surface_data):
    return [s for s in surface_data if s['material'] in ['safe_clean', 'resilient']]
