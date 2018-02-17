"""
Given a preorder traversal of a BST, print the leaf nodes of the tree without building the tree.
https://practice.geeksforgeeks.org/problems/print-leaf-nodes-from-preorder-traversal-of-bst/0
890 325 290 530 965
3 2 4
"""
def leaf(nums):
    leaves = []
    leaf_helper(nums, 0, len(nums)-1, leaves)
    return leaves

def leaf_helper(nums, low, high, leaves):
    if low>high:
        return
    if low==high:
        leaves.append(nums[low])
    i=low+1
    while i<=high and nums[i]<nums[low]:
        i += 1

    leaf_helper(nums, low+1, i-1, leaves)
    leaf_helper(nums, i, high, leaves)

print leaf([3, 2, 4])
print leaf([890 ,325, 290, 530, 965])