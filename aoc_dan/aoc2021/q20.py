"""
--- Day 20: Trench Map ---
https://adventofcode.com/2021/day/20
"""
from aocd import data

def pad(grid, space):
    """Pad grid image"""
    if any(value != space for value in grid[0]):
        grid.insert(0, [space] * len(grid[0]))
    if any(value != space for value in grid[-1]):
        grid.append([space] * len(grid[-1]))
    if any(values[0] != space or values[-1] != space for values in grid):
        grid = [[space] + values + [space] for values in grid]
    return grid

def scan(grid, row, col, space):
    """Scan grid image"""
    window = ""
    for row2 in range(row-1, row+2):
        for col2 in range(col-1, col+2):
            window += str(grid[row2][col2] if 0 <= row2 < len(grid) and 0 <= col2 < len(grid[row2]) else space)
    return window

def enhance(code, grid, iteration):
    """Enhance grid image"""
    if code[0] == 1:
        space = iteration % 2
        grid = pad(grid, space)
        result = [[1-space] * len(values) for values in grid]
    else:
        space = 0
        grid = pad(grid, space)
        result = [[space] * len(values) for values in grid]

    for row, values in enumerate(grid):
        for col, _ in enumerate(values):
            index = int(scan(grid, row, col, space), 2)
            result[row][col] = code[index]
    return result

def solve():
    """Start with the original input image and apply the image enhancement algorithm twice, being careful to account for the infinite size of the images. How many pixels are lit in the resulting image?

    Start again with the original input image and apply the image enhancement algorithm 50 times. How many pixels are lit in the resulting image?"""

    code = None
    grid = []
    for line in data.splitlines():
        if line != "":
            values = [int(character == '#') for character in line]
            if code is None:
                code = values
            else:
                grid.append(values)

    for iteration in range(2):
        grid = enhance(code, grid, iteration)
    print("part a:", sum(sum(values) for values in grid))

    for iteration in range(50 - 2):
        grid = enhance(code, grid, iteration)
    print("part b:", sum(sum(values) for values in grid))

if __name__ == "__main__":
    solve()
