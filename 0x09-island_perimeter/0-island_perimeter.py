#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    """
    grid is a list of list of integers:
        0 represents water
        1 represents land
        Each cell is square, with a side length of 1
        Cells are connected horizontally/vertically (not diagonally).
        grid is rectangular, with its width and height not exceeding 100
    Returns the perimeter of the island described in grid
    """
    perimeter = 0
    row = len(grid)
    column = len(grid[0])

    for i in range(row):
        for j in range(column):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter
                 