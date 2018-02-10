#recursive
def inc(num):
    if not num:
        return [1]
    lastDigit = num[len(num)-1]
    newNum = num
    if lastDigit < 9:
        newNum.pop(len(newNum)-1)
        newNum.append(lastDigit+1)
    else:
        newNum.pop(len(newNum) - 1)
        newNum = inc(newNum)
        newNum.append(0)

    return newNum


print inc([])
print inc([9])
print inc([1, 3, 2, 4])
print inc([1, 3, 2, 9])
print inc([9, 9,9,9])

# iterative
def inc2(num):
    if not num:
        return [1]
    result = [0] * len(num)
    carry = 1
    for i in range(len(num)-1, 0, -1):
        digit = num[i]+carry
        if digit==10:
            carry = 1
        else:
            result[i] = digit
            carry = 0
    if carry:
        result.insert(0, 1)
    return result



print inc2([])
print inc2([9])
print inc2([1, 3, 2, 4])
print inc2([1, 3, 2, 9])
print inc2([9, 9,9,9])

