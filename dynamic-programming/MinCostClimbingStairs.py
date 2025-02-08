"""
You are given an integer array cost where cost[i] is the cost of ith
step on a staircase. Once you pay the cost, you can either climb one
or two steps.

You can either start from the step with index 0, or the step with
index 1.

Return the minimum cost to reach the top of the floor.
Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.

"""
from typing import List


def min_cost_climbing_stairs(cost: List[int]) -> int:

    n = len(cost)
    if n == 1:
        return cost[0]

    if n == 2:
        return min(cost[0], cost[1])

    dp = [0] * n
    dp[0] = cost[0]
    dp[1] = cost[1]

    for i in range(2, n):
        dp[i] = cost[i] + min((dp[i - 1], dp[i - 2]))

    print(dp)

    print("Minimum cost of climbing " + str(n) + " stairs: " + str(min(dp[n - 1], dp[n - 2])))
    return min(dp[n - 1], dp[n - 2])

if __name__ == '__main__':
    min_cost_climbing_stairs([10,15,20])
    min_cost_climbing_stairs([1,100,1,1,1,100,1,1,100,1])
    min_cost_climbing_stairs([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])