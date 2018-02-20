"""
Given a string s1, we may represent it as a binary tree
by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.
"""

def isScramble(s1, s2):
    if not s1 or not s2:
        return False
    if len(s1)!=len(s2):
        return False
    if len(s1) == 1:
        return s1[0]==s2[0]
    even = len(s1) % 2 ==0
    if even:
        mid = len(s1) / 2 - 1
        return isScramble(s1[mid + 1:], s2[mid + 1:]) and isScramble(s1[:mid + 1], s2[:mid + 1]) \
               or isScramble(s1[mid + 1:], s2[:mid + 1]) and isScramble(s1[:mid + 1], s2[mid + 1:])
    else:
        mid = len(s1) / 2 - 1
        return isScramble(s1[mid + 1:], s2[mid + 1:]) and isScramble(s1[:mid + 1], s2[:mid + 1]) \
               or isScramble(s1[mid + 1:], s2[:mid + 2]) and isScramble(s1[:mid + 1], s2[mid + 2:])


print isScramble("great", "rgtae")
print isScramble("eat", "tae")
print isScramble("ea", "ae")
print isScramble("eat", "aet")
