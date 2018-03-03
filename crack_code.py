"""
There is a box protected by a password. The password is n digits,
where each letter can be one of the first k digits 0, 1, ..., k-1.

You can keep inputting the password, the password will
automatically be matched against the last n digits entered.

For example, assuming the password is "345", I can open it when
I type "012345", but I enter a total of 6 digits.

Please return any string of minimum length that is guaranteed to
open the box after the entire string is inputted.

Example 1:
Input: n = 1, k = 2
Output: "01"
Note: "10" will be accepted too.
Example 2:
Input: n = 2, k = 2
Output: "00110"
Note: "01100", "10011", "11001" will be accepted too.
"""

def dfs(n, k):
    path=str(0)*n
    return search(n, k, path, {})

def search(n, k, path, seen):
    if not n or not k:
        return ''
    word = path[len(path)-n:]
    seen[word]=1
    for x in range(k-1, -1, -1):
        if not (word[1:]+str(x)) in seen:
            return search(n, k, path+str(x), seen)
    return path

print dfs(1, 2)
print dfs(3, 3)