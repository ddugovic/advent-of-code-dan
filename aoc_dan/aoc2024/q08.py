"""
--- Day 8: Resonant Collinearity ---
https://adventofcode.com/2024/day/8
"""
from aocd import data
from math import gcd 

def dist(r1, r2, c1, c2):
    if r1 > r2 or (r1 == r2 and c1 > c2):
        return (r1-r2, c1-c2)
    else:
        return (r2-r1, c2-c1)

def test(nodes, x, y):
    # brute force (walk the entire space)
    # ray casting would be more efficient but more code
    for r in range(rows):
        for c in range(cols):
            if (r,c) not in nodes:
                d = []
                for z in nodes:
                    d.append(dist(r,z[0],c,z[1]))
                d.sort()
                for w in d[:-1]:
                    if (w[0]*2, w[1]*2) in d:
                        x.add((r,c))
                        break
            if (r,c) not in y:
                while len(d) > 1:
                    w = d.pop()
                    v = gcd(w[0], w[1])
                    if v > 1:
                        u = (w[0]//v, w[1]//v)
                        for t in range(1, v):
                            if (u[0]*t, u[1]*t) in d:
                                y.add((r,c))
                                break
    return x, y

a = b = 0
lines = data.splitlines()
rows = len(lines)
cols = len(lines[0])

x = set()
y = set()
chart = {}
for r, line in enumerate(lines):
    for c, ch in enumerate(line):
        if ch != '.':
            y.add((r,c))
            if ch in chart:
                chart[ch].append((r,c))
            else:
                chart[ch] = [(r,c)]
for nodes in chart.values():
    x, y = test(nodes, x, y)
a = len(x)
b = len(y)

print("answer_a:", a)
print("answer_b:", b)
