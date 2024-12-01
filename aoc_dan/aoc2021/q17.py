"""
--- Day 17: Trick Shot ---
https://adventofcode.com/2021/day/17
"""
import re
from aocd import data

def step(position, velocity):
    """Simulate a single step"""
    position = (position[0]+velocity[0], position[1]+velocity[1])
    velocity = (max(0, velocity[0]-1), velocity[1]-1)
    return (position, velocity)

def simulate(target, velocity):
    """Simulate an entire path"""
    path = [(step((0, 0), velocity))]
    (position, velocity) = path[-1]
    while position[0] <= target[0][1] and position[1] >= target[1][0]:
        if target[0][0] <= position[0] and position[1] <= target[1][1]:
            return path
        path.append(step(position, velocity))
        (position, velocity) = path[-1]
    return None

def solve():
    """Find the initial velocity that causes the probe to reach the highest y position and still eventually be within the target area after any step. What is the highest y position it reaches on this trajectory?

    How many distinct initial velocity values cause the probe to be within the target area after any step?"""

    pattern = r"target area: x=(-?\d+)\.\.(-?\d+), y=(-?\d+)\.\.(-?\d+)"
    for line in data.splitlines():
        target = list(map(int, re.match(pattern, line).groups()))
        target = ((target[0], target[1]), (target[2], target[3]))

    paths = []
    for yspeed in range(target[1][0], -target[1][0]+1):
        for xspeed in range(target[0][1]+1):
            path = simulate(target, (xspeed, yspeed))
            if path:
                paths.append(path)

    print("part a:", max([max([data[0][1] for data in path]) for path in paths]))
    print("part b:", len(paths))

if __name__ == "__main__":
    solve()
