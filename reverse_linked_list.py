"""
-- LESSON
-- p==q

https://leetcode.com/problems/reverse-linked-list-ii/description/
"""
#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def printf(self):
        print self.val
        if self.next:
            self.next.printf()

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or m>=n or m<0 or n<0:
            return head
        count = 1
        p, q = head, head
        while count<m and p:
            q, p = p, p.next
            count += 1
        if count<m or not p:
            return head
        qm, pm = q, p
        while count<=n and p:
#            p, q, p.next=p.next, p, q
            tmp1, tmp2, tmp3 =p.next, p, q
            p, q, tmp2.next=tmp1, tmp2, tmp3
            count += 1
        if pm==qm:
            pm.next = p
        else:
            pm.next, qm.next=p, q
        if m==1:
            head = q
        return head




a = ListNode(3)
b = ListNode(5)
c = ListNode(6)
d = ListNode(7)
e = ListNode(8)
a.next = b
b.next = c
c.next = d
d.next = e
#a.printf()
s = Solution()
x = s.reverseBetween(b, 1,2)
x.printf()