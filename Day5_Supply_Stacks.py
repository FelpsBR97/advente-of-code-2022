#import data
with open('input5.txt', 'r') as file:
    all_boxes, instructions = (i.splitlines() for i in file.read().strip('\n').split('\n\n'))

stacks = {int(number):[] for number in all_boxes[-1].replace(' ', '')}
indexes = [index for index, char in enumerate(all_boxes[-1]) if char != ' ']

#function to display all stack
def displayStacks():
    print('\n\nStacks: \n')
    for stack in stacks:
        print(stack, stacks[stack])
    print('\n')

#load the initial stack configuration into the stacks
def laodStacks():
    for string in all_boxes[:-1]:
        stack_num = 1
        for index in indexes:
            if string[index] != ' ':
                stacks[stack_num].insert(0, string[index])
            stack_num += 1

#clean all stacks loaded
def emptyStacks():
    for stack_num in stacks:
        stacks[stack_num].clear()

def getStacksEnd():
    top_boxes = ''
    for stack in stacks:
        top_boxes += stacks[stack][-1]
    return top_boxes

laodStacks()

#  ---- part 1 ----

for instruction in instructions:
    instruction = instruction.replace('move', '').replace('from ', '').replace('to ', '').strip().split(' ')
    instruction = [int(i) for i in instruction]

    boxes = instruction[0]
    from_stack = instruction[1]
    to_stack = instruction[2]

    for box in range(boxes):
        box_removed = stacks[from_stack].pop()
        stacks[to_stack].append(box_removed)

print('\nAnswer for part 1: ', getStacksEnd(), '\n')

# ---- part 2 ----

emptyStacks()
laodStacks()

for instruction in instructions:
    instruction = instruction.replace('move', '').replace('from ', '').replace('to ', '').strip().split(' ')
    instruction = [int(i) for i in instruction]

    boxes = instruction[0]
    from_stack = instruction[1]
    to_stack = instruction[2]

    box_to_remove = stacks[from_stack][-boxes:] #find the boxes to remove
    stacks[from_stack] = stacks[from_stack][:-boxes] #removing boxes
    for box in box_to_remove:
        stacks[to_stack].append(box) #adding boxes to diff stack

print('\nAnswer for part 2: ', getStacksEnd(), '\n')