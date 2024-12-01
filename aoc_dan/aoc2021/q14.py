"""
--- Day 14: Extended Polymerization ---
https://adventofcode.com/2021/day/14
"""
from collections import defaultdict
from aocd import data

def react(myomer, templates):
    """React all pairwise elements"""
    polymer = defaultdict(int)
    for pair, count in myomer.items():
        element = templates[pair]
        polymer[pair[0] + element] += count
        polymer[element + pair[1]] += count
    return polymer

def score(myomer, polymer):
    """Count difference in maximum and minimum frequency"""
    counter = defaultdict(int)
    counter[myomer[0]] += 1
    counter[myomer[-1]] += 1
    for key, value in polymer.items():
        for element in key:
            counter[element] += value
    return max(counter.values())//2 - min(counter.values())//2

def solve():
    """Apply 10 steps of pair insertion to the polymer template and find the most and least common elements in the result. What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?

    Apply 40 steps of pair insertion to the polymer template and find the most and least common elements in the result. What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?"""

    myomer = None
    polymer = None
    templates = {}
    for line in data.splitlines():
        if polymer is None:
            myomer = line
            polymer = defaultdict(int)
            for index, element in enumerate(line):
                if index > 0:
                    polymer[line[index-1] + element] += 1
        elif line != "":
            pattern, element = line.split(" -> ")
            templates[pattern] = element

    for _ in range(10):
        polymer = react(polymer, templates)
    print("part a:", score(myomer, polymer))

    for _ in range(40 - 10):
        polymer = react(polymer, templates)
    print("part b:", score(myomer, polymer))

if __name__ == "__main__":
    solve()
