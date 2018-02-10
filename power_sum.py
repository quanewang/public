# Find the number of ways that a given integer, , can be expressed as the sum of the  powers of unique, natural numbers.
#
# Input Format
#
# The first line contains an integer .
# The second line contains an integer .
#
# Constraints


# LESSON
#   typo
#   - power>N should be power>X
def powerSum(X, N):
    items = []
    item = 1
    while 1:
        power = pow(item, N)
        if power > X:
            break
        items.append(power)
        item = item + 1
    return checkSum(items, X, 0)


def checkSum(items, total, idx):
    if total < 0:
        return 0
    if not total:
        return 1
    if idx >= len(items):
        return 0
    return checkSum(items, total - items[idx], idx + 1) + checkSum(items, total, idx + 1)


print powerSum(10, 2)
print powerSum(100, 2)
print powerSum(100, 3)
print powerSum(2, 3)