with open('day 1/input.txt', 'r') as f:
    temp = []
    main_list = []
    for line in f:
        if line == '\n':
            main_list.append(temp)
            temp = []
        else:
            temp.append(int(line[:-1]))

highest = 0
temp = 0

for l in main_list:
    if sum(l) > highest:
        highest = sum(l)
print(main_list)
print(highest)