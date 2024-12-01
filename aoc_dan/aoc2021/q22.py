"""
--- Day 22: Reactor Reboot ---
https://adventofcode.com/2021/day/22
"""
from aocd import data

FACTOR = 2

def count(steps, xmin, ymin, zmin, window):
    """Count space within range"""
    if all(step[0] == 0 for step in steps):
        return 0
    volume = 0
    filtered = ()
    for xaxis in range(xmin, xmin+window, window//FACTOR):
        xsteps = set((step[0], ((min(xaxis+window-1, step[1][0][1]), max(xaxis, step[1][0][0])), step[1][1], step[1][2])) for step in steps if xaxis <= step[1][0][1] and step[1][0][0] < xaxis+window)
        if len(xsteps) == 0:
            continue
        for yaxis in range(ymin, ymin+window, window//FACTOR):
            ysteps = set((step[0], (step[1][0], (min(yaxis+window-1, step[1][1][1]), max(yaxis, step[1][1][0])), step[1][2])) for step in xsteps if yaxis <= step[1][1][1] and step[1][1][0] < yaxis+window)
            if len(ysteps) == 0:
                continue
            for zaxis in range(zmin, zmin+window, window//FACTOR):
                zsteps = set((step[0], (step[1][0], step[1][1], (min(zaxis+window-1, step[1][2][1]), max(zaxis, step[1][2][0])))) for step in ysteps if zaxis <= step[1][2][1] and step[1][2][0] < zaxis+window)
                if len(zsteps) == 0:
                    continue
                if len(zsteps) == 1:
                    value, cube = zsteps.pop()
                    volume += value * (cube[0][1] - cube[0][0]) * (cube[1][1] - cube[1][0]) * (cube[2][1] - cube[2][0])
                elif window > 128:
                    volume += count(zsteps, xaxis, yaxis, zaxis, window//FACTOR)
                elif any(step[0] == 1 for step in zsteps):
                    volume += sum(scan(zsteps, (xaxis, yaxis, zaxis), (xaxis+window-1, yaxis+window-1, zaxis+window-1)).values())

    return volume

def scan(steps, lower, upper):
    """Scan space within range"""
    space = {}
    for step in steps:
        value, cube = step[0], step[1]
        for x in range(max(lower[0], cube[0][0]), min(upper[0], cube[0][1])+1):
            for y in range(max(lower[1], cube[1][0]), min(upper[1], cube[1][1])+1):
                for z in range(max(lower[2], cube[2][0]), min(upper[2], cube[2][1])+1):
                    space[(x, y, z)] = value
    return space

def solve():
    """Execute the reboot steps. Afterward, considering only cubes in the region x=-50..50,y=-50..50,z=-50..50, how many cubes are on?"""

    steps = []
    for line in data.splitlines():
        line = line.split()
        value = 1 if line[0] == 'on' else 0
        cube = line[1].split(',')
        for index, axis in enumerate(cube):
            cube[index] = tuple(map(int, axis[2:].split('..')))
        steps.append((value, cube))

    print("part a:", sum(scan(steps, (-50, -50, -50), (50, 50, 50)).values()))

    upper = 2 ** 15
    lower = -upper
    print("part b:", count(steps, lower, lower, lower, upper-lower))

if __name__ == "__main__":
    solve()
