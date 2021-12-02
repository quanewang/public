### Sources

codedrills
* https://codedrills.io/drills/google

interviewbit
* https://www.interviewbit.com/search/?q=Google
* https://www.interviewbit.com/facebook-interview-questions/#questions

leetcode
* https://leetcode.com/discuss/interview-question/352460/Google-Online-Assessment-Questions

geeksforgeeks
* https://www.geeksforgeeks.org/n3-repeated-number-array-o1-space/

### Problems
All the subsets of an array

All permutations of a list of chars

A sorted list of the square of each element in a sorted list of integers

Quicksort with duplicates

Given a binary tree, find the maximum path sum. The path may start and end at any node in the tree.

Binary insertion

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

Add Two Numbers As Lists.

Given 2 non negative integers m and n, find gcd(m, n).
### Deletion Distance
The deletion distance of two strings is the minimum number of characters you need to delete in the two strings in order to get the same string. For instance, the deletion distance between "heat" and "hit" is 3:

By deleting 'e' and 'a' in "heat", and 'i' in "hit", we get the string "ht" in both cases.
We cannot get the same string from both strings by deleting 2 letters or fewer.
Given the strings str1 and str2, write an efficient function deletionDistance that returns the deletion distance between them. Explain how your function works, and analyze its time and space complexities.
```
Examples:

input:  str1 = "dog", str2 = "frog"
output: 3

input:  str1 = "some", str2 = "some"
output: 0

input:  str1 = "some", str2 = "thing"
output: 9

input:  str1 = "", str2 = ""
output: 0
```

### Median of Array

There are two sorted arrays A and B of size m and n respectively.

Find the median of the two sorted arrays ( The median of the array formed by merging both the arrays ).

The overall run time complexity should be O(log (m+n)).
```
Sample Input
A : [1 4 5]
B : [2 3]
Sample Output
3
NOTE: IF the number of elements in the merged array is even, then the median is the average of n / 2 th and n/2 + 1th element. 
For example, if the array is [1 2 3 4], the median is (2 + 3) / 2.0 = 2.5
```
```
class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def binSearch(self, A, k):
        l=0
        r=len(A)-1
        while l<r:
            m = (l+r)//2
            if A[m]==k:
                l=m
                r=m
                break
            if A[m]<k:
                l = m+1
            else:
                r = m-1
        return r
    def findMedianSortedArrays(self, A, B):
        l = len(A) + len(B)
        i = (len(A) + len(B))//2
        if l%2==0:
            m1 = self._findMedianSortedArrays(A, B, i)
            m2 = self._findMedianSortedArrays(A, B, i-1)
            return (m1+m2)//2
        else:
            return self._findMedianSortedArrays(A, B, i)

    def _findMedianSortedArrays(self, A, B, i=-1):

        if not A:
            return B[i]
        if not B:
            return A[i]
        ma = len(A)//2
        mb = self.binSearch(B, A[ma])
        if ma+mb+1==i:
            return A[ma]
        elif ma+mb+1>i:
            return self._findMedianSortedArrays(A[0:ma], B[0:mb+1], i)
        else:
            return self._findMedianSortedArrays(A[ma+1: len(A)], B[mb+1: len(B)], i-ma-mb-2)
```

### Next Smallest Palindrome!

Given a numeric string A representing a large number you need to find the next smallest palindrome greater than this number.

Problem Constraints
1 <= |A| <= 100

A doesn't start with zeroes and always contain digits from 0-9.

Input Format
First and only argument is an string A.

Output Format
Return a numeric string denoting the next smallest palindrome greater than A.
```
Example Input
Input 1:

 A = "23545"
Input 2:

 A = "999"


Example Output
Output 1:

 "23632"
Output 2:

 "1001"
```

```
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        odd = len(A)%2==1
        m = len(A)//2
        if odd:
          first = A[0:m]
          second = A[m+1:len(A)]
        else:
          first = A[0:m-1]
          second = A[m+1:len(A)]
          if A[m]!=A[m-1]:
              return first + max(A[m-1], A[m])+ max(A[m-1], A[m]) + first[::-1]
        if first and second:
          first_num = int(first)
          second_num = int(second[::-1])
          if int(first[::-1]) > int(second):
            if odd:
                return first+A[m]+first[::-1]
            else:
                return first+A[m-1]+A[m]+first[::-1]

        if A[m]!='9':
            if odd:
                return first + str(int(A[m])+1) + first[::-1]    
            else:
                return first + str(int(A[m])+1) + str(int(A[m])+1) + first[::-1]    
        found = False
        for i in range(len(first)-1, -1, -1):
            if i<'9':
                first[i]=str(int(i)+1)
                found=True
        if found:
          if odd:
            return first + '0' + first[::-1]    
          else:
            return first + '00' + first[::-1]          
        return '1'+'0'*(len(A)-1)+'1'
```
### Rotate Digits
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

### Shortest Transformation
Given two words (beginWord and endWord), and a dictionary's word list, 
find the length of shortest transformation sequence from beginWord to endWord, 
such that: 
* Only one letter can be changed at a time and, 
* Each transformed word must exist in the word list.

### Longest Path
Given a matrix of N rows and M columns. From m[i][j],
 we can move to m[i+1][j], if m[i+1][j] > m[i][j], or 
 can move to m[i][j+1] if m[i][j+1] > m[i][j]. 
 The task is print longest path length if we start from (0, 0).

### Robot Cleaner
Given a robot cleaner in a room modeled as a grid. 
Each cell in the grid can be empty or blocked. 
The robot cleaner with 4 given APIs can move forward,
 turn left or turn right. Each turn it made is 90 degrees. 
 When it tries to move into a blocked cell, its bumper 
 sensor detects the obstacle and it stays on the current cell. 
 Design an algorithm to clean the entire room using only the 4 given APIs shown below." (Solution)


### Three Sum
Given an array of numbers and a target integer, find three elements from the array that sums up to target. Return the value of these three elements (0-based). (Note: This is different from Two Sum where you had to return the indices)
The triplet of the values returned should be sorted. If multiple such values exist, break ties by returning the triplet with the least first value. If there are still multiple such triplets with same first value, return the triplet with the least second value. If there are still multiple such triplets with same first and second values, return the triplet with the least third value. If there is no triplet that sums to target, return an empty array.

```
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
```
### All Permutations
You have to find all the permutations of integers from 1 to n without using the permutation related library functions in your code.
```
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
```

### Smallest Supersequences 
Given an array of array of integers arrs and a random permutation p of first n integers {1,2,...,n}. Find if the given permutation p is the smallest supersequence of arrs.
A sequence is said to be a supersequence if it contains all arrays in arrs as subsequences.
A supersequence A is said to be smaller than another supersequence B, if A has less length than B. If both have same length, lexicographically smaller sequence is smaller.
```
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
```
### Largest Rectangle 
Given a binary matrix a comprising only 0's and 1's. You need to find the area of the largest rectangle containing only 1's.
Note - Return the single integer which is the required area.
```
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
```

### Minimum Jumps
Given an array of non negative numbers, each element in the array reprents maximum jump length from that position. Initially you are at first position (0th index) of the array and you want to go to the last position. Find minimum number of jumps you need to make to reach the last position.
Note that there is always a way to reach the last position.
```
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
```

### Max Profit
Given N jobs, where i-th job is scheduled to be done from startTime[i] to endTime[i], with a profit of profit[i].

You need to output the maximum profit that can be made by selecting jobs such that, no two jobs are overlapping in the time range.
Note:
If you finish a job at time T, you can start another job at time T.
```
Sample 0
Input
startTime: [1, 3, 7, 2]
endTime: [2, 4, 19, 17]
profit: [5, 2, 10, 20]
Output
25
```
### Grid Unique Paths

A robot is located at the top-left corner of an A x B grid (marked ‘Start’ in the diagram below).

Path Sum: Example 1

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked ‘Finish’ in the diagram below).

How many possible unique paths are there?

Note: A and B will be such that the resulting answer fits in a 32 bit signed integer.

Example :
```
Input : A = 2, B = 2
Output : 2

2 possible routes : (0, 0) -> (0, 1) -> (1, 1) 
              OR  : (0, 0) -> (1, 0) -> (1, 1)
```	      
### Trapping 2D Rainwater
Rocky is an architect. He likes to build different unique structures.
He made structure of pillars of the same width and breadth but having different heights in a region.
He wants to find out, maximum volume of water the structure can hold when it rains.
Given N x M matrix heights where,
heights[ i ][ j ] = height of pillar at ( i, j )
Return the maximum volume of water the structure can hold.
```
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
```

### Best Cover of Array
Given an array A consisting of only 0s and 1s. You can perform the following operation on the array:
choose any contiguous subarray of length at most K and change all the elements of the subarray to 1.
You goal is to find the minimum number of 0s remaining in the array after performing the operation at most Q times.
```
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
```
### overlapping intervals 
Given a collection of intervals, find out how many intervals have to be removed to ensure that no interval is overlapping over another. An interval is not considered overlapping if it starts where the previous one ends.
```
For e.g., [0, 1] and [1, 2] are not overlapping intervals while [0, 2] and [1, 2] are. Here’s an example:

Input: [0, 3], [9, 12], [3, 8], [8, 10]
Answer: 1
In this case, if [8, 10] is removed, there will be no overlapping between the others. Here’s another example:

Input: [0,5], [1, 2], [3, 5]
Answer: 1
In this case, if [0, 5] is removed, there will be no overlapping between the others.
```


### Shortest Palindrome
Given a string s.

You need to convert the string into a palindrome by appending any characters in front of the given string s.

Return the single string res which is the shortest palindrome after this transformation.

Sample 0
```
Input
s: eedoc

Output
res: codeedoc
```
Sample 1
```
Input
s: aabaaa

Output
res: aaabaaa
```
### Minimizing Largest Sum
You are given an array nums (containing non-negative integers) and an integer m. You can split the original array nums into m non-empty continuous subarrays.

There can be size of nums - 1Cm - 1 total ways to split the array nums into m subarrays.

Consider a function f(way) which accepts a way to split an array nums hence m subarrays will be created, f(way) returns max(sumsubarray_1, sumsubarray_2, ...., sumsubarray_m).

You have to find min(f(way1), f(way2),....., f(waytotal_ways)).

Note: Sum of all elements of array nums is guaranteed to fit in a 32-bit integer.

Sample 0
```
Input
nums: [5, 6]
m: 1

Output
11

Explanation
As the array can be splitted in only 1 array then it will be the original array nums only contaning sum 11.
```
Sample 1
```
Input
nums: [7, 9, 9]
m: 2

Output
16

Explanation
The array nums can be splitted in 2 subarrays in following ways:

[7], [9,9]
[7, 9], [9]

The first split have sums of subarrays (7, 18), so max(7, 18) = 18.
The second split have sums of subarrays (16, 9), so max(16, 9) = 16
Our final answer is min(18, 16) = 16.
```

### Coins in the Path
There is a stone-path in Mario land. Mario will always start from the first stone and he wants to reach last stone with minimum cost.
Each stone has a cost to jump on it given in the array. Mario has jump ability represented by steps i.e he can jump to any stone in range [ i + 1, i + steps ] when standing on stone at i'th-index.

Given an integer array array of length N and an integer steps where,

N = Number of stones
array[i] = Cost to jump on ith-stone
steps = Mario's jump ability

Note: if array[i] == -1 then Mario can't jump on that stone.

Return the path of indexes (0-based indexing) with the smallest cost. If there are multiple paths with the smallest cost, then return lexicographically smallest one.
If no possible path is found then return an empty array.
```
Sample 0
Input
array: [1, 3, 2, -1, 1]
steps: 2

Output
[0, 2, 4]

Explanation
There is only one minimum cost path possible starting from index-0 is 0, 2, 4 with cost 1 + 2 + 1 = 4

Sample 1
Input
array: [2, 3, 5, 3, 1]
steps: 3

Output
[0, 1, 4]

Explanation
There are two paths possible 0, 1, 4 and 0, 3, 4 with same cost 2 + 3 + 1 = 6.So lexicographically smaller path is our answer i.e 0, 1, 4.
```

### Longest D-Subsequence
You are given an array arr and integer d. Find longest non-decreasing subsequence of arr such that the difference between consecutive elements of the sequence is less than d.
Value of d is small.
Note - A subsequence is a sequence that can be derived from the given sequence by deleting zero or more elements without changing the order of the remaining elements.
```
Sample 0
Input
arr: [1]
d: 1

Output
1

Explanation
Array only has a single sequence satisfying this property.

Sample 1
Input
arr: [1, 3, 2, 4, 5]
d: 2

Output
3

Explanation
Array only has a sequence [3, 4, 5] satisfying this property.

```
### The Skyline Problem
Skyline: A skyline is the outline or shape created by a city's overall structure, which is formed when the sky meets buildings or the land.

You are given N rectangular buildings in a 2-dimensional city, your task is to compute the skyline of these buildings, eliminating hidden lines, when viewed from a distance.

All buildings share common bottom and every building is represented by a triplet (left, right, height) where,
‘left’: is x coordinate of left side (or wall).
‘right’: is x coordinate of right side
‘height’: is height of the building.

A skyline is a collection of rectangular strips. As shown in the figure B, rectangular strip is represented as a pair (left, ht) (Red Points) where left is x coordinate of left side of strip and ht is height of strip.

You should return all such points in increasing order of left(x-coordinate) along with the last point, which is termination point indicating end of skyline.
The height of termination point is always zero.

Note:
There should not be any consecutive points with equal height in the output skyline.
Eg: If the output skyline is [[1,3], [2,5], [3,5], [4,0]], it must be resolved by taking only the leftmost point and eliminating the rest with same height.
So, the vaild output will be [[1,3], [2,5], [4,0]].

FIGURE A Figure A FIGURE B Figure B
Note:

There will be atleast 1 building present.
Height of each building will be atleast 1.
Input buildings will be sorted in increasing order of left coordinate.
```
Sample 0
Input
buildings: [[1,3,4], [2,5,8], [4,8,2], [6,7,5]]

Output
[[1,4], [2,8], [5,2], [6,5], [7,2], [8,0]]
Note: This Example is of the skyline shown in figure above.

Sample 1
Input
buildings: [[1,3,4]]

Output
[[1,4], [3,0]]
```
###  Expression Calculator
Evaluate the given valid mathematical expression consisting of non-negative integers with operators +,*,-,/. You may assume, the answer can be evaluated using a 64-bit signed integer. Evaluation must follow the standard mathematical rules.
```
Sample 0
Input
s: "1+2*6/4"

Output
4

Sample 1
Input
s: "120-190*2/5+4"

Output
48
```

### Search in rotated sorted array
Given an array of integers nums of size N and an integer target.

array nums is rotated at some pivot unknown to you beforehand.

Example : [0, 1, 2, 4, 5, 6, 7] might become [4, 5, 6, 7, 0, 1, 2].

You are given a target value to search. Find if the target exists in the array.

You may assume no duplicate exists in the array.

Note:

Array nums was sorted in non-decreasing order before rotation.
Do not sort the array.
Expected a solution better than linear search.
Do not use inbuilt functions.
target and array elements can be positive, 0 or negative.
```
Sample 0
Input
nums = [4, 5, 6, 7, 0, 1, 2, 3]

Target: 4

Output
true

Sample 1
Input
nums = [5, 17, 100, 3]

Target: 6

Output
false
```
### Rotate Matrix

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

You need to do this in place.

Note that if you end up using an additional array, you will only receive partial score.

Example:
```
If the array is

[
    [1, 2],
    [3, 4]
]
Then the rotated array becomes:

[
    [3, 1],
    [4, 2]
]
```

### Majority Element
Write a function which takes an array and prints the majority element (if it exists), otherwise prints “No Majority Element”. A majority element in an array A[] of size n is an element that appears more than n/2 times (and hence there is at most one such element). 

Examples : 
```
Become a success story instead of just reading about them. Prepare for coding interviews at Amazon and other top product-based companies with our Amazon Test Series. Includes topic-wise practice questions on all important DSA topics along with 10 practice contests of 2 hours each. Designed by industry experts that will surely help you practice and sharpen your programming skills. Wait no more, start your preparation today!

Input : {3, 3, 4, 2, 4, 4, 2, 4, 4}
Output : 4
Explanation: The frequency of 4 is 5 which is greater
than the half of the size of the array size. 

Input : {3, 3, 4, 2, 4, 4, 2, 4}
Output : No Majority Element
Explanation: There is no element whose frequency is
greater than the half of the size of the array size.
```

### N/3 Repeat Number

You're given a read only array of n integers. Find out if any integer occurs more than n/3 times in the array in linear time and constant additional space.
If so, return the integer. If not, return -1.

If there are multiple solutions, return any one.

Example:
```
Input : [10, 10, 20, 30, 10, 10]
Output : 10
10 occurs 4 times which is more than 6/3.

Input : [20, 30, 10, 10, 5, 4, 20, 1, 2]
Output : -1
```
### Max Distance

Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].

```
Example Input
Input 1:

 A = [3, 5, 4, 2]


Example Output
Output 1:

 2


Example Explanation
Explanation 1:

Maximum value occurs for pair (3, 4).
```
### Google 1
#### Round 1: Single Number-ii

https://leetcode.com/problems/single-number-ii
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 
```
Example 1:

Input: nums = [2,2,3,2]
Output: 3
Example 2:

Input: nums = [0,1,0,1,0,1,99]
Output: 99
 

Constraints:

1 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
Each element in nums appears exactly three times except for one element which appears once.
```
#### Round 2: Decode String

https://leetcode.com/problems/decode-string

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

 
```
Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"
```

#### Round 3:

Given a tree representation of a html parsed output, wherein every block is a node in the tree, find if two html docs contain the same text.

#### Round 4:

Given a 2D matrix M X N, support two operations:
Query(row1, col1, row2, col2) such that I get the sum of all numbers in the rectangle ((row1, col1), (row1, col2), (row2, col1), (row2, col2)) and
Update(row, col) to a new number

And query is a very frequent operation and update is a rare operation, so query should be really fast, but update can be slower.

Follow up: How would you solve this in a distributed fashion

#### Round 5:

https://leetcode.com/problems/toeplitz-matrix

Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

```
Example 1:
Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: true
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
Example 2:


Input: matrix = [[1,2],[2,2]]
Output: false
Explanation:
The diagonal "[1, 2]" has different elements.
Follow-up: assume that the whole matrix cannot be fit in memory and should be read from a file, assume that a few rows and all columns can be read in, how to verify?
```
