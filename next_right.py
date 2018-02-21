"""
Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL

"""

class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        print self.connect_(root, [], 0)

    def connect_(self, node, lefts, depth):
        if not node:
            return
        if len(lefts)-1<depth:
            lefts.append(node)
        else:
            node.next = lefts[depth]
            lefts[depth] = node
        self.connect_(node.right, lefts, depth+1)
        self.connect_(node.left, lefts, depth+1)

