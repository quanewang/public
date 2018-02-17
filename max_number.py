"""
LESSON
-- list(nums) list(ops)
-- if not ops => if ops

Given a string of numbers, the task is to find the maximum value from the string,
you can add a + or * sign between any two numbers.
Note: Add sign between two numbers on the basis of numbers not on the value calculated till that number.
For eg: n = 5120
(((5  + 1 )  + 2 )  + 0 ) = 8 is right.

5120
(((5  + 1 )  * 2 )  + 0 ) =  12 is wrong.

"""

def max_number(nums):
    if not nums:
        return 0, []
    max_value, max_ops = max_number_helper(nums, [])
    print max_value, max_ops

def max_number_helper(nums, ops):
    if len(ops)>=len(nums)-1:
        print ops, nums
        return compute(list(nums), list(ops)), ops
    ops.append('*')
    value1, ops1 = max_number_helper(nums, list(ops))
    ops.pop()
    ops.append('+')
    value2, ops2 = max_number_helper(nums, list(ops))
    ops.pop()
    if value1<value2:
        value1, ops1 = value2, ops2
    return value1, ops1

def compute(nums, ops):
    while ops:
        op = ops.pop()
        if op == '*':
            nums.append(nums.pop() * nums.pop())
        else:
            operand = nums.pop()
            while ops and ops[-1]=='*':
                ops.pop()
                nums.append(nums.pop() * nums.pop())
            nums.append(operand + nums.pop())
    return nums.pop()

max_number([5, 2, 1, 0])
