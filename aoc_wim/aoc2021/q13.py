"""
--- Day 13: Transparent Origami ---
https://adventofcode.com/2021/day/13
"""
from aocd import data
from aoc_wim.ocr import AOCR

points, folds = data.split("\n\n")
d = {}
for line in points.splitlines():
    real, imag = line.split(",")
    d[complex(int(real), int(imag))] = "#"

for i, fold in enumerate(folds.splitlines()):
    axis, n = fold.split("=")
    n = int(n)
    for z in [*d]:
        if axis[-1] == "y" and z.imag > n:
            z_ = complex(z.real, 2 * n - z.imag)
        elif axis[-1] == "x" and z.real > n:
            z_ = complex(2 * n - z.real, z.imag)
        else:
            continue
        d[z_] = "#"
        del d[z]
    if i == 0:
        a = len(d)

print("part a:", a)
print("part b:", AOCR[d])
