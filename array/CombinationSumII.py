"""
Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]
"""

from typing import List


def combination_sum2 (candidates: List [int], target: int) -> List [List [int]]:
    candidates.sort()
    result = []
    print("Input: " + str(candidates) + " target: " + str(target))
    def dfs (target, start, comb):
        if target < 0:
            return
        if target == 0:
            result.append(comb)
            return

        for i in range(start, len(candidates)):
            if i > start and candidates [i] == candidates [i - 1]:
                continue
            if candidates [i] > target:
                break

            dfs(target - candidates [i], i + 1, comb + [candidates [i]])

    dfs(target, 0, [])
    print("Possible Combinations: " + str(result) + " for target: " + str(target))
    return result

if __name__ == '__main__':
    combination_sum2([10,1,2,7,6,1,5], 8)
    combination_sum2([2,5,2,1,2], 5)