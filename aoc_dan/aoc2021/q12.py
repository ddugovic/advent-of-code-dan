"""
--- Day 12: Passage Pathing ---
https://adventofcode.com/2021/day/12
"""
from collections import defaultdict
from aocd import data

def explore(graph, path, slack=0):
    """Depth-first explore"""
    score = 0
    for cave in graph[path[-1]]:
        if cave == 'end':
            score += 1
        elif slack > 0 or cave.isupper() or cave not in path:
            path.append(cave)
            if slack > 0 and cave.islower() and cave in path[:-1]:
                score += explore(graph, path, slack-1)
            else:
                score += explore(graph, path, slack)
            path.pop(-1)
    return score

def solve():
    """How many paths through this cave system are there that visit small caves at most once?

    Given these new rules, how many paths through this cave system are there?"""

    graph = defaultdict(set)
    for line in data.splitlines():
        start, end = line.split("-")
        graph.setdefault(start, []).append(end)
        if start != 'start' and end != 'end':
            graph.setdefault(end, []).append(start)

    print("part a:", explore(graph, ['start']))
    print("part b:", explore(graph, ['start'], 1))

if __name__ == "__main__":
    solve()
