"""
Given a string s, return the longest
palindromic

substring
 in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""


def longest_palindromic_substring(word: str) -> str:
    n = len(word)

    if n == 1:
        return word
    if word == word[::-1]:
        return word

    def expand_from_center(start: int, end: int):
        while start >= 0 and end < n and word[start] == word[end]:
            start -= 1
            end += 1
        return word[start + 1 : end]

    result = word[0]

    for i in range(n - 1):
        odd = expand_from_center(i, i)
        even = expand_from_center(i, i + 1)

        if len(odd) > len(result):
            result = odd
        if len(even) > len(result):
            result = even
    print("Longest palindromic substring of string: " + word + " is: " + result)
    return result


def longest_palindromic_substring_recursive(word: str) -> str:
    if word == word[::-1]:
        return word

    left = longest_palindromic_substring_recursive(word[1:])
    right = longest_palindromic_substring_recursive(word[:-1])

    if len(left) > len(right):
        print("Longest palindromic substring of string: " + word + " is: " + left)
        return left
    else:
        print("Longest palindromic substring of string: " + word + " is: " + right)
        return right

if __name__ == '__main__':
    longest_palindromic_substring("babad")
    longest_palindromic_substring("abcbadkpspqrstsrqp")


    longest_palindromic_substring_recursive("babad")
    longest_palindromic_substring_recursive("abcbadkpspqrstsrqp")