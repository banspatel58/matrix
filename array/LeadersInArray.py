'''
Given an array arr[] of size n, the task is to find all the Leaders in the array.
An element is a Leader if it is greater than or equal to all the elements to its
right side.

Note: The rightmost element is always a leader.

Examples:

Input: arr[] = [16, 17, 4, 3, 5, 2]
Output: [17 5 2]
Explanation: 17 is greater than all the elements to its right i.e., [4, 3, 5, 2],
therefore 17 is a leader. 5 is greater than all the elements to its right i.e.,
[2], therefore 5 is a leader. 2 has no element to its right, therefore 2 is a leader.

Input: arr[] = [1, 2, 3, 4, 5, 2]
Output: [5 2]
Explanation: 5 is greater than all the elements to its right i.e., [2], therefore
5 is a leader. 2 has no element to its right, therefore 2 is a leader.
'''
from typing import List


def find_leaders_in_array(arr: List[int]) -> List[int]:
    n = len(arr)
    result = [arr [n - 1]]
    for i in range(n - 2, -1, -1):
        if arr[i] > max(arr[i + 1 : ]):
            result.append(arr[i])
    print("Leaders of the array: " + str(arr) + " are: " + str(result[::-1]))
    return result[::-1]

if __name__ == '__main__':
    find_leaders_in_array([16, 17, 4, 3, 5, 2])
    find_leaders_in_array([1, 2, 3, 4, 5, 2])