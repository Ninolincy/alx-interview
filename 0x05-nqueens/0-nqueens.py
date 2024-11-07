#!/usr/bin/python3
"""
Usage: nqueens N
        If the user called the program with the wrong number
         of arguments, print Usage: nqueens N,
        followed by a new line, and exit with the status 1
        where N must be an integer greater or equal to 4
        If N is not an integer, print N must be a number,
        followed by a new line, and exit with the status 1
        If N is smaller than 4, print N must be at least 4,
        followed by a new line, and exit with the status 1
    The program should print every possible solution to the problem
        One solution per line
        You don’t have to print the solutions in a specific order
"""
import sys


def is_safe(board, row, column):
    """
    check if placing the queen in a squareis safe
    """
    # check if queens are in the same column
    for x in range(row):
        if board[x] == column:
            return False

        if abs(x - row) == abs(board[x] - column):
            return False
    return True


def n_queens(n, row, board, solutions):
    """
    Recursively solve n queens using backtracking
    Args:
            n : size of chessboard
            row: current row in consideration
            board: current state of  the board
            solution: list to store the solutions found
    """
    if row == n:
        solutions.append([[x, board[x]] for x in range(n)])
    else:
        for column in range(n):
            if is_safe(board, row, column):
                board[row] = column
                n_queens(n, row + 1, board, solutions)


def print_solution(solutions):
    """
    print the solution found
    """
    for solution in solutions:
        print(solution)


def nqueens(n):
    """
    entry point for solution
    """
    if not n.isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(n)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [-1] * n
    solution = []
    n_queens(n, 0, board, solution)
    print_solution(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    n = sys.argv[1]
    nqueens(n)
