"""
--- Day 4: Ceres Search ---
https://adventofcode.com/2024/day/4
"""
from aocd import data

a = b = 0
grid = []
for line in data.splitlines():
    grid.append(line)

def test(grid, r, c, rows, cols, w, e):
    q = 'XMAS'
    r2 = r
    c2 = c
    for z in range(0, 4):
        if not (0 <= r2 < rows) or not (0 <= c2 < cols) or grid[r2][c2] != q[z]:
            return 0
        r2 += w
        c2 += e
    return 1

def test2(grid, r, c, rows, cols):
    p = 0
    r2 = r-1
    r3 = r+1
    c2 = c-1
    c3 = c+1
    if r2 >= 0 and c2 >= 0 and r3 < rows and c3 < cols:
        p1 = 0
        p2 = 0
        match grid[r2][c2] + grid[r3][c3]:
            case 'MS' | 'SM':
                p1 = 1
        match grid[r2][c3] + grid[r3][c2]:
            case 'MS' | 'SM':
                p2 = 1
        if p1 and p2:
            p += 1
    return p

rows = len(grid)
cols = len(grid[0])
for r, line in enumerate(grid):
    for c, ch in enumerate(line):
        if ch == 'A':
            b += test2(grid, r, c, rows, cols)
        if ch == 'X':
            a += test(grid, r, c, rows, cols, -1, -1)
            a += test(grid, r, c, rows, cols, -1, 0)
            a += test(grid, r, c, rows, cols, -1, 1)
            a += test(grid, r, c, rows, cols, 0, -1)
            a += test(grid, r, c, rows, cols, 0, 1)
            a += test(grid, r, c, rows, cols, 1, -1)
            a += test(grid, r, c, rows, cols, 1, 0)
            a += test(grid, r, c, rows, cols, 1, 1)

print("answer_a:", a)
print("answer_b:", b)
