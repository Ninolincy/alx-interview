#!/usr/bin/python3
"""Prime Game"""


def generatePrime(n):
    """
    Generate a list of prime numbers
    """
    prime = []
    select = [True] * (n + 1)
    select[0] = select[1] = False

    for i in range(2, n + 1):
        if select[i]:
            prime.append(i)
            for j in range(i * i, n + 1, i):
                select[j] = False
    return prime


def get_winner(prime, player):
    """
    Get a winner of a game round on list of prime nos.
    """
    prime = []
    select = [True] * (n + 1)
    select[0] = select[1] = False

    for i in range(2, n + 1):
        if select[i]:
            prime.append(i)
            for j in range(i * i, n + 1, i):
                select[j] = False
    return prime


def isWinner(x, nums):
    """
    x is the number of rounds
    nums is an array of n
    Return:name of winner else None
    players: maria and ben
    """
    mariascore = 0
    benscore = 0

    for n in nums:
        prime = generatePrime(n)
        if len(prime) % 2 == 0:
            benscore += 1
        else:
            mariascore += 1

    if mariascore > benscore:
        return "Maria"
    elif benscore > mariascore:
        return "Ben"
    else:
        return None
