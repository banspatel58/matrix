"""
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number n on the chalkboard. On each player's
turn, that player makes a move consisting of:

Choosing any x with 0 < x < n and n % x == 0.
Replacing the number n on the chalkboard with n - x.
Also, if a player cannot make a move, they lose the game.

Return true if and only if Alice wins the game, assuming both
players play optimally.
Example 1:

Input: n = 2
Output: true
Explanation: Alice chooses 1, and Bob has no more moves.
Example 2:

Input: n = 3
Output: false
Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.
"""

def divisor_game(n: int) -> bool:
    """
    Part 1) If Alice starts with an even number she will always win.
    If Alice has an even number, she can always subtract 1, giving Bob
    an odd number. Odd numbers are not divisible by 2. They are only
    divisible by odd numbers. Hence Bob must subtract an odd number.
    Since odd minus odd is even, Bob will always return an even number
    to Alice. Alice will thus get a smaller even number after each round
    of play and Bob will get a smaller odd number after each round of play.
    Eventually Bob will have to play the number 1 and will lose the game
    since he will have no options.

    Part 2) If Alice starts with an odd number she will always lose. If
    Alice has an odd number, she has no choice but to subtract an odd number
    as odd numbers have no even divisors. Thus, Bob will get an even number.
    Now using the argument from Part 1 above, Bob can take this even number
    and keep giving an odd number back to Alice by subtracting 1. Thus, Bob
    will always get to play even and Alice will always be stuck with an odd
    number smaller than her previous odd number after each round. Eventually
    Alice will have to play the number 1 and will lose the game since she
    will have no options.
    """
    print("For n = " + str(n) + " Alice won the game: " + str(n % 2 == 0))
    return n % 2 == 0

if __name__ == '__main__':
    divisor_game(999)
    divisor_game(483)
    divisor_game(924)
    divisor_game(473)
    divisor_game(986)