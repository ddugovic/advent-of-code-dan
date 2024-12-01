"""
--- Day 5: Hydrothermal Venture ---
https://adventofcode.com/2021/day/5
"""
from collections import defaultdict
import re
from aocd import data

PATTERN = r'(\d+),(\d)'

def count(vents):
    """Count intersections between segments"""
    return sum(value > 1 for value in vents.values())

def solve():
    """Consider only horizontal and vertical lines. At how many points do at least two lines overlap?

    Consider all of the lines. At how many points do at least two lines overlap?"""

    vents = defaultdict(int)
    segments = []
    for line in data.splitlines():
        points = []
        for match in re.findall(PATTERN, line):
            points.append(tuple(map(int, match)))
        segments.append(tuple(sorted(points)))

    diagonals = []
    for segment in segments:
        if segment[0][0] == segment[1][0]:
            row = segment[0][0]
            for col in range(segment[0][1], segment[1][1] + 1):
                vents[(row, col)] += 1
        elif segment[0][1] == segment[1][1]:
            col = segment[0][1]
            for row in range(segment[0][0], segment[1][0] + 1):
                vents[(row, col)] += 1
        else:
            diagonals.append(segment)
    print("part a:", count(vents))

    for segment in diagonals:
        col = segment[0][1]
        for row in range(segment[0][0], segment[1][0] + 1):
            vents[(row, col)] += 1
            if segment[0][1] < segment[1][1]:
                col += 1
            else:
                col -= 1
    print("part b:", count(vents))

if __name__ == "__main__":
    solve()
