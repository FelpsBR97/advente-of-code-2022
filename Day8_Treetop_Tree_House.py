with open('input8.txt', 'r') as file:
    all_trees = [tree_line.strip() for tree_line in file.readlines()]

ROWS = len(all_trees)
COLUMNS = len(all_trees[0])
edges = COLUMNS*2 + ((ROWS-2)*2)
visible_trees = edges
scores = []

#iterate with all trees, without considerating the edges
for row in range(1 ,ROWS-1):
    for col in range(1, COLUMNS-1):
        tree = all_trees[row][col]

        #gatting all trees in 4 directions
        right = [all_trees[row][col+i] for i in range(1, COLUMNS - col)]
        left = [all_trees[row][col-i] for i in range(1, col+1)]
        up = [all_trees[row-i][col] for i in range(1, row+1)]
        down = [all_trees[row+i][col] for i in range(1, ROWS - row)]

        # ---- part 1 ----
        if max(right)<tree or max(left)<tree or max(up)<tree or max(down)<tree:
            visible_trees += 1
        
        # ---- part 2 ----
        tree_scenic_score =  1
        for lst in (left, right, up, down):
            distance = 0
            for i in range(len(lst)):
                if lst[i] < tree:
                    distance += 1
                else:
                    distance += 1
                    break

            
            tree_scenic_score *= distance
        
        scores.append(tree_scenic_score)

print('\nAnswer for part 1: ', visible_trees, '\n')
print('\nAnswer for part 2: ', max(scores), '\n')