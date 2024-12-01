"""
--- Day 19: Beacon Scanner ---
https://adventofcode.com/2021/day/19
"""
from itertools import combinations
import re
from aocd import data

PATTERN = r'--- scanner \d+ ---'

def dist(first, second):
    """Manhattan distance"""
    return sum(map(abs, subtract(first, second)))

def subtract(first, second):
    """Point subtraction"""
    result = []
    for index, value in enumerate(first):
        result.append(value - second[index])
    return tuple(result)

def measure(points, origin):
    """Measure shape relative to origin"""
    return frozenset(subtract(point, origin) for point in points)

def orient(point, orientation):
    """Rotate point in 3-space"""
    a, b, c = point
    return (
        (+a,+b,+c), (+b,+c,+a), (+c,+a,+b), (+c,+b,-a), (+b,+a,-c), (+a,+c,-b), 
        (+a,-b,-c), (+b,-c,-a), (+c,-a,-b), (+c,-b,+a), (+b,-a,+c), (+a,-c,+b), 
        (-a,+b,-c), (-b,+c,-a), (-c,+a,-b), (-c,+b,+a), (-b,+a,+c), (-a,+c,+b), 
        (-a,-b,+c), (-b,-c,+a), (-c,-a,+b), (-c,-b,-a), (-b,-a,-c), (-a,-c,-b) 
    )[orientation]

def orientations(points):
    """Rotate points in 3-space"""
    return ((i, tuple(orient(x, i) for x in points)) for i in range(24))

def anneal(beacons, scan):
    """Combine scan with known beacons"""
    best = 11
    result = None
    offsets = {origin : measure(beacons, origin) for origin in beacons}
    for _, points in orientations(scan):
        for point in tuple(sorted(points))[:-best]:
            shape = measure(points, point)
            for beacon in beacons[:-best]:
                shape2 = shape & offsets[beacon]
                if len(shape2) > best:
                    best = len(shape2)
                    offset = subtract(point, beacon)
                    result = offset, measure(points, offset)
    return result

def solve():
    """Assemble the full map of beacons. How many beacons are there?

    What is the largest Manhattan distance between any two scanners?"""

    scanner = -1
    scans = []
    for line in data.splitlines():
        if match := re.match(PATTERN, line):
            scanner += 1
            scans.append([])
        elif line:
            scans[scanner].append(tuple(map(int, line.split(','))))

    offsets = [(0, 0, 0)]
    beacons = set(scans[0])
    used = [0]
    while len(used) < len(scans):
        for index, scan in enumerate(scans):
            if index not in used:
                if result := anneal(tuple(sorted(beacons)), scan):
                    offsets.append(result[0])
                    beacons |= result[1]
                    used.append(index)

    print("part a:", len(beacons))
    print("part b:", max(dist(first, second) for first, second in combinations(offsets, 2)))

if __name__ == "__main__":
    solve()
