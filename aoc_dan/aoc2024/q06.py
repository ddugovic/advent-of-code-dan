"""
--- Day 6: Guard Gallivant ---
https://adventofcode.com/2024/day/6
"""
from aocd import data

def solve(start):
    u = 0
    v = start[0]
    w = start[1]
    path = set()
    cycle = set()
    while 0 <= v < rows and 0 <= w < cols and (u, v, w) not in cycle:
        path.add((v, w))
        cycle.add((u, v, w))
        match u:
            case 0:
                if v == 0 or (v-1, w) not in walls:
                    v -= 1
                else:
                    u = 1
            case 1:
                if w+1 == cols or (v, w+1) not in walls:
                    w += 1
                else:
                    u = 2
            case 2:
                if v+1 == rows or (v+1, w) not in walls:
                    v += 1
                else:
                    u = 3
            case 3:
                if w == 0 or (v, w-1) not in walls:
                    w -= 1
                else:
                    u = 0
    return path, v, w

a = b = 0
grid = []
for line in data.splitlines():
    grid.append(line)

walls = set()
rows = len(grid)
cols = len(grid[0])
start = None
for r, line in enumerate(grid):
    for c, ch in enumerate(line):
        if ch == '^':
            start = (r, c)
        if ch == '#':
            walls.add((r,c))

path, _, _ = solve(start)
a = len(path)

blocks = set()
for p in path:
    if p != start:
        walls.add(p)
        _, v, w = solve(start)
        walls.remove(p)
        if 0 <= v < rows and 0 <= w < cols:
            blocks.add(p)
            b += 1

print("answer_a:", a)
print("answer_b:", b)
