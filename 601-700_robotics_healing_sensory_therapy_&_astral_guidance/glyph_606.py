# glyph_606 – SOLAR_RECHARGE_OPTIMIZER
# Plan recharge stops for solar-powered bots

def glyph_606(route, sunny_spots):
    return [node for node in route if node in sunny_spots]
