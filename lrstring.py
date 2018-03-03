"""
https://leetcode.com/problems/swap-adjacent-in-lr-string/description/
Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
Output: True
"""
class Solution(object):
    def canTransform(self, start, end):
        return transform(start,end)

def transform(start, end):
    if start==end:
        return True
    if not start or len(start)!=len(end):
        return False
    for i in range(len(start)-1):
        if start[i:i+2] in ['XL', 'RX']:
            if transform(start[:i] + start[i+1] + start[i] + start[i+2:], end):
                return True
    return False

s = Solution()
print s.canTransform("XRXXLXLXXXXRXXXXLXXL", "XXRXLXXLXXRLXXXLXXXX")