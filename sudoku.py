'''
Write the function sudokuSolve that checks whether a given sudoku board
(i.e. sudoku puzzle) is solvable. If so, the function will returns true.
Otherwise (i.e. there is no valid solution to the given sudoku board), returns false.

'''


def solve(board):
        return solve_(board, 0, 0, len(board))

def solve_(board, i, j, size):
        print i, j, board
        if i >= size or j >= size:
            return check(board, len(board))
        if board[i][j] > 0:
            if i == size-1 and j == size-1:
                return check(board, len(board))
            x, y = next(i, j, size)
            if x > i:
                if not check_row(board, i, size):
                    return False
            return solve_(board, x, y, size)
        else:
            for value in range(1, size + 1):
                board[i][j] = value * -1
                x, y = next(i, j, size)
                if y>j and i==size-1:
                    if not check_col(board, j, size):
                        continue
                if solve_(board, x, y, size):
                    return True
        return False
        #return check(board, len(board))


def next(i, j, size):
        if j < size - 1:
            return i, j + 1
        else:
            return i + 1, 0

def check_row(board, row, size):
        print 'check_row', row
        hash = {}
        for col in range(0, size):
            value = abs(board[row][col])
            if value not in range(1, size + 1):
                print board, row, col
                raise Exception
                return False
            elif value in hash:
                return False
            hash[value] = value
        return True


def check_col(board, col, size):
    print 'check_col', col
    hash = {}
    for row in range(0, size):
        value = abs(board[row][col])
        if value not in range(1, size + 1):
            print board, row, col
            raise Exception
            return False
        elif value in hash:
            return False
        hash[value] = value
    return True


def check(board, size):
    print 'check'
    for row in range(0, size):
        if not check_row(board, row, size):
            return False
    for col in range(0, size):
        if not check_col(board, col, size):
            return False
    return True

board = [
    [1, 2, 3, 4],
    [2, 3, 4, 1],
    [0, 0, 0, 0],
    [0, 0, 3, 0]
]
board1 = [
    [0, 0],
    [0, 0]
]
board1 = [
    [1, 2, 3],
    [2, 3, 1],
    [3, 1, 2]
]
#print check(board, len(board))
print solve(board)

