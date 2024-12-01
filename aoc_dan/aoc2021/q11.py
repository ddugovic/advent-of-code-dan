"""
--- Day 11: Dumbo Octopus ---
https://adventofcode.com/2021/day/11
"""
from aocd import data

def step(grid):
    """Simulate a single iteration"""
    count = 0
    for row, values in enumerate(grid):
        for col, value in enumerate(values):
            grid[row][col] = value + 1
    for _ in range(len(grid) * len(grid[0])):
        lastcount = count
        for row, values in enumerate(grid):
            for col, value in enumerate(values):
                if value > 9:
                    for row2 in range(row-1, row+2):
                        for col2 in range(col-1, col+2):
                            if 0 <= row2 < len(grid) and 0 <= col2 < len(values) and 0 < grid[row2][col2] <= 9:
                                grid[row2][col2] += 1
                    count += 1
                    grid[row][col] = 0
        if count == lastcount:
            break
    return count

def solve():
    """Given the starting energy levels of the dumbo octopuses in your cavern, simulate 100 steps. How many total flashes are there after 100 steps?

    If you can calculate the exact moments when the octopuses will all flash simultaneously, you should be able to navigate through the cavern. What is the first step during which all octopuses flash?"""

    count = []
    grid = []
    for line in data.splitlines():
        grid.append(list(map(int, list(line))))

    for _ in range(100):
        count.append(step(grid))
    print("part a:", sum(count))

    for _ in range(1000):
        count.append(step(grid))
        if count[-1] == len(grid) * len(grid[0]):
            break
    print("part b:", len(count))

if __name__ == "__main__":
    solve()
