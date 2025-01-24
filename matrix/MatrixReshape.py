"""
In MATLAB, there is a handy function called reshape which can reshape an m x n
matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number
of rows and the number of columns of the wanted to be reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix
in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new
reshaped matrix; Otherwise, output the original matrix.

Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]

Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]
"""

from typing import List


def matrix_reshape (mat: List [List [int]], r: int, c: int) -> List [List [int]]:
    rows = len(mat)
    cols = len(mat [0])

    if rows * cols != r * c:
        return mat
    elements = []
    for row in mat:
        elements.extend(row)
    print(elements)

    result = []

    for i in range(r):
        row = []
        for j in range(c):
            row.append(elements.pop(0))
        result.append(row)
    return result

if __name__ == '__main__':
    matrix_reshape([[1,2], [3,4], [5, 6]], 2, 2)