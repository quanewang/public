import heapq


class Solution(object):
    """
    Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
    https://leetcode.com/problems/merge-k-sorted-lists/description/
    """
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    def mergeKLists(self, lists):
        h = []
        k = len(lists)
        cursors = [lists[i] for i in range(k)]
        for i in range(k):
            if cursors[i]:
                heapq.heappush(h, (cursors[i].val, i))
                cursors[i]=cursors[i].next
        result=[]
        while h:
            val, i = heapq.heappop(h)
            result.append(val)
            if cursors[i]:
                heapq.heappush(h, (cursors[i].val, i))
                cursors[i]=cursors[i].next
        return result
    """
    Given a positive integer, output its complement number. The complement strategy 
    is to flip the bits of its binary representation.
    https://leetcode.com/problems/number-complement/description/
    """
    def findComplement(self, num):
        if not num:
            return 1
        x = 1
        while x<=num:
            num=num^x
            x=x<<1
        return num

    """
    Given an unsorted array, find the maximum difference between the successive elements in its sorted form.
    Try to solve it in linear time/space.
    """
    def maximumGap(self, nums):
