# glyph_856 – BEAT_PHASE_SCHEDULER
# Schedule event times locked to BPM with phase correction.

def glyph_856(bpm, beats=16, subdivision=4, phase_offset=0.0, start_time=0.0):
    """
    Returns list of event times (seconds) for beats*subdivision ticks.
    phase_offset: fraction of beat in [0,1)
    """
    if bpm <= 0: raise ValueError("bpm > 0")
    beat_sec = 60.0 / bpm
    times=[]
    for i in range(beats*subdivision):
        t = start_time + (i/subdivision + phase_offset) * beat_sec
        times.append(t)
    return times
