"""
--- Day 8: Seven Segment Search ---
https://adventofcode.com/2021/day/8
"""
from itertools import permutations
from aocd import data

DIGITS = ("abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg")

def decode(pattern, key):
    """Decodes a signal pattern"""
    translation = "".maketrans(key, "abcdefg")
    return tuple(''.join(sorted(digit.translate(translation))) for digit in pattern)

def count(segment):
    """Counts unique signal patterns"""
    return sum(len(digit) in (2, 3, 4, 7) for digit in segment)

def quantify(segment):
    """Quantifies signal display"""
    number = 0
    for digit in segment:
        number *= 10
        number += DIGITS.index(digit)
    return number

def solve():
    """In the output values, how many times do digits 1, 4, 7, or 8 appear?

For each entry, determine all of the wire/segment connections and decode the four-digit output values. What do you get if you add up all of the output values?"""

    patterns = []
    segments = []
    for line in data.splitlines():
        pattern, segment = line.split(" | ")
        patterns.append(tuple(sorted(pattern.split(), key=len)))
        segments.append(tuple(segment.split()))
        first = patterns[-1][0]
        for key in permutations("abcdefg"):
            if len(first) <= 3 and (key[2] not in first or key[5] not in first):
                continue
            pattern = decode(patterns[-1], ''.join(key))
            if all(digit in DIGITS for digit in pattern):
                segment = decode(segments[-1], ''.join(key))
                patterns[-1] = pattern
                segments[-1] = segment
                break

    print("part a:", sum(count(segment) for segment in segments))
    print("part b:", sum(quantify(segment) for segment in segments))

if __name__ == "__main__":
    solve()
