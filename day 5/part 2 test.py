import re
from collections import deque

with open('day 5/input.txt', 'r') as f:
    lines = [line.strip('\n') for line in f.readlines()]

# helper function to split string into 4 char chunks
split = lambda x: [x[i:i+4].strip() for i in range(0, len(x), 4) ]

# part 1
stacks, cmds = list(reversed(lines[:lines.index('')])), lines[lines.index('')+1:]

st = {x: deque() for x in split(stacks[0])}

for s in stacks[1:]:
    for i, v in enumerate(split(s), start=1):
        st[str(i)].append(v) if v else None

for cmd in cmds:
    move, from_, to = re.findall('\d+', cmd)
    for i in range(int(move)):
        st[to].append(st[from_].pop())

answer = ''.join([st[str(k)].pop() for k in range(1, len(st.keys())+1) if st[str(k)]]).replace('[', '').replace(']', '')
print(answer)

# part 2
stacks, cmds = list(reversed(lines[:lines.index('')])), lines[lines.index('')+1:]

st = {x: deque() for x in split(stacks[0])}

for s in stacks[1:]:
    for i, v in enumerate(split(s), start=1):
        st[str(i)].append(v) if v else None

for cmd in cmds:
    move, from_, to = re.findall('\d+', cmd)
    xx = reversed([st[from_].pop() for i in range(int(move))])
    st[to].extend(xx)

answer = ''.join([st[str(k)].pop() for k in range(1, len(st.keys())+1) if st[str(k)]]).replace('[', '').replace(']', '')
print(answer)