"""
--- Day 1: Historian Hysteria ---
https://adventofcode.com/2024/day/1
"""
from aocd import data

a = b = 0
nums_a = []
nums_b = []
for line in data.splitlines():
    nums_a.append(int(line.split()[0]))
    nums_b.append(int(line.split()[1]))

nums_a.sort()
nums_b.sort()

for idx, x in enumerate(nums_a):
    a += abs(x - nums_b[idx])
    b += x * nums_b.count(x)

print("answer_a:", a)
print("answer_b:", b)
