"""
--- Day 10: Syntax Scoring ---
https://adventofcode.com/2021/day/10
"""
from aocd import data

CHUNKS = {'(':')', '[':']', '{':'}', '<':'>'}
ERRORS = {')':3, ']':57, '}':1197, '>':25137}
SCORES = {'(':1, '[':2, '{':3, '<':4}

def check(line):
    """Syntax check input character chunks"""
    stack = []
    for character in line:
        if character in CHUNKS:
            stack.append(character)
        elif character == CHUNKS[stack[-1]]:
            stack.pop(-1)
        else:
            return [ERRORS[character], 0]
    score = 0
    while len(stack) > 0:
        score *= 5
        score += SCORES[stack.pop(-1)]
    return [0, score]

def solve():
    """Find the first illegal character in each corrupted line of the navigation subsystem. What is the total syntax error score for those errors?

Find the completion string for each incomplete line, score the completion strings, and sort the scores. What is the middle score?"""

    errors = []
    scores = []
    for line in data.splitlines():
        error, score = check(line)
        if error > 0:
            errors.append(error)
        if score > 0:
            scores.append(score)
    scores = sorted(scores)

    print("part a:", sum(errors))
    print("part b:", scores[len(scores)//2])

if __name__ == "__main__":
    solve()
