"""
Given an integer n, return an array answer of length n + 1 such that
for each i (0 <= i <= n), ans[i] is the number of 1's in the binary
representation of i.
Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

"""
from typing import List


def count_bits(n: int) -> List[int]:
    result = []

    for i in range(n + 1):
        bits = bin(i)[2:]
        one_count = bits.count('1')
        result.append(one_count)

    print("Bits for " + str(n) + ": " + str(result))
    return result

if __name__ == '__main__':
    count_bits(4)
    count_bits(5)
    count_bits(2)
    count_bits(1)