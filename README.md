### Problems

All the subsets of an array

All permutations of a list of chars

### Best Cover of Array
Given an array A consisting of only 0s and 1s. You can perform the following operation on the array:

choose any contiguous subarray of length at most K and change all the elements of the subarray to 1.

You goal is to find the minimum number of 0s remaining in the array after performing the operation at most Q times.

Sample 0
Input
A : [0, 0, 0, 1, 1, 1]
K : 2
Q : 2

Output
0

Explanation
We can perform the operation once on the subarray [1, 2],
the array becomes, [1, 1, 0, 1, 1].
Then we perform the operation on the subarray [3, 3],
The array becomes, [1, 1, 1, 1, 1]

Sample 1
Input
A : [1, 0, 0, 0, 1, 1]
K : 2
Q : 1

Output
1
