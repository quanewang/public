"""
Given an array arr of integers (not necessarily distinct),
we split the array into some number of chunks (partitions),
 and individually sort each chunk.  After concatenating them,
 the result equals the sorted array.

What is the most number of chunks we could have made?

Example 1:

Input: arr = [5,4,3,2,1]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3], which isn't sorted.
Example 2:

Input: arr = [2,1,3,4,4]
Output: 4
Explanation:
We can split into two chunks, such as [2, 1], [3, 4, 4].
However, splitting into [2, 1], [3], [4], [4] is the highest number of chunks possible.
"""
class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if not arr:
            return 0
        count = 1
        idx = len(arr)-1
        low = arr[idx]
        while idx>0:
            i = 0
            while i<idx and arr[i]<=low:
                i += 1
            if i==idx:
                idx -= 1
                count += 1
                low = min(low, arr[idx])
            else:
                while idx>i:
                    idx -= 1
                    low = min(low, arr[idx])
        return count

s = Solution()
print s.maxChunksToSorted([1,1,0,0,1])
print s.maxChunksToSorted([2,1,3,4,4])
print s.maxChunksToSorted([5,4,3,2,1])