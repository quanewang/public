"""
Given a list, rotate the list to the right by k places, where k is non-negative.


Example:

Given 1->2->3->4->5->NULL and k = 2,

return 4->5->1->2->3->NULL.

https://leetcode.com/problems/rotate-list/description/

"""

# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        if not k:
            return head
        if not head:
            return head
        steps = 0
        p1 = head
        p2 = None
        while p1.next:
            p1 = p1.next
            steps += 1
            if steps == k:
                p2 = head
            elif steps>k:
                p2 = p2.next
        if not p2:
            len = steps + 1
            k = k%len
            return self.rotateRight(head, k)
        p1.next = head
        head = p2.next
        p2.next = None
        return head


