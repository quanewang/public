"""
Nearly every one have used the Multiplication Table. But could you find out the k-th smallest number quickly from the multiplication table?

Given the height m and the length n of a m * n Multiplication Table, and a positive integer k, you need to return the k-th smallest number in this table.

Example 1:
Input: m = 3, n = 3, k = 5
Output:
Explanation:
The Multiplication Table:
1	2	3
2	4	6
3	6	9

The 5-th smallest number is 3 (1, 2, 2, 3, 3).
Example 2:
Input: m = 2, n = 3, k = 6
Output:
Explanation:
The Multiplication Table:
1	2	3
2	4	6

The 6-th smallest number is 6 (1, 2, 2, 3, 4, 6).
"""

class Solution(object):
    def findKthNumber(self, m, n, k):
        low = 1
        high = m*n
        while low<high:
            mid = (low+high)/2
            lesseq, eq = self.countLesseq(m, n, mid)
            if k in range(lesseq - eq + 1, lesseq+1):
                return mid
            elif k <= lesseq-eq:
                high = mid - 1
            else:
                low = mid + 1
        return low

    def countLesseq(self, m, n, x):
        lesseq= 0
        eq = 0
        for i in range(1, m+1):
            div = min(x/i, n)
            if div*i==x:
                eq += 1
            lesseq += div
        return lesseq, eq

s = Solution()
print s.findKthNumber(3, 3, 5)
print s.findKthNumber(2, 3, 6)