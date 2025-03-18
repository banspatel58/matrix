'''
Given two arrays, arr[] and dep[], that represent the arrival and departure times of
trains respectively, the task is to find the minimum number of platforms required so
that no train waits.

Examples:

Input: arr[] = [900, 940, 950, 1100, 1500, 1800],
dep[] = [910, 1200, 1120, 1130, 1900, 2000]
Output: 3
Explanation: There are at-most three trains at a time (time between 940 and 1200)

Input: arr[] = [1,  5], dep[] = [3, 7]
Output: 1
Explanation: Only one platform is needed.
'''
from typing import List

def max_platform_needed(arr: List[int], dep: List[int]) -> int:
    n = len(arr)

    arr.sort()
    dep.sort()

    ans = 0
    j = 0
    count = 0

    for i in range(n):
        while j < n and dep[j] < arr[i]:
            count -= 1
            j += 1

        count += 1

        ans = max(count, ans)
    print("Max platforms needed are: " + str(ans))
    return ans


if __name__ == '__main__':
    arrival = [900, 940, 950, 1100, 1500, 1800]
    departure = [910, 1200, 1120, 1130, 1900, 2000]
    max_platform_needed(arrival, departure)
    arrival = [1,  5]
    departure = [3,  7]
    max_platform_needed(arrival, departure)