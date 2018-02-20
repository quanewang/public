
"""
Given an integer array of size n, find the maximum of the minimums 
of every window size in the array. Note that window size varies from 1 to n.

Example:
Input: 
10 20 30 50 10 70 30
10 20 30

Output: 
70 30 20 10 10 10 10 
30 20 10

Explaination:
Input:  arr[] = {10, 20, 30, 50, 10, 70, 30}
Output:         70, 30, 20, 10, 10, 10, 10

First element in output indicates maximum of minimums of all 
windows of size 1.
Minimums of windows of size 1 are {10}, {20}, {30}, {50}, {10},
{70} and {30}.  Maximum of these minimums is 70

Second element in output indicates maximum of minimums of all 
windows of size 2.
Minimums of windows of size 2 are {10}, {20}, {30}, {10}, {10},
and {30}.  Maximum of these minimums is 30

Third element in output indicates maximum of minimums of all 
windows of size 3.
Minimums of windows of size 3 are {10}, {20}, {10}, {10} and {10}. 
Maximum of these minimums is 20

Similarly other elements of output are computed.
"""










