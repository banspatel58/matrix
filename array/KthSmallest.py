'''
Given an array arr[] of N distinct elements and a number K, where K is
smaller than the size of the array. Find the K’th the smallest element in
the given array.

Examples:

Input: arr[] = {7, 10, 4, 3, 20, 15}, K = 3
Output: 7

Input: arr[] = {7, 10, 4, 3, 20, 15}, K = 4
Output: 10
'''
import heapq
from typing import List

def kth_smallest_v1(arr: List[int], k: int) -> int:
    arr.sort()

    print("Kth smallest element of an array: " + str(arr) + " is " + str(arr[k - 1]))
    return arr[k - 1]

def kth_smallest_v2(arr: List[int], k: int) -> int:
    min_heap = []
    n = len(arr)

    for i in range(n):
        heapq.heappush(min_heap, -arr[i])

        if len(min_heap) > k:
            heapq.heappop(min_heap)

    print("Kth smallest element of an array: " + str(arr) + " is " + str(-min_heap[0]))
    return -min_heap[0]

if __name__ == '__main__':
    kth_smallest_v1([7, 10, 4, 3, 20, 15], 3)
    kth_smallest_v1([7, 10, 4, 3, 20, 15], 4)

    print("____________V2_________________________")

    kth_smallest_v2([7, 10, 4, 3, 20, 15], 3)
    kth_smallest_v2([7, 10, 4, 3, 20, 15], 4)
