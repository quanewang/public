"""
LESSON
--  current += stack.pop() => current = stack.pop() + current
--  current = current * stack[-1] => current = current * stack.pop()
--  if stack[-1] => if stack

An encoded string (s) is given, the task is to decode it.
The pattern in which the strings were encoded were as follows
original string: abbbababbbababbbab
encoded string : "3[a3[b]1[ab]]".

abbbab
"""

def decode(text):
    stack = []
    current = ''
    for x in text:
        if x>'0' and x<='9':
            if current:
                stack.append(current)
                current = ''
            stack.append(int(x))
        elif x>='a' and x<='z':
            current = current + x
        elif x==']':
            if stack and type(stack[-1])==int:
                current = current * stack.pop()
            if stack and type(stack[-1]) == str:
                current = stack.pop() + current
    while stack and type(stack[-1])==int:
        current = current * stack.pop()

    if stack:
        raise Exception
    return current

print decode("3[a3[b]1[ab]]")