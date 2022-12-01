with open('day 1/input.txt', 'r') as f:
    temp = []
    main_list = []
    for line in f:
        if line == '\n':
            main_list.append(temp)
            temp = []
        else:
            temp.append(int(line[:-1]))

top_3 = [0, 0, 0]

for l in main_list:
    total = sum(l)
    for score in range(len(top_3)):
        if top_3[score] < total:
            top_3[score] = total
            break

print(main_list)
print(sum(top_3))