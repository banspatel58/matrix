"""
There is a robot on an m x n grid. The robot is initially located in the
top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right
corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right
at any point in time.

Given the two integers m and n, return the number of possible unique paths that
the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal
to 2 * 109.
Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
"""
from itertools import product


def unique_paths(m: int, n: int) -> int:
    dp = [[1] * n for p in range(m)]

    for i, j in product(range(1, m), range(1, n)):
        dp[i][j] = dp[i - 1][j] + dp[i][j -1]

    print("Unique paths for " + str(m) + " x " + str(n) + " matrix is: " + str(dp))
    return dp[m - 1][n - 1]

if __name__ == '__main__':
    unique_paths(3, 7)
    unique_paths(6, 6)
    unique_paths(1, 1)
    unique_paths(2,2)