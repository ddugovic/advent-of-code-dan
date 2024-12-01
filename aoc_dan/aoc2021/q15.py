"""
--- Day 15: Chiton ---
https://adventofcode.com/2021/day/15
"""
import heapq
import math
from aocd import data

def search(risks):
    """Breadth-first search"""
    bests = [[math.inf] * len(row) for row in risks]
    bests[0][0] = 0
    queue = []
    heapq.heappush(queue, (0, 0, 0))
    while True:
        _, row, col = heapq.heappop(queue)
        best = bests[col][row]
        if col == len(risks) - 1 and row == len(risks[col]) - 1:
            return best
        for row2, col2 in ((row - 1, col), (row, col - 1), (row, col + 1), (row + 1, col)):
            if col2 not in range(len(risks)) or row2 not in range(len(risks[col2])):
                continue
            cost = best + risks[col2][row2]
            if cost < bests[col2][row2]:
                bests[col2][row2] = cost
                heapq.heappush(queue, (cost, row2, col2))


def solve():
    """What is the lowest total risk of any path from the top left to the bottom right?

    Using the full map, what is the lowest total risk of any path from the top left to the bottom right?"""

    partial = []
    for line in data.splitlines():
        partial.append(list(map(int, list(line))))
    print("part a:", search(partial))

    full = []
    for values in partial:
        extension = list(values)
        for iteration in range(4):
            extension.extend([(value + iteration) % 9 + 1 for value in values])
        full.append(extension)
    for iteration in range(4):
        for row in range(len(partial)):
            values = full[row]
            full.append([(value + iteration) % 9 + 1 for value in values])
    print("part b:", search(full))

if __name__ == "__main__":
    solve()
