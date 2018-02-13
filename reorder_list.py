"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 1-2
class Solution(object):
    def reorderList(self, head):
        if not head or not head.next:
            return
        len = 1
        tail = head
        while tail.next:
            tail = tail.next
            len += 1
        middle = head
        for i in range(len/2):
            middle = middle.next
        p, q = head, middle.next
        middle.next = None
        q = self.reverse(q)
        while q:
            p1, p2 = p.next, q.next
            p.next, q.next = q, p1
            p, q = p1, p2

    def reverse(self, head):
        if not head:
            return
        p = head
        q = p.next
        p.next = None
        while q:
            tmp = q
            q = q.next
            tmp.next = p
            p = tmp
        return p



