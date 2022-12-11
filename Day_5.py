import numpy as np

stacks = []
instructions = []

with open('input_day5.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip('\n')
        if '[' in line:
            stacks.append([char for char in line [1::4]])
        elif 'move' in line:
            split=(line.split(" "))
            instructions.append(([int(char) for char in split[1::2]]))
      

stacks_t = np.array(stacks)[::-1].transpose()

stacks = []
for stack in stacks_t:
    stack = list(stack)
    if ' ' in stack:
        cutoff = stack.index(' ')
        stacks.append(stack[:cutoff])
    else:
        stacks.append(stack)

for instruction in instructions:
    to = stacks[(instruction[2]-1)]
    n = instruction[0]
    print(to)
    to += stacks[(instruction[1]-1)][-n:]
    stacks[(instruction[1]-1)]=stacks[(instruction[1]-1)][:-n]


for stack in stacks:
    print(stack[-1])