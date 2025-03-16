'''
Given an array arr[] of size n-1 with distinct integers in the range of [1, n].
This array represents a permutation of the integers from 1 to n with one
element missing. Find the missing element in the array.

Examples:

Input: arr[] = [1, 2, 4, 6, 3, 7, 8]
Output: 5
Explanation: Here the size of the array is 7, so the range will be [1, 8].
The missing number between 1 and 8 is 5

Input: arr[] = [1, 2, 3, 5]
Output: 4
Explanation: Here the size of the array is 4, so the range will be [1, 5].
The missing number between 1 and 5 is 4
'''
from typing import List


def find_missing_number(arr: List[int]) -> int:
    n = len(arr) + 1

    actual_sum = sum(arr)

    expected_sum = (n * (n + 1)) // 2

    print("expected sum: " + str(expected_sum))
    print("actual sum: " + str(actual_sum))
    return expected_sum - actual_sum

if __name__ == '__main__':
    find_missing_number([1, 2, 4, 6, 3, 7, 8])
    find_missing_number([1, 2, 3, 5])