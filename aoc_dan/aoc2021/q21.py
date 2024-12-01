"""
--- Day 21: Dirac Dice ---
https://adventofcode.com/2021/day/21
"""
from aocd import data

def step(iteration, player):
    """Iterate a triple roll (modulo 10)"""
    roll = (5 - iteration) % 10 + 1
    if iteration % 2 == 0:
        position, score = player[0]
        position = (position + roll) % 10
        score += position + 1
        return ((position, score), player[1])
    else:
        position, score = player[1]
        position = (position + roll) % 10
        score += position + 1
        return (player[0], (position, score))

def leap(iteration, superplayers):
    """Quantum iterate a triple roll"""
    rolls = {3:1, 4:3, 5:6, 6:7, 7:6, 8:3, 9:1}
    if iteration % 2 == 0:
        result = {0:{}, 1:{}, 2:{}, 3:{}, 4:{}, 5:{}, 6:{}, 7:{}, 8:{}, 9:{}}
        for roll, count1 in rolls.items():
            for position, scores in superplayers[0].items():
                nextpos = (position + roll) % 10
                for score, count2 in scores.items():
                    result[nextpos][score + nextpos + 1] = result[nextpos].get(score + nextpos + 1, 0) + count1 * count2 * score
        return (result, superplayers[1])
    else:
        result = {0:{}, 1:{}, 2:{}, 3:{}, 4:{}, 5:{}, 6:{}, 7:{}, 8:{}, 9:{}}
        for roll, count1 in rolls.items():
            for position, scores in superplayers[1].items():
                nextpos = (position + roll) % 10
                for score, count2 in scores.items():
                    result[nextpos][score + nextpos + 1] = result[nextpos].get(score + nextpos + 1, 0) + count1 * count2 * score
        return (superplayers[0], result)

def solve():
    """Play a practice game using the deterministic 100-sided die. The moment either player wins, what do you get if you multiply the score of the losing player by the number of times the die was rolled during the game?

    Using your given starting positions, determine every possible outcome. Find the player that wins in more universes; in how many universes does that player win?"""

    position = []
    for line in data.splitlines():
        position.append(int(line.split()[-1]))
    players = ((position[0]-1, 0), (position[1]-1, 0))
    superplayers = (
        {0:{}, 1:{}, 2:{}, 3:{}, 4:{}, 5:{}, 6:{}, 7:{}, 8:{}, 9:{}},
        {0:{}, 1:{}, 2:{}, 3:{}, 4:{}, 5:{}, 6:{}, 7:{}, 8:{}, 9:{}}
    )
    superplayers[0][position[0]-1] = {1:0}
    superplayers[1][position[1]-1] = {1:0}

    states = []
    for iteration in range(1000):
        players = step(iteration, players)
        states.append(players)
        if max(player[1] for player in players) >= 1000:
            break
    print("part a:", 3 * min(player[1] for player in players) * len(states))

    for iteration in range(9):
        superplayers = leap(iteration, superplayers)
    print("part b:", 0)

if __name__ == "__main__":
    solve()
