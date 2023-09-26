#!/usr/bin/python3
"""
Defines function to calculate the perimeter of an island
represented by a list of list of ints
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of an island represented by a list of list of ints
    """
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # For each land cell, check its adjacent cells
                # and count the number of water cells (0) in its surroundings
                perimeter += 4  # Each land cell contributes 4 to the perimeter

                # Check the cell to the left
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2  # If the left cell is also land, subtract 2

                # Check the cell above
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2

    return perimeter
