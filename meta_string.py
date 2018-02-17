"""
Given two strings, the task is to check whether these strings are meta strings or not. Meta strings are the strings which can be made equal by exactly one swap in any of the strings. Equal string are not considered here as Meta strings.

Examples:

Input : A = "geeks"
        B = "keegs"
Output : 1
By just swapping 'k' and 'g' in any of string,
both will become same.

Input : A = "rsting"
        B = "string
Output : 0
"""

def meta_string(a, b):
    if not a or not b:
        return 0
    if len(a)!=len(b):
        return 0
    diffs = []
    for i in range(len(a)):
        if a[i]!=b[i]:
            diffs.append(i)
    if len(diffs)==2 and a[diffs[0]] == b[diffs[1]] and a[diffs[1]]==b[diffs[0]]:
        return 1
    return 0

print meta_string('geeks', 'keegs')
print meta_string('rsting', 'string')