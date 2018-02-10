
'''
LESSON
- if not stack and => if stack

A string of brackets is considered correctly matched if every opening
bracket in the string can be paired up with a later closing bracket,
and vice versa.
Examples:

input:  text = (()
output: 1

input:  text = (())
output: 0

input:  text = ())(
output: 2
'''

def bracket_match(text):
    if text is None:
        return 0
    stack = []
    count = 0
    for t in text:
        if t=='(':
            stack.append(t)
        else:
            if stack and stack[len(stack)-1]=='(':
                stack.pop()
            else:
                count += 1
    return count + len(stack)

print bracket_match("((")
print bracket_match("(()()")
print bracket_match("((")

