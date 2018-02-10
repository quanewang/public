'''
LESSON
- row_end = row_end+1 => row_end = row_end-1
- missing
        if row_begin>row_end:
            break
'''

# Given a 2D array (matrix) inputMatrix of integers,
# create a function spiralCopy that copies inputMatrix
# values into a 1D array in a spiral order, clockwise.
# Your function then should return that array. Analyze
# the time and space complexities of your solution.
#
# Example:
#
# input:  inputMatrix  = [ [1,    2,   3,  4,    5],
#                          [6,    7,   8,  9,   10],
#                          [11,  12,  13,  14,  15],
#                          [16,  17,  18,  19,  20] ]
#
# output: [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]


def spiral(arr):
    result = []
    row_count = len(arr)
    col_count = len(arr[0])

    row_begin = 0
    row_end = row_count-1

    col_begin = 0
    col_end = col_count-1

    while row_begin<=row_end and col_begin<=col_end:
        for i in range(col_begin, col_end+1, 1):
            result.append(arr[row_begin][i])
        row_begin = row_begin+1
        if row_begin>row_end:
            break
        for i in range(row_begin, row_end+1, 1):
            result.append(arr[i][col_end])
        col_end = col_end-1
        if col_begin>col_end:
            break
        for i in range(col_end, col_begin-1, -1):
            result.append(arr[row_end][i])
        row_end = row_end-1
        if row_begin>row_end:
            break
        for i in range(row_end, row_begin-1, -1):
            result.append(arr[i][col_begin])
        col_begin = col_begin+1
    return result

inputMatrix  = [ [1,  2,  3,  4,  5],
                 [6,  7,  8,  9,  10],
                 [11, 12, 13, 14, 15],
                 [16, 17, 18, 19, 20]]

inputMatrix1 = [[1, 2, 3, 4, 5]]

inputMatrix2  = [ [1,  2,  3,  4,  5],
                 [6,  7,  8,  9,  10]]

print spiral(inputMatrix)

print spiral(inputMatrix1)

print spiral(inputMatrix2)