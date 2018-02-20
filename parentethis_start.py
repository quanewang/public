"""
Given a string containing only three types of characters: '(', ')' and '*',
write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
Example 1:
Input: "()"
Output: True
Example 2:
Input: "(*)"
Output: True
Example 3:
Input: "(*))"
Output: True
"""
def checkValidString(s):
    if not s:
        return True
    return valid(s, 0, [])

def valid(s, idx, progress):
    if idx>=len(s):
        return is_valid(progress)
    if s[idx]=='*':
        for x in ['(', '', '}']:
            progress.append(x)
            result = valid(s, idx+1, progress)
            progress.pop()
            if result:
                return True
        return False
    else:
        progress.append(s[idx])
        result = valid(s, idx + 1, progress)
        progress.pop()
        return result

def is_valid(progress):
    if not progress:
        return True
    stack = []
    for x in progress:
        if x=='(':
            stack.append(x)
        elif x == ')':
            if stack and stack[-1]=='(':
                stack.pop()
            else:
                return False
    return not stack

print checkValidString("(*))")

