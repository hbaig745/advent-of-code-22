class Stack:
    def __init__(self, contents):
        self.contents = contents

    def enqueue(self, item):
        self.contents.append(item)

    def dequeue(self):
        temp = self.peek()
        del self.contents[-1]
        return temp
    
    def peek(self):
        return self.contents[-1]

one = Stack(['D', 'T', 'R', 'B', 'J', 'L', 'W', 'G'])
two = Stack(['S', 'W', 'C'])
three = Stack(['R', 'Z', 'T', 'M'])
four = Stack(['D', 'T', 'C', 'H', 'S', 'P', 'V'])
five = Stack(['G', 'P', 'T', 'L', 'D', 'Z'])
six = Stack(['P', 'B', 'R', 'Z', 'J', 'Q', 'C', 'D'])
seven = Stack(['S', 'B', 'D', 'J', 'M', 'P', 'T', 'R'])
eight = Stack(['L', 'H', 'R', 'B', 'T', 'V', 'M'])
nine = Stack(['Q', 'P', 'D', 'S', 'V'])

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
    for p in range(int(i[1])):
        mappings[int(i[5])].enqueue(mappings[int(i[3])].dequeue())

string = ''
for num in range(1, 10):
    string = string + mappings[num].peek()

print(string)