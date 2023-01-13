with open('day 4/input.txt', 'r') as f:
    temp = [
    ]
    for pair in f:
        temp.append(pair[:-1].split(','))

main_list = []

for i in temp:
    t = []
    for s in i:
        s = s.split('-')
        t.append(range(int(s[0]), int(s[1]) + 1))
    main_list.append(t)

def inter(range1, range2):
    xs = set(range1)
    if not xs.intersection(range2):
        return False
    else:
        return True


total = 0
for thing in main_list:
    if inter(thing[0], thing[1]):
        total += 1

print(total)

