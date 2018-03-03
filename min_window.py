"""
https://leetcode.com/problems/minimum-window-substring/description/
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".
"""
class Solution(object):
    def minWindow(self, s, t):
        return minw(s, t)

def minw(s, t):
    p=[]
    q=[]
    max_range=None
    t1=list(t)
    for i in range(len(s)):
        if s[i] in t:
            if s[i] in t1:
                t1.pop(t1.index(s[i]))
            else:
                idx = q.index(s[i])
                p.pop(idx)
                q.pop(idx)
            p.append(i)
            q.append(s[i])
            if not t1:
                if not max_range or max_range[1]-max_range[0]>p[-1]-p[0]:
                    max_range=[p[0], p[-1]]
    if max_range:
        return s[max_range[0]:max_range[1]+1]
    return ''



