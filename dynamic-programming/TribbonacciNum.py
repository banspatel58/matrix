"""
The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537

"""


def fibonacci_number(n: int) -> int:
    if n == 0:
        return 0

    if n == 1 or n == 2:
        return 1

    dp = [0] * n
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1

    for i in range(3, n):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[n - 3]
    print(dp)

    print("Tribonnaci of number: " + str(n) + " is: " + str(dp[n- 1] + dp[n -2] + dp[n - 3]))
    return dp[n- 1] + dp[n -2] + dp[n - 3]

if __name__ == '__main__':
    fibonacci_number(5)
    fibonacci_number(6)
    fibonacci_number(10)