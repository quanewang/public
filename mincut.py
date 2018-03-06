"""
LESSON:
-- remaining_cuts-1 => remaining_cuts

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.

n=1, cur=1..len-1
01234

"""

class Solution(object):
    def minCut(self, s):
        if not s:
            return 0
        for cuts in range(len(s)-1):
            if self.minCutHelper(s, cuts, 1, []):
                return cuts
        return len(s)-1

    #index: 1..len-1
    def minCutHelper(self, s, remaining_cuts, cut_pos, partition):
        if cut_pos>=len(s):
            return self.isPalindrome(s, partition)
        if remaining_cuts==0:
            return self.isPalindrome(s, partition)
        if not self.minCutHelper(s, remaining_cuts, cut_pos+1, partition):
            partition.append(cut_pos)
            status = self.minCutHelper(s, remaining_cuts-1, cut_pos+1, partition)
            partition.pop()
            return status
        return True

    def isPalindrome(self, s, partition):
        start = 0
        for p in partition:
            if not self.verify(s, start, p-1):
                return False
            start = p
        if start<len(s)-1:
            if not self.verify(s, start, len(s)-1):
                return False
        return True

    def verify(self, s, start, end):
        while start<end:
            if s[start]!=s[end]:
                return False
            start += 1
            end -= 1
        return True

def dp(s):
    if not s:
        return 0
    n=len(s)
    m=[0]*n
    for i in range(1, n):
        m[i]=1+m[i-1]
        for j in range(0, i):
            if valid(s[j:i+1]):
                if j==0:
                    m[i] = min(m[i], m[j])
                else:
                    m[i] = min(m[i], m[j-1]+1)

    return m[n-1]
def valid(s):
    l, h=0, len(s)-1
    while l<h:
        if s[l]!=s[h]:
            return False
        l+=1
        h-=1
    return True
print dp("aabaa")
print dp("abceedee")