"""
You are given a 0-indexed 1-dimensional (1D) integer array original, and two integers, m and n.
You are tasked with creating a 2-dimensional (2D) array with  m rows and n columns using all
the elements from original.

The elements from indices 0 to n - 1 (inclusive) of original should form the first row of the
constructed 2D array, the elements from indices n to 2 * n - 1 (inclusive) should form the
second row of the constructed 2D array, and so on.

Return an m x n 2D array constructed according to the above procedure, or an empty 2D array
if it is impossible.

Input: original = [1,2,3,4], m = 2, n = 2
Output: [[1,2],[3,4]]
Explanation: The constructed 2D array should contain 2 rows and 2 columns.
The first group of n=2 elements in original, [1,2], becomes the first row in the constructed 2D array.
The second group of n=2 elements in original, [3,4], becomes the second row in the constructed 2D array.
Example 2:

Input: original = [1,2,3], m = 1, n = 3
Output: [[1,2,3]]
Explanation: The constructed 2D array should contain 1 row and 3 columns.
Put all three elements in original into the first row of the constructed 2D array.
Example 3:

Input: original = [1,2], m = 1, n = 1
Output: []
Explanation: There are 2 elements in original.
It is impossible to fit 2 elements in a 1x1 2D array, so return an empty 2D array.


Constraints:

1 <= original.length <= 5 * 104
1 <= original[i] <= 105
1 <= m, n <= 4 * 104
"""
from typing import List


def construct_2d_array (original: List [int], m: int, n: int) -> List [List [int]]:
    array_len = len(original)

    if m * n != array_len:
        return []

    result = []
    for i in range(0, array_len, n):
        result.append(original [i: i + n])

    print(result)
    return result


if __name__ == '__main__':
    construct_2d_array([1,2,3,4], 2, 2)
    construct_2d_array([1,2,3], 1, 3)
    construct_2d_array([1,2], 1, 1)