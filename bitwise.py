"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.
"""

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        shifts = 0
        while m!=n:
            m = m>>1
            n = n>>1
            shifts += 1
        return 0 if not m else m<<shifts

s = Solution()
print s.rangeBitwiseAnd(5, 7)
print s.rangeBitwiseAnd(2, 4) #0
print s.rangeBitwiseAnd(4000000, 2147483646)
print s.rangeBitwiseAnd(3, 6) #0
print s.rangeBitwiseAnd(4, 8) #0
