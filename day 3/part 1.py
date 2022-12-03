with open('day 3/input.txt' , 'r') as f:
    arr = []
    for line in f:
        arr.append(line[:-1])

def find(firstpart, secondpart):
    for char in firstpart:
        if char in secondpart:
            return char

def priority(char):
    num = ord(char)
    if char == char.upper():
        num -= 38
    else:
        num -= 96

    return num


total = 0

for i in arr:
    firstpart, secondpart = i[:len(i)//2], i[len(i)//2:]
    common_character = find(firstpart, secondpart)
    total = total + priority(common_character)

print(total)
