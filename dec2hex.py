"""
convert decimal to hex
a=10
b=11
c=12

Given an integer, write an algorithm to convert it to hexadecimal.
For negative integer, twos complement method is used.

Note:
All letters in hexadecimal (a-f) must be in lowercase.
The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
The given number is guaranteed to fit within the range of a 32-bit signed integer.
You must not use any method provided by the library which converts/formats the number to hex directly.
Example 1:

Input:
26

Output:
"1a"
Example 2:

Input:
-1
Output:
"ffffffff"
"""

def hex(n):
    result = ''
    while n:
        rem = n%16
        result += map(rem)
        n = n/16
    print result

def map(n):
    if n<10:
        return str(n)
    else:
        return chr(ord('a') + n - 10)

hex(26)
