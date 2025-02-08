"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
"""
from typing import List


def pascals_triangle_2(row_index: int) -> List[int]:
    if row_index == 0:
        return [1]
    elif row_index == 1:
        return [1, 1]
    else:
        prev = [1, 1]
        for _ in range(row_index - 1):
            current = [1] * (len(prev) + 1)
            for j in range(1, len(current) - 1):
                current[j] = prev[j - 1] + prev[j]

            prev = current
        print(prev)
        return prev

if __name__ == '__main__':
    pascals_triangle_2(3)
    pascals_triangle_2(1)
    pascals_triangle_2(0)
    pascals_triangle_2(8)

