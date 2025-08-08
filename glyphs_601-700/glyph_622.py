# glyph_622 – PROTECTIVE_BARRIER_DEPLOY
# Deploy soft protective barrier if collision risk detected

def glyph_622(collision_risk):
    return 'DEPLOY' if collision_risk else 'RETRACT'
