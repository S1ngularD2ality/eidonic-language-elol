# glyph_647 – VOICE_CALM_MODE
# Use calm and slow voice synthesis when speaking to distressed humans

def glyph_647(emotion_state):
    return {'voice_speed': 0.8, 'tone': 'calm'} if emotion_state == 'distressed' else {'voice_speed': 1.0, 'tone': 'neutral'}
