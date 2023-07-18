with open('input7.txt', 'r') as file:
    commands = [command.strip() for command in file.readlines()]

path = '/home'
dirs = {'/home':0}

#'run' all commands, commands starts with '$'
for command in commands:
    if command[0] == '$':

        #ignore listing
        if command[2:4] == 'ls':
            pass

        #changing paths
        elif command[2:4] == 'cd':

            #go '/home'
            if command[5:6] == '/':
                path = '/home'
            
            #go one step back on path
            elif command[5:7] == '..':
                path = path[:path.rfind('/')]
            
            #change path
            else:
                dir_name = command[5:]
                path = path + '/' + dir_name
                dirs.update({path:0})
    
    elif command[0:3] == 'dir':
        pass

    #get file size and add to directories it was found
    else:
        size = int(command[:command.find(' ')])

        dir = path
        for i in range(path.count('/')):
            dirs[dir] += size
            dir = dir[:dir.rfind('/')]


total = 0
limit = 30000000 - (70000000 - dirs['/home'])
valid_dirs = []

for dir in dirs:

    # ---- part 1 ----
    if dirs[dir] <= 100000:
        total += dirs[dir]
    
    # ---- part 2 ----
    if limit <= dirs[dir]:
        valid_dirs.append(dirs[dir])
        
    smallest_dir = min(valid_dirs)

print('\n Answer for part 1: ', total, '\n')
print('\n Answer for part 2: ', smallest_dir, '\n') 