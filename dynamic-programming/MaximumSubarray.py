"""
Given an integer array nums, find the subarray with the largest sum
and return its sum.
Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
"""
from typing import  List


def maximum_subarray(nums: List[int]) -> int:
    n = len(nums)

    if n == 1:
        return nums[0]

    dp = nums

    for i in range(1, n):
        dp[i] = max(nums[i], nums[i] + dp[i - 1])

    print("Maximum sum of subarray: " + str(nums) + " is: " + str(max(dp)))
    return max(dp)

if __name__ == '__main__':
    maximum_subarray([-2,1,-3,4,-1,2,1,-5,4])
    maximum_subarray([-2])
    maximum_subarray([5,4,-1,7,8])
    maximum_subarray([-2, -1])