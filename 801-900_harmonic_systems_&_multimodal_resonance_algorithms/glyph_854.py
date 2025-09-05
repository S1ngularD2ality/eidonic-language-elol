# glyph_854 – BEZIER_DE_CASTELJAU
# Evaluate arbitrary-degree Bezier curve at N samples.

def glyph_854(control_points, N=100):
    """
    control_points: list[(x,y)]
    Returns list[(x,y)] length N
    """
    if len(control_points) < 2:
        raise ValueError("Need >= 2 control points.")
    def de_casteljau(ctrl, t):
        pts = list(ctrl)
        while len(pts) > 1:
            pts = [( (1-t)*pts[i][0] + t*pts[i+1][0],
                     (1-t)*pts[i][1] + t*pts[i+1][1]) for i in range(len(pts)-1)]
        return pts[0]
    return [de_casteljau(control_points, i/(N-1)) for i in range(N)]
