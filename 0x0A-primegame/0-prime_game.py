#!/usr/bin/python3
"""0-prime_game.py"""


def is_prime_num(n):
    """
    a function that checks if n is a prime number

    Args:
        n (int): the number to Check

    Returns:
        bool: True if n is prime False if not
    """
    if n < 2:
        return False
    for factor in range(2, int(n ** 0.5) + 1):
        if n % factor == 0:
            return False
    return True


def isWinner(x, nums):
    """
    a function that returns a winner between Maira and ben in the Prime Game

    Args:
        x (int): number of rounds
        nums (list[int]): a list of n and n is a range of consecutive integers

    Returns:
        str | None: the name of the winner or None if there is no winner
    """
    ben_wins = 0
    maria_wins = 0

    for num in nums:
        primes_set = [n for n in range(1, num + 1) if is_prime_num(n)]
        rounds_set = list(range(1, num + 1))

        if not primes_set:
            ben_wins += 1
            continue

        is_maria_turn = True

        while True:
            if not primes_set:
                if is_maria_turn:
                    ben_wins += 1
                else:
                    maria_wins += 1
                break

            smallest_prime = primes_set.pop(0)
            rounds_set.remove(smallest_prime)

            rounds_set = [x for x in rounds_set if x % smallest_prime != 0]

            is_maria_turn = not is_maria_turn

    if maria_wins > ben_wins:
        return "Maria"

    if maria_wins < ben_wins:
        return "Ben"

    return None
