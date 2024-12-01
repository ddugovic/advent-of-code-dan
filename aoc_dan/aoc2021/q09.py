"""
--- Day 9: Smoke Basin ---
https://adventofcode.com/2021/day/9
"""
from aocd import data

def flood(grid):
    """Iterative flood fill of negative values"""
    for _ in range(len(grid)):
        for row, values in enumerate(grid):
            for col, value in enumerate(values):
                if value >= 0:
                    continue
                if row > 0 and grid[row-1][col] != 9:
                    grid[row-1][col] = value
                if row+1 < len(grid) and grid[row+1][col] != 9:
                    grid[row+1][col] = value
                if col > 0 and values[col-1] != 9:
                    values[col-1] = value
                if col+1 < len(values) and values[col+1] != 9:
                    values[col+1] = value

def solve():
    """Find all of the low points on your heightmap. What is the sum of the risk levels of all low points on your heightmap?

    What do you get if you multiply together the sizes of the three largest basins?"""

    grid = []
    minima = []
    for line in data.splitlines():
        values = [9]
        for character in line:
            values.append(int(character))
        values.append(9)
        grid.append(values)
    grid.insert(0, [9] * len(values))
    grid.append([9] * len(values))

    for row, values in enumerate(grid):
        for col, value in enumerate(values):
            if value < 9 and grid[row-1][col] > value and grid[row+1][col] > value and grid[row][col-1] > value and grid[row][col+1] > value:
                minima.append(value + 1)
                grid[row][col] = -1 * len(minima)
    print("part a:", sum(minima))

    flood(grid)
    sizes = [0] * len(minima)
    for values in grid:
        for value in values:
            if value < 0:
                sizes[value] += 1
    sizes = sorted(sizes)
    print("part b:", sizes[-1] * sizes[-2] * sizes[-3])

if __name__ == "__main__":
    solve()
