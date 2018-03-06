"""
--LESSON
-- 3/3
-- 2/3
-- 4/2
"""

def div(m, n):
    factors=[1]
    power=0
    factor=1
    while factor*n<=m:
        factor = factor<<1
        factors.append(factor)
        power += 1
    power -= 1
    r=0
    while power>=0:
        if m >= factors[power]*n:
            m = m - factors[power]*n
            r += factors[power]
        power -= 1
    return r

print div(3, 3)