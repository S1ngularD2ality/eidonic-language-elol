# glyph_611 – EMOTION_SAFE_INTERACTION
# Adjust interaction level based on detected emotional state

def glyph_611(emotion_state):
    if emotion_state == 'stressed':
        return 'slow_gentle'
    elif emotion_state == 'neutral':
        return 'normal'
    else:
        return 'uplifting'
