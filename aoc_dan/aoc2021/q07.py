"""
--- Day 7: The Treachery of Whales ---
https://adventofcode.com/2021/day/7
"""
from aocd import data

def cost(crab, position):
    """Calculate triangular number"""
    displacement = abs(crab - position)
    return displacement * (displacement + 1) // 2

def solve():
    """Determine the horizontal position that the crabs can align to using the least fuel possible. How much fuel must they spend to align to that position?

Determine the horizontal position that the crabs can align to using the least fuel possible so they can make you an escape route! How much fuel must they spend to align to that position?"""

    crabs = []
    for crab in data.splitlines()[0].split(','):
        crabs.append(int(crab))

    fuel = sum(crabs)
    for position in range(max(crabs)):
        fuel = min(fuel, sum([abs(crab - position) for crab in crabs]))
    print("part a:", fuel)

    fuel = sum(crabs) * sum(crabs)
    for position in range(max(crabs)):
        fuel = min(fuel, sum([cost(crab, position) for crab in crabs]))
    print("part b:", fuel)

if __name__ == "__main__":
    solve()
