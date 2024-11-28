#!/usr/bin/python3
"""
Make change
"""


def makeChange(coins, total):
    """
    determine the fewest number of coins
    needed to meet a given amount total.

    Args:
        coins (list): list of integers representing the coin denominations
        total (int): total amount to be met

    Returns:
        int: the fewest number of coins needed to meet the total
        -1 if total cannot be met by the coins
    """

    if total <= 0:
        return 0

    # SORT COINS
    coins.reverse(reverse=True)

    # INITIALIZE COUNT
    count = 0
    remaining_total = total

    # ITERATE THROUGH COINS
    for coin in coins:
        if coin <= remaining_total:
            # CALCULATE MAXIMUM NO. OF COINS IN TOTAL
            count_denom = remaining_total // coin
            # UPDATE REMAINING TOTAL
            remaining_total = count_denom * coin
            # UPDATE COUNT
            count += count_denom
        if remaining_total == 0:
            break

    if remaining_total != 0:
        return -1

    return count


if __name__ == '__main__':
    print(makeChange([1, 2, 25], 37))
    print(makeChange([1256, 54, 48, 16, 102], 1453))
