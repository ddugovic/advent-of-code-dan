"""
--- Day 5: Print Queue ---
https://adventofcode.com/2024/day/5
"""
from aocd import data
from functools import cmp_to_key

after = {}
def compare(a, b):
    global after
    if a in after and b in after[a]:
        return -1
    elif b in after and a in after[b]:
        return 1
    else:
        return 0

a = b = 0
for line in data.splitlines():
    if '|' in line:
        v = line.split('|')
        if v[0] in after:
            after[v[0]] = after[v[0]].union({v[1]})
        else:
            after[v[0]] = {v[1]}
    elif len(line) > 0:
        w = line.split(',')
        v = line.split(',')
        v.sort(key=cmp_to_key(compare))
        if v == w:
            a += int(v[len(v)//2])
        else:
            b += int(v[len(v)//2])

print("answer_a:", a)
print("answer_b:", b)
