"""
LESSON
-- if node.key == num: not necessary
-- if found => if found!=-1
-- o(height) time
-- space is constant if non recursive
-- non negative key value?

flatten tree
-- what if key is key.a.b?

Largest Smaller BST Key
Given a root of a Binary Search Tree (BST) and a number num, implement an efficient function findLargestSmallerKey that finds the largest key in the tree that is smaller than num. If such a number doesn’t exist, return -1. Assume that all keys in the tree are nonnegative.

Analyze the time and space complexities of your solution.

"""


def find_helper(self, node, num):
    if not node:
        return -1
    if node.key < num:
        found = self.find_helper(node.right, num)
        if found != -1:
            return found
        return node.key
    else:  # node.key >= num
        return self.find_helper(node.left, num)
