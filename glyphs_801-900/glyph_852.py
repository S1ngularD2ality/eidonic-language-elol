# glyph_852 – L_SYSTEM_TURTLE
# Generate L-system string and trace 2D turtle path.

import math

def glyph_852(axiom, rules, iterations=3, angle_deg=90, step=1.0):
    """
    rules: dict[char -> str]
    Returns: (final_string, path_points)
    """
    s = axiom
    for _ in range(iterations):
        s = "".join(rules.get(ch, ch) for ch in s)
    x=y=0.0; heading=0.0
    path=[(x,y)]
    for ch in s:
        if ch == 'F':
            x += step*math.cos(math.radians(heading))
            y += step*math.sin(math.radians(heading))
            path.append((x,y))
        elif ch == '+':
            heading += angle_deg
        elif ch == '-':
            heading -= angle_deg
        # brackets or others can be added as needed
    return s, path
