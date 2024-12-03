"""
--- Day 2: Red-Nosed Reports ---
https://adventofcode.com/2024/day/2
"""
from aocd import data

def test(l):
    l2 = list(l)
    l2.sort()
    for d in [x - l2[i-1] if i else None for i, x in enumerate(l2)][1:]:
        if d < 1 or d > 3:
            return 0
    l3 = list(l2)
    l3.reverse()
    if l == l2 or l == l3:
        return 1
    return 0

def test2(l):
    for i, value in enumerate(l):
        l2 = list(l)
        l2.pop(i)
        if test(l2):
            return 1
    return 0

a = b = 0
for line in data.splitlines():
    nums_a = []
    for d in line.split():
        nums_a.append(int(d))
    a += test(nums_a)
    b += test2(nums_a)

print("answer_a:", a)
print("answer_b:", b)
