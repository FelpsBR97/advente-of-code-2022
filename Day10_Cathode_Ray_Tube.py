import math

with open ('input10.txt', 'r') as file:
    commands = file.read().strip().split('\n')

x = 1
op = 0
signalStrength = 0
cycles = [20, 60 ,100 ,140, 180, 220]

# ---- part 1 ----

for command in commands:
    if command.startswith('noop'):
        op += 1
        for cycle in cycles:
            if op == cycle:
                signalStrength += op * x
    else:

        op += 1
        for cycle in cycles:
            if op == cycle:
                signalStrength += op * x

        op += 1
        for cycle in cycles:
            if op == cycle:
                signalStrength += op * x
        
        x += int(command.split(' ')[1])

print('\nAnswer for part 1: ', signalStrength, '\n')

# ---- part 2 ----

cur_X = 1
X = [1 for _ in range(241)]
op = 0

for command in commands:
    if command.startswith('noop'):
        op += 1
        X[op] = cur_X
    else:
        X[op+1] = cur_X
        cur_X += int(command.split(' ')[1])

        op += 2
        X[op] = cur_X

CTR = [['' for _ in range(40)] for _ in range(6)]

for row in range(6):
    for col in range(40):
        index = row * 40 + col + 1
        if abs(X[index - 1] - col) <= 1:
            CTR[row][col] = '■'
        else:
            CTR[row][col] = ' '

print('\nAnswer for part 2:')

for row in range(6):
    print(CTR[row])