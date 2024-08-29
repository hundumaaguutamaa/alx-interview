#!/usr/bin/python3
"""
Function to calculate the perimeter of an island in a grid.
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.

    Args:
        grid (list of list of int): A 2D grid where 0 represents water and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    num_rows = len(grid)
    num_cols = len(grid[0]) if num_rows > 0 else 0

    for row in range(num_rows):
        for col in range(num_cols):
            if grid[row][col] == 1:  # Land found
                # Check all four directions
                # Up
                if row == 0 or grid[row - 1][col] == 0:
                    perimeter += 1
                # Down
                if row == num_rows - 1 or grid[row + 1][col] == 0:
                    perimeter += 1
                # Left
                if col == 0 or grid[row][col - 1] == 0:
                    perimeter += 1
                # Right
                if col == num_cols - 1 or grid[row][col + 1] == 0:
                    perimeter += 1

    return perimeter

