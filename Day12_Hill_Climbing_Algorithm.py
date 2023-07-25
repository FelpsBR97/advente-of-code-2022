from collections import deque

heightmap = [list(x) for x in open('input12.txt').read().strip().splitlines()]

for r, row in enumerate(heightmap):
    for c, height in enumerate(row):
        if height == 'S':
            S_row = r
            S_col = c
            heightmap[r][c] = 'a'
        if height == 'E':
            E_row = r
            E_col = c
            heightmap[r][c] = 'z'

visited = {(S_row, S_col)}

queue_part1 = deque()
queue_part1.append((0, S_row, S_col))

# --- part 1 ---

while queue_part1:
    dist_1, row_1, col_1 = queue_part1.popleft()
    for next_row_1, next_col_1 in [(row_1 + 1, col_1), (row_1 - 1, col_1), (row_1, col_1 + 1), (row_1, col_1 - 1)]:
        if next_row_1 < 0 or next_col_1 < 0 or next_row_1 >= len(heightmap) or next_col_1 >= len(heightmap[0]):
            continue
        if (next_row_1, next_col_1) in visited:
            continue
        if ord(heightmap[next_row_1][next_col_1]) - ord(heightmap[row_1][col_1]) > 1:
            continue
        if next_row_1 == E_row and next_col_1 == E_col:
            print('\nAnswer for part 1:',dist_1 + 1, '\n')
            break
        visited.add((next_row_1, next_col_1))
        queue_part1.append((dist_1 + 1, next_row_1, next_col_1))

# ---- part 2 ----

visited_part2 = {(E_row, E_col)}

queue_part2 = deque()
queue_part2.append((0, E_row, E_col))

while queue_part2:
    dist_2, row_2, col_2 = queue_part2.popleft()
    for next_row_2, next_col_2 in [(row_2 + 1, col_2), (row_2 - 1, col_2), (row_2, col_2 + 1), (row_2, col_2 - 1)]:
        if next_row_2 < 0 or next_col_2 < 0 or next_row_2 >= len(heightmap) or next_col_2 >= len(heightmap[0]):
            continue
        if (next_row_2, next_col_2) in visited_part2:
            continue
        if ord(heightmap[next_row_2][next_col_2]) - ord(heightmap[row_2][col_2]) < -1:
            continue
        if heightmap[next_row_2][next_col_2] == 'a':
            print('\nAnswer for part 2:',dist_2 + 1, '\n')
            exit()      #here is an exit than break because have lots of 'a' heights, if was a break, gonna print distance for all 'a'
        visited_part2.add((next_row_2, next_col_2))
        queue_part2.append((dist_2 + 1, next_row_2, next_col_2))