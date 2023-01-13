with open('day 6/input.txt', 'r') as f:
    for line in f:
        string = line

def is_repeating(string):
    visited = []
    for char in string:
        if char in visited:
            return True
        else:
            visited.append(char)

    return False

found = False
total = 14
while found == False:
    #check first 4 chars is repeating
    if not is_repeating(string[:14]):
    #if it not is then break
        found = string[:14]
    #if true then remove first char and add to total
    else:
        string = string[1:]
        total += 1


print(total)