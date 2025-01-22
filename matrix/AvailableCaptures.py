"""
You are given an 8 x 8 matrix representing a chessboard. There is exactly one white rook represented by 'R',
 some number of white bishops 'B', and some number of black pawns 'p'. Empty squares are represented by '.'.

A rook can move any number of squares horizontally or vertically (up, down, left, right) until it reaches
another piece or the edge of the board. A rook is attacking a pawn if it can move to the pawn's square in
one move.

Note: A rook cannot move through other pieces, such as bishops or pawns. This means a rook cannot attack a
pawn if there is another piece blocking the path.

Return the number of pawns the white rook is attacking.

Input: board = [[".",".",".",".",".",".",".","."],
                [".",".",".","p",".",".",".","."],
                [".",".",".","R",".",".",".","p"],
                [".",".",".",".",".",".",".","."],
                [".",".",".",".",".",".",".","."],
                [".",".",".","p",".",".",".","."],
                [".",".",".",".",".",".",".","."],
                [".",".",".",".",".",".",".","."]]

Output: 3

Explanation:

In this example, the rook is attacking all the pawns

Input: board = [[".",".",".",".",".",".","."],
                [".","p","p","p","p","p",".","."],
                [".","p","p","B","p","p",".","."],
                [".","p","B","R","B","p",".","."],
                [".","p","p","B","p","p",".","."],
                [".","p","p","p","p","p",".","."],
                [".",".",".",".",".",".",".","."],
                [".",".",".",".",".",".",".","."]]

Output: 0

Explanation:

The bishops are blocking the rook from attacking any of the pawns.

Input: board = [[".",".",".",".",".",".",".","."],
                [".",".",".","p",".",".",".","."],
                [".",".",".","p",".",".",".","."],
                ["p","p",".","R",".","p","B","."],
                [".",".",".",".",".",".",".","."],
                [".",".",".","B",".",".",".","."],
                [".",".",".","p",".",".",".","."],
                [".",".",".",".",".",".",".","."]]

Output: 3

Explanation:

The rook is attacking the pawns at positions b5, d6, and f5.
"""

from typing import List


def num_rook_captures (board: List [List [str]]) -> int:
    rows = len(board)
    cols = len(board [0])

    rook_index_i = 0
    rook_index_j = 0
    for i in range(rows):
        for j in range(cols):
            if board [i] [j] == 'R':
                rook_index_i = i
                rook_index_j = j
                break
    count = 0

    # Move down
    start_index_i = rook_index_i
    while start_index_i < rows:
        if board [start_index_i] [rook_index_j] == 'B':
            break
        elif board [start_index_i] [rook_index_j] == 'p':
            count += 1
            break
        start_index_i += 1

    # Move Up
    start_index_i = rook_index_i
    while start_index_i >= 0:
        if board [start_index_i] [rook_index_j] == 'B':
            break
        elif board [start_index_i] [rook_index_j] == 'p':
            count += 1
            break
        start_index_i -= 1

    # Move Right
    start_index_j = rook_index_j
    while start_index_j < rows:
        if board [rook_index_i] [start_index_j] == 'B':
            break
        elif board [rook_index_i] [start_index_j] == 'p':
            count += 1
            break
        start_index_j += 1

    # Move Left
    start_index_j = rook_index_j
    while start_index_j >= 0:
        if board [rook_index_i] [start_index_j] == 'B':
            break
        elif board [rook_index_i] [start_index_j] == 'p':
            count += 1
            break
        start_index_j -= 1

    return count

if __name__ == '__main__':
    matrix = [[".",".",".",".",".",".",".","."],
             [".",".",".","p",".",".",".","."],
             [".",".",".","R",".",".",".","p"],
             [".",".",".",".",".",".",".","."],
             [".",".",".",".",".",".",".","."],
             [".",".",".","p",".",".",".","."],
             [".",".",".",".",".",".",".","."],
             [".",".",".",".",".",".",".","."]]
    num_rook_captures(matrix)