#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Args:
        grid (list): A list of list of integers representing the island.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows else 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # Start with 4 sides for each land cell
                sides = 4

                # Check the cell above
                if row > 0 and grid[row - 1][col] == 1:
                    sides -= 1
                # Check the cell below
                if row < rows - 1 and grid[row + 1][col] == 1:
                    sides -= 1
                # Check the cell to the left
                if col > 0 and grid[row][col - 1] == 1:
                    sides -= 1
                # Check the cell to the right
                if col < cols - 1 and grid[row][col + 1] == 1:
                    sides -= 1

                perimeter += sides

    return perimeter
