#!/usr/bin/python3
"""some thing here"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total

    Args:
        coins (list int): a list of the values of the coins in your possession
        total (int): the total.

    Returns (int):
        0 If total is 0 or less ||
        -1 If total cannot be met by any number of coins you have ||
        fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0

    # min_coins_for_amount is a list where minCoinsForAmount[i]
    # is the minimum number of coins needed to make change for i
    minCoinsForAmount = [total + 1] * (total + 1)
    minCoinsForAmount[0] = 0

    # a for amount
    for a in range(1, total + 1):
        for coin in coins:
            if a - coin < 0:
                continue

            if minCoinsForAmount[a - coin] + 1 < minCoinsForAmount[a]:
                minCoinsForAmount[a] = minCoinsForAmount[a - coin] + 1

    if minCoinsForAmount[-1] > total:
        return -1

    return minCoinsForAmount[-1]
