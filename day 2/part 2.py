with open('day 2/input.txt', 'r') as f:
    main = []
    for line in f:
        main.append(line.split())


def find(first, second):

    paper = 'Y'
    rock = 'X'
    sciz = 'Z'

    if first == 'A':
        if second == 'Y':
            return rock
        if second == 'X':
            return sciz
        if second == 'Z':
            return paper
    if first == 'B':
        if second == 'Y':
            return paper
        if second == 'X':
            return rock
        if second == 'Z':
            return sciz
    if first == 'C':
        if second == 'Y':
            return sciz
        if second == 'X':
            return paper
        if second == 'Z':
            return rock


def result(first, second):

    win = 6
    draw = 3
    lose = 0

    if first == 'A':
        if second == 'Y':
            return win
        if second == 'X':
            return draw
        if second == 'Z':
            return lose
    if first == 'B':
        if second == 'Y':
            return draw
        if second == 'X':
            return lose
        if second == 'Z':
            return win
    if first == 'C':
        if second == 'Y':
            return lose
        if second == 'X':
            return win
        if second == 'Z':
            return draw



def score(choice):
    
    if choice == 'Y':
        return 2
    if choice == 'X':
        return 1
    if choice == 'Z':
        return 3


total = 0
for row in main:
    first = row[0]
    res = row[1]

    second = find(first, res)
    total = total + result(first, second) + score(second)

print(total)
