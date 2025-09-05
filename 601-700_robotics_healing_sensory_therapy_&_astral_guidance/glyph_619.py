# glyph_619 – COLLABORATIVE_LOAD_SHARE
# Distribute carrying load between multiple bots

def glyph_619(total_weight, num_bots):
    return total_weight / max(1, num_bots)
