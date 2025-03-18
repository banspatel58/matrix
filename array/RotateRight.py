'''
Given an Array of size N and a value K, around which we need to right rotate
the array. How do you quickly print the right rotated array?
Examples :

Input: Array[] = {1, 3, 5, 7, 9}, K = 2.
Output: 7 9 1 3 5
Explanation:
After 1st rotation – {9, 1, 3, 5, 7}After 2nd rotation – {7, 9, 1, 3, 5}

Input: Array[] = {1, 2, 3, 4, 5}, K = 4.
Output: 2 3 4 5 1
'''
from typing import  List

def rotate_right(arr: List[int], k: int) -> List[int]:
    n = len(arr)
    k = k % n
    result = []

    for i in range(n):
        if i < k:
            result.append(arr[n + i - k])
        else:
            result.append(arr[i - k])
    print("Array: " + str(arr) + " after " + str(k) + " rotations looks like: " + str(result))
    return result

if __name__ == '__main__':
    rotate_right([1, 3, 5, 7, 9], 2)
    rotate_right([1, 2, 3, 4, 5], 4)