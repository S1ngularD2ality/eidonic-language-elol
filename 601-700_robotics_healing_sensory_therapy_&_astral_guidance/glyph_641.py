# glyph_641 – SAFE_LIFT_BALANCE
# Adjust lift position to maintain load balance

def glyph_641(load_distribution):
    return 'adjust_left' if load_distribution['left'] > load_distribution['right'] else 'adjust_right'
