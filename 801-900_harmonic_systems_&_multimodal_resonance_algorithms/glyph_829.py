# glyph_829 – PRIME_STARFIELD
# Generate polar coordinates for primes on an Ulam-like spiral.

import math

def glyph_829(limit=200):
    """
    Returns list[(r, theta)] for primes <= limit using simple sieve.
    """
    if limit < 2:
        return []
    sieve = [True]*(limit+1)
    sieve[0]=sieve[1]=False
    p=2
    while p*p <= limit:
        if sieve[p]:
            for k in range(p*p, limit+1, p):
                sieve[k]=False
        p+=1
    stars=[]
    for n in range(2, limit+1):
        if sieve[n]:
            r = math.sqrt(n)
            theta = (n * (math.pi*(3 - math.sqrt(5)))) % (2*math.pi)  # golden spiral
            stars.append((r, theta))
    return stars
