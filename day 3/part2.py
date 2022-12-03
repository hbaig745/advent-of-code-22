with open('day 3/input.txt' , 'r') as f:
    temp = []
    arr = []
    for line in f:
        if len(temp) == 3:
            arr.append(temp)
            temp = []
            temp.append(line[:-1])
        else:
            temp.append(line[:-1])
    arr.append(temp)

def find(array):
    for char in array[0]:
        if char in array[1] and char in array[2]:
            print(char)
            return char

def priority(char):
    num = ord(char)
    if char == char.upper():
        num -= 38
    else:
        num -= 96

    return num

total = 0
print(arr)
for group in arr:
    common_character = find(group)
    total = total + priority(common_character)

print(total)
