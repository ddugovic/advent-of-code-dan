"""
--- Day 3: Mull It Over ---
https://adventofcode.com/2024/day/3
"""
from aocd import data
from re import findall

do = True
def scan(line):
    global do
    x = y = 0
    for l in findall(r"(do|don't|mul)\((?:(\d+),(\d+))?\)", line):
        match l[0]:
            case 'do':
                do = True
            case "don't":
                do = False
            case _:
                z = int(l[1]) * int(l[2])
                x += z
                if do:
                    y += z
    return [x, y]

a = b = 0
for line in data.splitlines():
    [x, y] = scan(line)
    a += x
    b += y

print("answer_a:", a)
print("answer_b:", b)
