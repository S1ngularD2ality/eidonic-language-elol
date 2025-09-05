# glyph_629 – ASSISTIVE_HANDOFF
# Smoothly hand off object to human without sudden movement

def glyph_629(object_weight, human_grip_strength):
    return 'slow_release' if human_grip_strength < object_weight else 'normal_release'
