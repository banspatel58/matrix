"""
This code helps in traversing matrix in spiral order
"""
from typing import List


def spiral_order_traversal(matrix: List[List[int]]) -> List[int]:
    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    visited = set()
    top, bottom, left, right = 0, rows - 1, 0, cols - 1

    while top <= bottom and rows <= cols:
        for i in range(left, right + 1):
            result.append(matrix[top][i])
            visited.add((top, i))

        top += 1

        for j in range(top, bottom + 1):
            result.append(matrix [j] [right])
            visited.add((j, right))

        right -= 1

        if top <= bottom:
            for k in range(right, left - 1, -1):
                result.append(matrix [bottom] [k])
                visited.add((bottom, k))
            bottom -= 1

        if left <= right:
            for m in range(bottom, top - 1, - 1):
                result.append(matrix [m] [left])
                visited.add((m, left))
            left += 1
    print(result)


    return result


if __name__ == '__main__':
    matrix_a = [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]
    spiral_order_traversal(matrix_a)

    matrix_b = [[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]]
    spiral_order_traversal(matrix_b)