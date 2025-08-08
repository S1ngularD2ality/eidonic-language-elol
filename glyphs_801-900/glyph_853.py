# glyph_853 – CATMULL_ROM_SPLINE
# Sample Catmull-Rom spline through control points.

def glyph_853(points, samples_per_segment=20, alpha=0.5):
    """
    points: list[(x,y)] with len>=4
    alpha: 0.5 centripetal; 0 chordal  -> choose parameterization
    Returns: list[(x,y)] sampled points
    """
    if len(points) < 4:
        raise ValueError("Need >= 4 control points.")
    def tj(ti, pi, pj):
        import math
        dx = pj[0]-pi[0]; dy = pj[1]-pi[1]
        return ( (dx*dx + dy*dy)**0.5 )**alpha + ti
    out=[]
    for i in range(1, len(points)-2):
        p0, p1, p2, p3 = points[i-1], points[i], points[i+1], points[i+2]
        t0 = 0.0
        t1 = tj(t0,p0,p1); t2 = tj(t1,p1,p2); t3 = tj(t2,p2,p3)
        for t in [t1 + (t2-t1)*k/samples_per_segment for k in range(samples_per_segment)]:
            def interp(pa, pb, ta, tb, t):
                if tb - ta == 0: return pa
                u = (t - ta)/(tb - ta)
                return (pa[0] + u*(pb[0]-pa[0]), pa[1] + u*(pb[1]-pa[1]))
            A1 = interp(p0,p1,t0,t1,t)
            A2 = interp(p1,p2,t1,t2,t)
            A3 = interp(p2,p3,t2,t3,t)
            B1 = interp(A1,A2,t0,t2,t)
            B2 = interp(A2,A3,t1,t3,t)
            C  = interp(B1,B2,t1,t2,t)
            out.append(C)
    out.append(points[-2])
    return out
