#!/usr/bin/python3
"""Island perimeter computing module.
"""

def island_perimeter(grid):
    """Computes the perimeter of an island with no lakes.
    """
    perimeter = 0
    if not isinstance(grid, list):
        return 0

    n = len(grid)
    m = len(grid[0]) if grid else 0

    for x in range(n):
        for y in range(m):
            if grid[x][y] == 1:
                # Add 4 for each land cell
                perimeter += 4

                # Subtract 2 for each adjacent land cell
                if x > 0 and grid[x - 1][y] == 1:
                    perimeter -= 2
                if y > 0 and grid[x][y - 1] == 1:
                    perimeter -= 2

    return perimeter
