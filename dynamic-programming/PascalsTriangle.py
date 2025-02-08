"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly
above it as shown:
Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
"""
from typing import List


def pascals_triangle(num_rows: int) -> List[List[int]]:
    result = []

    if num_rows == 1:
        return [[1]]

    dp = [[0]] * num_rows
    dp[0] = [1]
    dp[1] = [1, 1]

    for i in range(2, num_rows):
        sub_array = [1] * (i + 1)
        prev_sub_array = dp[i - 1]
        for j in range(1, len(sub_array) - 1):
            sub_array[j] = prev_sub_array[j - 1] + prev_sub_array[j]
        dp[i] = sub_array

    print(dp)
    return dp


if __name__ == '__main__':

    pascals_triangle(5)
    pascals_triangle(8)