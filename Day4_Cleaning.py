import pandas as pd

#import data
data = pd.read_csv('input4.txt', header = None)
header = ['elf_1','elf_2']
data.columns = header

#split the data, for 'a' and 'b' for elf_1 and elf_2
data[['a_elf_1','b_elf_1']] = data['elf_1'].str.split('-', expand=True)
data[['a_elf_2','b_elf_2']] = data['elf_2'].str.split('-', expand=True)
data.drop(['elf_1','elf_2'], axis=1, inplace=True)

#transform all colunns into int variable
data['a_elf_1'] = data['a_elf_1'].astype(int)
data['b_elf_1'] = data['b_elf_1'].astype(int)
data['a_elf_2'] = data['a_elf_2'].astype(int)
data['b_elf_2'] = data['b_elf_2'].astype(int)

#condition for part 1
def condition_1(row):
    if row['a_elf_1'] >= row['a_elf_2'] and row['b_elf_1'] <= row['b_elf_2']:
        return 1
    elif row['a_elf_2'] >= row['a_elf_1'] and row['b_elf_2'] <= row['b_elf_1']:
        return 1
    else:
        return 0
    
#condition for part 2
def condition_2(row):
    if row['b_elf_1'] < row['a_elf_2']:
        return 0
    elif row['b_elf_2'] < row['a_elf_1']:
        return 0
    else:
        return 1

#apply the conditions
data['fully_contais'] = data.apply(condition_1, axis=1)
data['overlap'] = data.apply(condition_2, axis=1)

print(data)
print(data['fully_contais'].sum())
print(data['overlap'].sum())