# glyph_832 – KNOT_INVARIANT_CHECK
# Estimate trivial crossing parity from segment list (even/odd crossing count).

def glyph_832(segments):
    """
    segments: list[((x1,y1),(x2,y2))]
    Returns 'even' or 'odd' crossing parity.
    """
    def ccw(a,b,c):
        return (c[1]-a[1])*(b[0]-a[0]) > (b[1]-a[1])*(c[0]-a[0])
    def intersect(s1, s2):
        (a,b),(c,d)=s1,s2
        return ccw(a,c,d) != ccw(b,c,d) and ccw(a,b,c) != ccw(a,b,d)
    crosses=0
    n=len(segments)
    for i in range(n):
        for j in range(i+1,n):
            if intersect(segments[i], segments[j]):
                crosses+=1
    return 'odd' if (crosses % 2) else 'even'
