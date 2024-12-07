"""
--- Day 7: Bridge Repair ---
https://adventofcode.com/2024/day/7
"""
from aocd import data

def test_a(l):
    x = int(l[0])
    s = [x]
    if len(l) > 1:
        for y in test_a(l[1:]):
            s.append(x + y)
            s.append(x * y)
    return s

def test_b(l):
    x = int(l[0])
    s = [x]
    if len(l) > 1:
        for y in test_b(l[1:]):
            s.append(x + y)
            s.append(x * y)
            s.append(int(str(y) + l[0]))
    return s

a = b = 0
for line in data.splitlines():
    l = line.split()
    goal = int(l[0][:-1])
    z = l[1:]
    z.reverse()
    if goal in test_a(z):
        a += goal
    if goal in test_b(z):
        b += goal

print("answer_a:", a)
print("answer_b:", b)
