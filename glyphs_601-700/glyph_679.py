# glyph_679 – RESPECT_QUIET_ZONE
# Avoid noise in designated quiet areas

def glyph_679(path, quiet_zones):
    return [node for node in path if node not in quiet_zones]
