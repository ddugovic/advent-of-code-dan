"""
--- Day 18: Snailfish ---
https://adventofcode.com/2021/day/18
"""
import functools
from itertools import permutations
import re
from aocd import data

PATTERN = r'\[(\d+),(\d+)\]'

def add(first, second):
    """Add numbers"""
    number = '['+first+','+second+']'
    return deparse(normalize(parse(number)))

def magnitude(number):
    """Measure number"""
    while match := re.search(PATTERN, number):
        value = 3 * int(match.group(1)) + 2 * int(match.group(2))
        number = number.replace(match.group(0), str(value))
    return int(number)

def deparse(tree):
    """Deparse tree"""
    result, prev_depth = "", 0
    for node in tree:
        depth, value = node
        if depth > prev_depth:
            result += "[" * (depth - prev_depth) + str(value) + ","
        else:
            result += str(value) + "]" * (prev_depth - depth) + ","
        prev_depth = depth
    return result.replace(",None,",",").replace(",None","")[:-1]

def parse(snail, depth=0):
    """Parse number"""
    tree = []
    for character in snail:
        if character == '[':
            depth += 1
        elif character == ']':
            depth -= 1
        elif character == ',':
            tree.append((depth, None))
        else:
            tree.append([depth, int(character)])
    tree.append((0, None))
    return tree

def normalize(tree):
    """Reduce tree"""
    for index, snail in enumerate(tree):
        depth, value = snail
        if depth > 4 and value is None:
            left, right = tree[:index-1], tree[index+2:]
            lvalue, rvalue = tree[index-1][1], tree[index+1][1]
            if index > 1:
                left[-2][1] += lvalue
            if index+3 < len(tree):
                right[1][1] += rvalue
            return normalize(left + [[depth-1, 0]] + right)

    for index, snail in enumerate(tree):
        if snail[1] and snail[1] >= 10:
            depth, value = snail[0]+1, snail[1]
            middle = [[depth, value//2], [depth, None], [depth, (value+1)//2]]
            return normalize(tree[:index] + middle + tree[index+1:])
    return tree

def solve():
    """Add up all of the snailfish numbers from the homework assignment in the order they appear. What is the magnitude of the final sum?

    What is the largest magnitude of any sum of two different snailfish numbers from the homework assignment?"""

    numbers = []
    for line in data.splitlines():
        numbers.append(line)
    print("part a:", magnitude(functools.reduce(add, numbers)))

    pairs = permutations(set(numbers), 2)
    print("part b:", max([magnitude(add(pair[0], pair[1])) for pair in pairs]))

if __name__ == "__main__":
    solve()
