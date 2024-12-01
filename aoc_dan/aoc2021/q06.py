"""
--- Day 6: Lanternfish ---
https://adventofcode.com/2021/day/6
"""
import itertools
from aocd import data

def step(timers):
    """Simulate a single day for all lanternfish"""
    fish = timers.pop(0)
    timers[6] += fish
    timers.append(fish)

def solve():
    """Find a way to simulate lanternfish. How many lanternfish would there be after 80 timer?

    How many lanternfish would there be after 256 days?"""

    timers = [0] * 9
    for timer in data.splitlines()[0].split(','):
        timers[int(timer)] += 1

    for _ in itertools.repeat(None, 80):
        step(timers)
    print("part a:", sum(timers))

    for _ in itertools.repeat(None, 256 - 80):
        step(timers)
    print("part b:", sum(timers))

if __name__ == "__main__":
    solve()
