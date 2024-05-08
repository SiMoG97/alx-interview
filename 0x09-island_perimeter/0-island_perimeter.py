#!/usr/bin/python3
""" 0-island_perimeter """


def island_perimeter(grid):
    """returns the perimeter of the island described in grid

    Args:
        grid (int[]): list of lists

    Returns:
        int: the perimeter of the island
    """
    perimeter = 0
    gridWidth = len(grid[0])
    gridHeight = len(grid)
    for i in range(gridHeight):
        for j in range(gridWidth):
            if grid[i][j] != 1:
                continue

            #  check top cell
            if i - 1 == -1 or i - 1 >= 0 and grid[i - 1][j] == 0:
                perimeter += 1
            # check bottom cell
            if i+1 == gridHeight or i+1 < gridHeight and grid[i+1][j] == 0:
                perimeter += 1
            # check left cell
            if j - 1 == -1 or j - 1 >= 0 and grid[i][j - 1] == 0:
                perimeter += 1
            # check right cell
            if j + 1 == gridWidth or j + 1 < gridWidth and grid[i][j + 1] == 0:
                perimeter += 1
    return perimeter
