"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if not nums1 and not nums2:
            return 0
        if nums1 is None:
            nums1=[]
        if nums2 is None:
            nums2=[]
        total = len(nums1) + len(nums2)
        k = (total+1)/2
        if total % 2:
            return self.findSmallestK(nums1, nums2, k)
        else:
            return float(self.findSmallestK(nums1, nums2, k) + self.findSmallestK(nums1, nums2, k+1))/2

    def findSmallestK(self, a, b, k):
        if len(a)>len(b):
            a, b = b, a
        if not a:
            return b[k-1]
        m = len(a) + len(b)
        if k==m:
            return max(a[-1], b[-1])
        i = len(a)/2
        j = k-i-1
        if (a[i]==b[j]):
            return max(a[i], b[j])
        elif a[i]<b[j]:
            return self.findSmallestK(a[i:], b[:j], k-i)
        else:
            return self.findSmallestK(a[:i], b[j:], k-j)


nums1 = [1, 2, 3, 4]
nums2 = [3, 4, 6, 8, 9]
s = Solution()
# print s.findMedianSortedArrays(nums1, nums2)
print s.findMedianSortedArrays([1, 2], [1,2])
print s.findMedianSortedArrays([1], [3,4])
print s.findMedianSortedArrays([], [3,4])
print s.findMedianSortedArrays([1,2], [3,4])
print s.findMedianSortedArrays([1, 1, 1], [1,1,1])
print s.findMedianSortedArrays([1], [1,2,3])
print s.findMedianSortedArrays([1, 2], [3,4])
print s.findMedianSortedArrays([1], [2,3])
print s.findMedianSortedArrays([1, 3], [2])
print s.findMedianSortedArrays([3], [1, 2, 4])