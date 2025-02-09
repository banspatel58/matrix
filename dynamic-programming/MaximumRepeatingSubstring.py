"""
For a string sequence, a string word is k-repeating if word concatenated
k times is a substring of sequence. The word's maximum k-repeating value
is the highest value k where word is k-repeating in sequence. If word is
not a substring of sequence, word's maximum k-repeating value is 0.
Given strings sequence and word, return the maximum k-repeating value of
word in sequence.
Example 1:

Input: sequence = "ababc", word = "ab"
Output: 2
Explanation: "abab" is a substring in "ababc".
Example 2:

Input: sequence = "ababc", word = "ba"
Output: 1
Explanation: "ba" is a substring in "ababc". "baba" is not a substring in "ababc".
Example 3:

Input: sequence = "ababc", word = "ac"
Output: 0
Explanation: "ac" is not a substring in "ababc".
"""

def maximum_repeating_substring(sequence: str, word: str) -> int:
    if not word or word not in sequence:
        return 0

    k = 0
    max_count = 0
    temp = word

    while temp in sequence:
        k += 1
        temp += word
        max_count = max(max_count, k)

    print("Maximum # of times word: " + word + " appears in sequence: " + sequence + " is: " + str(max_count))
    return max_count

if __name__ == '__main__':
    maximum_repeating_substring("ababc", "ab")
    maximum_repeating_substring("ababc", "ba")
    maximum_repeating_substring("ababc", "ac")