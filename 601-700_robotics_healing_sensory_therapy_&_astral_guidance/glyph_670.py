# glyph_670 – WASTE_COLLECTION_PATH
# Plan route for waste pickup without disturbing surroundings

def glyph_670(path, sensitive_areas):
    return [node for node in path if node not in sensitive_areas]
