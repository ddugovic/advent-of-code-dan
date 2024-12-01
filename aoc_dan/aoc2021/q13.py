"""
--- Day 13: Transparent Origami ---
https://adventofcode.com/2021/day/13
"""
from aocd import data

def foldx(grid, crease):
    """Fold along x-axis"""
    return set(map(lambda point: (crease - abs(point[0] - crease), point[1]), grid))

def foldy(grid, crease):
    """Fold along y-axis"""
    return set(map(lambda point: (point[0], crease - abs(point[1] - crease)), grid))

def write(grid):
    """Print grid to string"""
    paper = ""
    for row in range(6):
        for col in range(40):
            if (col, row) in grid:
                paper += "#"
            else:
                paper += "."
        paper += "\n"
    return paper

def solve():
    """How many dots are visible after completing just the first fold instruction on your transparent paper?

    What code do you use to activate the infrared thermal imaging camera system?"""

    grids = [set()]
    for line in data.splitlines():
        if line.startswith("fold along"):
            axis, crease = line.split()[2].split("=")
            if axis == 'x':
                grids.append(foldx(grids[-1], int(crease)))
            else:
                grids.append(foldy(grids[-1], int(crease)))
        elif line != "":
            grids[-1].add(tuple(map(int, line.split(','))))

    print("part a:", len(grids[1]))
    print("part b:", write(grids[-1]))

if __name__ == "__main__":
    solve()
