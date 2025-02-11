"""
You are given an m x n integer matrix mat and an integer target.

Choose one integer from each row in the matrix such that the absolute
difference between target and the sum of the chosen elements is minimized.

Return the minimum absolute difference.

The absolute difference between two numbers a and b is the absolute value of a - b.

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], target = 13
Output: 0
Explanation: One possible choice is to:
- Choose 1 from the first row.
- Choose 5 from the second row.
- Choose 7 from the third row.
The sum of the chosen elements is 13, which equals the target, so the absolute difference is 0.
Example 2: Input: mat = [[1],[2],[3]], target = 100
Output: 94
Explanation: The best possible choice is to:
- Choose 1 from the first row.
- Choose 2 from the second row.
- Choose 3 from the third row.
The sum of the chosen elements is 6, and the absolute difference is 94.
Example 3:Input: mat = [[1,2,9,8,7]], target = 6
Output: 1
Explanation: The best choice is to choose 7 from the first row.
The absolute difference is 1.
"""


from typing import List


def minimize_the_difference (mat: List [List [int]], target: int) -> int:
    sum_set = {0}

    for row in mat:
        sum_set = {elem + num for elem in sum_set for num in row}

    min_difference = min(abs(target - sum_val) for sum_val in sum_set)

    print("Minimum difference for the target is: " + str(target) + " is: " + str(min_difference))
    return min_difference

if __name__ == '__main__':
    minimize_the_difference([[1,2,3],[4,5,6],[7,8,9]], 13)
    minimize_the_difference([[1],[2],[3]], 100)
    minimize_the_difference([[1,2,9,8,7]], 6)