"""
You are given a number n in hexadecimal. A new number can be made
from the number n by selecting
any subsequence of it (in HexaDecimal) and rearranging it.
You have tell the number of distinct numbers that can be made from number n.
Since the answer will be very large, output the answer as modulo 10^9+7.
Input:
1F
1FF
Output:
4
8

Explanation:

For 1FF possible combinations are - 1,F,1F,F1,FF,1FF,F1F,FF1
"""
def hex_count(h):
    if not h:
        return 0
    result = {}
    u = {}
    for x in h:
        if x not in u:
            u[x]=1
        else:
            u[x] = u[x]+1
    for i in range(1, len(h)+1):
        for x in hex(dict(u), i, ''):
            result[x]=1
    return len(result)

def hex(u, i, progress):
    if i<=0:
        return [progress]
    r = []
    for x in u.iterkeys():
        if u[x]>=1:
            u[x]=u[x]-1
        else:
            continue
        r += hex(dict(u), i-1, progress + x)
        u[x] = u[x] + 1
    return r


print hex_count('1F')
print hex_count('1FF')