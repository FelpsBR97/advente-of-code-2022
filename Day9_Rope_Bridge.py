import math

with open('input9.txt', 'r') as file:
    movements = file.read().strip().split('\n')

orientation = {'L': (-1, 0), 'R': (1, 0), 'U': (0, -1), 'D': (0, 1)}
Hx, Hy = 0, 0
Tx, Ty = 0, 0
visited_pt1 = { (0,0) }

# ---- part 1 ---- 

for movement in movements:

    direction, num = movement.split(' ')
    m = orientation[direction]

    for i in range(int(num)):
        #Head moviment
        Hx, Hy = Hx + m[0], Hy + m[1] 

        #Tail movimet
        dx, dy = Hx - Tx, Hy - Ty
        if abs(dx) > 1 or abs(dy) > 1:
            if dx:
                Tx += math.copysign(1, dx)
            if dy:
                Ty += math.copysign(1, dy)
            visited_pt1.add((Tx, Ty))

print('\n Answer for part 1: ', len(visited_pt1), '\n')

# ---- part 2 ---- 
#Part 2 is a generalization for part 1, before we have 2 knots moving, now we have 10.
#I'm gona keep the part 1 the same but part 2 solve part 1 if we change 10 knots to only 2.

def move_function(movements, num_knots):
    knots = [(0, 0)] * num_knots
    visited_pt2 = { (0,0) }
    for movement in movements:

        direction, num = movement.split(' ')
        m = orientation[direction]

        for i in range(int(num)):

            #Head moviment
            knots[0] = (knots[0][0] + m[0], knots[0][1] + m[1])

            #Tails movimet
            for i in range(1 , len(knots)):
                dx = knots[i-1][0] - knots[i][0]
                dy = knots[i-1][1] - knots[i][1]

                if abs(dx) > 1 or abs(dy) > 1:
                    newx, newy = knots[i][0], knots[i][1]
                    if dx:
                        newx = knots[i][0] + math.copysign(1, dx)
                    if dy:
                        newy = knots[i][1] + math.copysign(1, dy)
                    knots[i] = (newx, newy)
                visited_pt2.add(knots[-1])
                
    return len(visited_pt2)

part2 = move_function(movements, 10)
print('\n Answer for part 2: ', part2, '\n')