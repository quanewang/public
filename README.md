All the subsets of an array

All permutations of a list of chars

A sorted list of the square of each element in a sorted list of integers

Quicksort with duplicates

Given a binary tree, find the maximum path sum. The path may start and end at any node in the tree.

We can rotate digits by 180 degrees to form new digits. 
When 0, 1, 6, 8, 9 are rotated 180 degrees, they become 
0, 1, 9, 8, 6 respectively. 
When 2, 3, 4, 5, and 7 are rotated 180 degrees, 
they become invalid. A confusing number is a number 
that when rotated 180 degrees becomes a different number 
with each digit valid.(Note that the rotated number 
can be greater than the original number.) 
Given a positive integer N, return the number 
of confusing numbers between 1 and N inclusive.

Given two words (beginWord and endWord), and a dictionary's word list, 
find the length of shortest transformation sequence from beginWord to endWord, 
such that: 1) Only one letter can be changed at a time and, 
2) Each transformed word must exist in the word list.

Given a matrix of N rows and M columns. From m[i][j],
 we can move to m[i+1][j], if m[i+1][j] > m[i][j], or 
 can move to m[i][j+1] if m[i][j+1] > m[i][j]. 
 The task is print longest path length if we start from (0, 0).

Given a robot cleaner in a room modeled as a grid. 
Each cell in the grid can be empty or blocked. 
The robot cleaner with 4 given APIs can move forward,
 turn left or turn right. Each turn it made is 90 degrees. 
 When it tries to move into a blocked cell, its bumper 
 sensor detects the obstacle and it stays on the current cell. 
 Design an algorithm to clean the entire room using only the 4 given APIs shown below." (Solution)


Given an encoded string, return its decoded string.

Implement a SnapshotArray that supports pre-defined interfaces (note: see link for more details). 

In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.) We may rotate the i-th domino, so that A[i] and B[i] swap values. Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same. If it cannot be done, return -1.

Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times. You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Given a list of query words, return the number of words that are stretchy." Note: see link for more details. 

Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.


Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Your car starts at position 0 and speed +1 on an infinite number line. (Your car can go into negative positions.) Your car drives automatically according to a sequence of instructions A (accelerate) and R (reverse)...Now for some target position, say the length of the shortest sequence of instructions to get there." 

Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a subsequence of W. If there is no such window in S that covers all characters in T, return the empty string "". If there are multiple such minimum-length windows, return the one with the left-most starting index.

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down). Find all strobogrammatic numbers that are of length = n.

Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root. The length of path between two nodes is represented by the number of edges between them.

Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive). The binary search tree is guaranteed to have unique values.

A group of two or more people wants to meet and minimize the total travel distance. You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Given a matrix and a target, return the number of non-empty submatrices that sum to target.

Given an array of numbers and a target integer, find three elements from the array that sums up to target. Return the value of these three elements (0-based). (Note: This is different from Two Sum where you had to return the indices)
The triplet of the values returned should be sorted. If multiple such values exist, break ties by returning the triplet with the least first value. If there are still multiple such triplets with same first value, return the triplet with the least second value. If there are still multiple such triplets with same first and second values, return the triplet with the least third value. If there is no triplet that sums to target, return an empty array.
Sample 0
Input
nums: [1, 2, 3, 3, 4, 1, 1]
target: 6
Output
[1, 2, 3]
Sample 1
Input
num: [1, 2, 3, 3, 4, 1, 1]
target: 100
Output
[]


You have to find all the permutations of integers from 1 to n without using the permutation related library functions in your code.
Sample 0
Input
n: 2
Output
[ [ 1 , 2 ] , [ 2 , 1 ] ]
Sample 1
Input
n: 3
Output
[ [ 1 , 2 , 3 ] , [ 1 , 3 , 2 ] , [ 2 , 1 , 3 ] , [ 2 , 3 , 1 ] , [ 3 , 2 , 1 ] , [ 3 , 1 , 2 ] ]


Given an array of array of integers arrs and a random permutation p of first n integers {1,2,...,n}. Find if the given permutation p is the smallest supersequence of arrs.
A sequence is said to be a supersequence if it contains all arrays in arrs as subsequences.
A supersequence A is said to be smaller than another supersequence B, if A has less length than B. If both have same length, lexicographically smaller sequence is smaller.
Sample 0
Input
arrs:[[1,3],[2,3]]
p:[2,1,3]
Output
false
Explanation
[1,2,3] is the smallest supersequence in this case.
Sample 1
Input
arrs:[[1,2],[3,2]]
p:[1,3,2]
Output
true

Given a binary matrix a comprising only 0's and 1's. You need to find the area of the largest rectangle containing only 1's.
Note - Return the single integer which is the required area.
Sample 0
Input
[[1,1]]
Output
2
Sample 1
Input
[[1,0]]
Output
1
Largest Rectangle in Histogram
[2, 3, 4, 2, 2] 10
[2, 1, 5, 6, 2, 3] 10

Minimum Jumps
Given an array of non negative numbers, each element in the array reprents maximum jump length from that position. Initially you are at first position (0th index) of the array and you want to go to the last position. Find minimum number of jumps you need to make to reach the last position.
Note that there is always a way to reach the last position.
Sample 0
Input
[2,1,3,5,1]
Output
2
Explanation
We can jump 2 steps from index 0 to 2 and then 2 steps from index 2 to 4. So, minimum number of jumps to reach to the last position is 2.
Sample 1
Input
[1,4,2,6,3]
Output
2

Given N jobs, where i-th job is scheduled to be done from startTime[i] to endTime[i], with a profit of profit[i].

You need to output the maximum profit that can be made by selecting jobs such that, no two jobs are overlapping in the time range.
Note:
If you finish a job at time T, you can start another job at time T.
Sample 0
Input
startTime: [1, 3, 7, 2]
endTime: [2, 4, 19, 17]
profit: [5, 2, 10, 20]
Output
25


Trapping 2D Rainwater
Rocky is an architect. He likes to build different unique structures.
He made structure of pillars of the same width and breadth but having different heights in a region.
He wants to find out, maximum volume of water the structure can hold when it rains.
Given N x M matrix heights where,
heights[ i ][ j ] = height of pillar at ( i, j )
Return the maximum volume of water the structure can hold.
Sample 0
Input
heights:

	[
		[5, 5, 5, 5],
		[5, 0, 0, 5],
		[5, 0, 0, 5],
		[5, 5, 5, 5]
	]
Output
20
Sample 1
Input
heights:
	[
		[1, 2, 5, 9],
		[3, 2, 6, 11],
		[4, 9, 2, 7],
		[7, 8, 9, 10]
	]
Output
4
Explanation
Only pillar at (2,2) with height 2 can hold water of 4 cubic units.

Best Cover of Array
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
