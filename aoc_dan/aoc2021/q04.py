"""
--- Day 4: Giant Squid ---
https://adventofcode.com/2021/day/4
"""
from aocd import data

def score(balls, card):
    """Simulate and score a bingo game with a single card"""
    transpose = list(map(list, card))
    for row, numbers in enumerate(card):
        for col, number in enumerate(numbers):
            transpose[col][row] = number
    drawn = []
    for index, ball in enumerate(balls):
        drawn.append(ball)
        if len(drawn) < len(card):
            continue
        for row in range(len(card)):
            if all(number in drawn for number in card[row]) or all(number in drawn for number in transpose[row]):
                count = 0
                for numbers in card:
                    count += sum([number for number in numbers if number not in drawn])
                return [index, count * drawn[-1]]
    return [0, 0]

def solve():
    """To guarantee victory against the giant squid, figure out which board will win first. What will your final score be if you choose that board?

    Figure out which board will win last. Once it wins, what would its final score be?"""

    balls = []
    bingos = []
    card = []
    for line in data.splitlines():
        if line == "":
            if len(card) > 0:
                bingos.append(score(balls, card))
                card = []
            continue
        if len(balls) == 0:
            balls = list(map(int, line.split(",")))
        else:
            card.append(list(map(int, line.split())))

    best = score(balls, card)
    worst = best
    for bingo in bingos:
        if bingo[0] < best[0]:
            best = bingo
        if bingo[0] > worst[0]:
            worst = bingo

    print("part a:", best[1])
    print("part b:", worst[1])

if __name__ == "__main__":
    solve()
