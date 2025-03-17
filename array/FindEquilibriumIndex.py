'''
Given an array arr[] of size n, the task is to return an equilibrium index (if any)
or -1 if no equilibrium index exists. The equilibrium index of an array is an index
such that the sum of all elements at lower indexes equals the sum of all elements
at higher indexes.

Note: When the index is at the start of the array, the left sum is 0, and when it’s
at the end, the right sum is 0.

Examples:

Input: arr[] = [1, 2, 0, 3]
Output: 2
Explanation: The sum of left of index 2 is 1 + 2 = 3 and sum on right of index 2 is 3.

Input: arr[] = [1, 1, 1, 1]
Output: -1
Explanation: There is no equilibrium index in the array.

Input: arr[] = [-7, 1, 5, 2, -4, 3, 0]
Output: 3
Explanation: The sum of left of index 3 is -7 + 1 + 5 = -1 and sum on right of index 3
is -4 + 3 + 0 = -1.
'''
from typing import List

def find_equilibrium_index_v1(arr: List[int]) -> int:
    n = len(arr)

    for i in range(n):
        left = sum(arr[ : i])
        right = sum(arr[i + 1: ])

        if left == right:
            print("Found equilibrium index: " + str(i)
                  + "\nwith left array: " + str(arr[:i])
                  + " and right array: " + str(arr[i + 1 :]))
            return i

    print("Could not find equilibrium index: -1")
    return -1

def find_equilibrium_index_v2(arr: List[int]) -> int:

    prefix_sum = 0
    n = len(arr)
    total_sum = sum(arr)

    for i in range(n):
        suffix_sum = total_sum - prefix_sum - arr[i]

        if prefix_sum == suffix_sum:
            print("Found equilibrium index: " + str(i)
                  + "\nwith left array: " + str(arr[:i])
                  + " and right array: " + str(arr[i + 1 :]))
            return i
        prefix_sum += arr[i]

    print("Could not find equilibrium index: ")
    return -1

if __name__ == '__main__':
    find_equilibrium_index_v1([1, 2, 0, 3])
    find_equilibrium_index_v1([1, 1, 1, 1])
    find_equilibrium_index_v2([1, 2, 0, 3])
    find_equilibrium_index_v2([-7, 1, 5, 2, -4, 3, 0])

















