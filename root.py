# note
# - est *= middle n-1 time to get n power
# - root(0.04, 2)
# - root(1, n)
# - root(n, 1)

import math

def root(x, n):
    if n == 1:
        return x
    if x == 1:
        return 1
    if x < 1:
        range = [x, 1]
    else:
        range = [1, x]
    while math.fabs(range[1] - range[0]) >= 0.001:
        middle = float(range[0] + range[1]) / float(2)
        counter = n - 1
        est = middle
        while counter:
            counter = counter - 1
            est = est * middle
        # print x, n, range[0], range[1], middle, est

        if est == x:
            break
        elif est > x:
            range[1] = middle
        else:
            range[0] = middle
    return middle


if __name__ == "__main__":
    print root(4, 2)
    print root(7, 1)
    print root(7, 3)
    print root(9, 2)
    print root(0.04, 2)