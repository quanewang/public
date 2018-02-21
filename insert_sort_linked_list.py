"""
Sort a linked list using insertion sort.
"""
# https://leetcode.com/problems/insertion-sort-list/description/
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        last = None
        while last!=head.next:
            node = prev = head
            cur_max_node = cur_max_prev = None
            while node.next and node.next!=last:
                if not cur_max_node or node.val > cur_max_node.val:
                    cur_max_node, cur_max_prev= node, prev
                prev, node = node, node.next
            if cur_max_node.val<=node.val:
                last = node
            else:
                if cur_max_node==cur_max_prev:
                    head = cur_max_node.next
                else:
                    cur_max_prev.next = cur_max_node.next
                node.next, cur_max_node.next = cur_max_node, node.next
                last = cur_max_node
        return head



