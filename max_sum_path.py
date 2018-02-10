'''
Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        path, partial = self.maxPathSumHelper(root)
        if path < partial:
            return partial
        return path

    def maxPathSumHelper(self, node):
        if not node:
            return None, None
        if not node.left and not node.right:
            return node.val, node.val

        path_left, partial_left = self.maxPathSumHelper(node.left)
        path_right, partial_right = self.maxPathSumHelper(node.right)

        path = None
        partial = None

        if path_left != None:
            path = path_left
            partial = partial_left

        if path_right != None:
            if path is None or path < path_right:
                path = path_right
            if partial is None or partial < partial_right:
                partial = partial_right

        if partial > 0:
            partial = partial + node.val
        else:
            partial = node.val

        potential_path = node.val
        if partial_left != None and partial_left > 0:
            potential_path += partial_left
        if partial_right != None and partial_right > 0:
            potential_path += partial_right
        path = max(path, potential_path)

        return path, partial

s=Solution()
n1 = TreeNode(-2)
n2 = TreeNode(1)
n3 = TreeNode(3)
n1.left = n2
n1.right = n3
print s.maxPathSum(n1)

n1 = TreeNode(-2)
n2 = TreeNode(1)
n1.left = n2
print s.maxPathSum(n1)

n1 = TreeNode(-2)
print s.maxPathSum(n1)

n1 = TreeNode(-2)
n2 = TreeNode(-1)
n1.left = n2
print s.maxPathSum(n1)

s=Solution()
n1 = TreeNode(-2)
n2 = TreeNode(0)
n3 = TreeNode(3)
n1.left = n2
n1.right = n3
print s.maxPathSum(n1)