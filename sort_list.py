"""
Sort a linked list in O(n log n) time using constant space complexity.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        if not head:
            return head
        if not head.next:
            return head
        length = self.get_len(head)
        head1, head2 = self.cut(head, length/2)
        p1 = self.sortList(head1)
        p2 = self.sortList(head2)
        head = tail = None
        while p1 and p2:
            if p1.val>p2.val:
                p1, p2 = p2, p1
            if not head:
                head = tail = p1
            else:
                tail.next=p1
                tail = p1
            p1_next = p1.next
            p1.next = None
            p1 = p1_next
        if p1:
            tail.next=p1
        if p2:
            tail.next=p2
        return head

    def get_len(self, p):
        length = 0
        while p:
            p = p.next
            length += 1
        return length

    def cut(self, head, steps):
        p = head
        while steps>1:
            p = p.next
            steps -= 1
        p_next = p.next
        p.next = None
        return head, p_next

