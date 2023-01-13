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

def range_subset(range1, range2):
    if not range1:
        return True
    if not range2:
        return False 
    if len(range1) > 1 and range1.step % range2.step:
        return False
    return range1.start in range2 and range1[-1] in range2

total = 0
for thing in main_list:
    if range_subset(thing[0], thing[1]) or range_subset(thing[1], thing[0]):
        total += 1

print(total)

