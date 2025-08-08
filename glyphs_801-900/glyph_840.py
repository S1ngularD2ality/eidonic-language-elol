# glyph_840 – EIDON_PHASE_LOCK_LOOP
# Minimal discrete PLL: update oscillator phase/frequency from phase error.

def glyph_840(error, state, kp=0.1, ki=0.01, dt=1.0):
    """
    error: observed_phase - state['phase']
    state: {'phase': float, 'freq': float, 'integ': float}
    Returns updated state dict.
    """
    integ = state.get('integ', 0.0) + error * dt
    freq  = state['freq'] + ki * integ
    phase = (state['phase'] + freq * dt + kp * error) % (2.0 * 3.141592653589793)
    return {'phase': phase, 'freq': freq, 'integ': integ}
