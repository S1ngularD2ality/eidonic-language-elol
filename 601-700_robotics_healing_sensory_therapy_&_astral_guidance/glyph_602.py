# glyph_602 – LIDAR_SIM
# Simulate LIDAR sensor readings for safe navigation

import math

def glyph_602(position, obstacles, max_distance=10, angle_step=5):
    readings = {}
    for angle in range(0, 360, angle_step):
        rad = math.radians(angle)
        for dist in range(1, max_distance+1):
            x = position[0] + dist * math.cos(rad)
            y = position[1] + dist * math.sin(rad)
            if any(abs(x-ox) < 0.5 and abs(y-oy) < 0.5 for ox, oy in obstacles):
                readings[angle] = dist
                break
        else:
            readings[angle] = max_distance
    return readings
