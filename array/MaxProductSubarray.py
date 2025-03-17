'''
Given an integer array, the task is to find the maximum product of any subarray.

Examples:

Input: arr[] = {-2, 6, -3, -10, 0, 2}
Output: 180
Explanation: The subarray with maximum product is {6, -3, -10} with product = 6 * (-3) * (-10) = 180

Input: arr[] = {-1, -3, -10, 0, 60}
Output: 60
Explanation: The subarray with maximum product is {60}.
'''
from typing import List


def max_product_of_subarray(arr: List[int]) -> int:
    n = len(arr)
    max_product = -9999

    left_to_right = 1
    right_to_left = 1

    for i in range(n):
        if left_to_right == 0:
            left_to_right = 1
        if right_to_left == 0:
            right_to_left = 1

        left_to_right *= arr[i]

        j = n - 1 - i
        right_to_left *= arr[j]

        max_product = max(left_to_right, max(right_to_left, max_product))
    print("Max product of a subarray " + str(arr) + " is: " + str(max_product))
    return max_product


if __name__ == '__main__':
    max_product_of_subarray([-2, 6, -3, -10, 0, 2])
    max_product_of_subarray([-1, -3, -10, 0, 60])