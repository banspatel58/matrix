"""
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Example 1:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:
Input: n = 1
Output: [[1]]
"""
from typing import List


def generate_matrix (n: int) -> List [List [int]]:
    if n == 1:
        return [[1]]

    result = [[0 for _ in range(n)] for _ in range(n)]

    top, bottom, left, right = 0, n - 1, 0, n - 1
    start = 0
    while top <= bottom and left <= right:

        for i in range(left, right + 1):
            result [top] [i] = start + 1
            start += 1
        top += 1

        for j in range(top, bottom + 1):
            result [j] [right] = start + 1
            start += 1
        right -= 1

        if top <= bottom:
            for k in range(right, left - 1, -1):
                result [bottom] [k] = start + 1
                start += 1
            bottom -= 1

        if left <= right:
            for m in range(bottom, top - 1, -1):
                result [m] [left] = start + 1
                start += 1
            left += 1
    print(result)
    return result

if __name__ == '__main__':
    generate_matrix(3)
    generate_matrix(1)
    generate_matrix(5)