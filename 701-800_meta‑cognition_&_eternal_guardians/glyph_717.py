# glyph_717 – HARMONIC_SYSTEM_HEALER
# Balance system metrics by feedback control.

class glyph_717:
    """
    Expects metrics dict {'cpu':0..1,'mem':0..1,'latency':ms}
    Returns recommended adjustments: {'scale': +/-int, 'sleep_ms': int}
    """
    def recommend(self, metrics):
        scale = 0
        sleep_ms = 0
        if metrics.get("cpu", 0) > 0.85 or metrics.get("mem", 0) > 0.9:
            scale += 1
        if metrics.get("latency", 0) > 200:
            scale += 1
            sleep_ms += 10
        if metrics.get("cpu", 0) < 0.2 and metrics.get("latency", 0) < 50:
            scale -= 1
        return {"scale": scale, "sleep_ms": sleep_ms}
