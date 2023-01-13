one = ['D', 'T', 'R', 'B', 'J', 'L', 'W', 'G']
two = ['S', 'W', 'C']
three = ['R', 'Z', 'T', 'M']
four = ['D', 'T', 'C', 'H', 'S', 'P', 'V']
five = ['G', 'P', 'T', 'L', 'D', 'Z']
six = ['P', 'B', 'R', 'Z', 'J', 'Q', 'C', 'D']
seven = ['S', 'B', 'D', 'J', 'M', 'P', 'T', 'R']
eight = ['L', 'H', 'R', 'B', 'T', 'V', 'M']
nine = ['Q', 'P', 'D', 'S', 'V']

mappings = {
    1 : one,
    2 : two,
    3 : three,
    4 : four,
    5 : five,
    6 : six,
    7 : seven,
    8 : eight,
    9 : nine
}

with open('day 5/input.txt', 'r') as f:
    main = []
    for line in f:
        main.append(line.split())


for i in main:
    mappings[int(i[5])].extend(mappings[int(i[3])][-(int(i[1])):])
    del mappings[int(i[3])][-int(i[1]):]

string = ''
for num in range(1, 10):
    print(mappings[num])
    string = string + mappings[num][-1]

print(string)