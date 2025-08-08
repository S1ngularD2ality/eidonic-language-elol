# glyph_727 – RESOURCE_GOVERNOR
# Compute throttle or scale recommendations from resource usage.

def glyph_727(cpu_util: float, mem_util: float, rps: float):
    """
    Returns: {'throttle': 0..1, 'scale_delta': int}
    """
    throttle = 0.0
    scale_delta = 0
    if cpu_util > 0.85 or mem_util > 0.9:
        throttle = min(1.0, (cpu_util - 0.85) * 4 + (mem_util - 0.9) * 4)
        scale_delta += 1
    if rps > 1000 and cpu_util > 0.7:
        scale_delta += 1
    if cpu_util < 0.25 and rps < 200:
        scale_delta -= 1
    return {"throttle": max(0.0, throttle), "scale_delta": scale_delta}
