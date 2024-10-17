#!/usr/bin/python3

"""
    method that calculates the fewest number
    of operation to result in exactly n H characters
    no. of arguments: n
    if n is impossible, return 0
"""


def minOperations(n):
    if n <= 0:
        return (0)
    """initialize a divisor of 2"""
    divisor = 2
    num_operations = 0
    while n > 1:
        if n % divisor == 0:
            n /= divisor
            num_operations += divisor
        else:
            divisor += 1
    return num_operations


"""
def minOperations(n):
    num_operations = 0
    for i in range(1, n):
        num_operations += 1
    return num_operations

if __name__ == "__main__":
        n = int(sys.argv[1])
        print(minOperations(n))
"""
