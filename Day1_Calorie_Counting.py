import pandas as pd

with open('input1.txt', 'r') as f:
    input1 = [line.strip() for line in f.readlines()]

elfs = []
current_group = []
for value in input1:
    if value == '':
        if current_group:  # Fill the current group if not empty
            elfs.append(current_group)
            current_group = []
    else:
        current_group.append(value)

# Fill the last group if not empty
if current_group:
    elfs.append(current_group)

elf_calories = [[int(valor) for valor in sublist] for sublist in elfs] #Convert 'str' to 'int'

elf_data = {}

for i, elf in enumerate(elf_calories):
    elf_name = f"Elf {i+1}"
    elf_data[elf_name] = {
        "Total Calories": sum(elf),
    }

df = pd.DataFrame.from_dict(elf_data, orient='index')
df = df.sort_values(by="Total Calories", ascending=False)

print(df) #Show the elf with more total calories on top. Total calories with elf on top the list is 70509