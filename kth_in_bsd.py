def kth(node, n):
    result= visit(node, [n])
    return result

def visit(node, nn):
    if not node:
        return None
    if not nn[0]:
        return node.val
    result = kth(node.left, nn)
    if result!=None:
        return result
    nn[0] = nn[0] - 1
    if not nn[0]:
        return node
    return kth(node.right, nn)
