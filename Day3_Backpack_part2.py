import pandas as pd
import numpy as np

#import data
data = pd.read_csv('input3.txt', header = None)
header = ['all_elfs']
data.columns = header

#number of elfs in each columm
num_elfs = data.shape[0] // 3

elf1 = np.array(data['all_elfs'].iloc[::3][:num_elfs]) #first elf and every 3 next elfs
elf2 = np.array(data['all_elfs'].iloc[1::3][:num_elfs])#second elf and every 3 next elfs
elf3 = np.array(data['all_elfs'].iloc[2::3][:num_elfs])#third elf and every 3 next elfs

#new data, every line represent a group of 3 elfs
data = pd.DataFrame({'elf1': elf1,
                     'elf2': elf2,
                     'elf3': elf3,})

#find the badge how appears in each elf backpack
def find_badge(row):
    itens_elf1 = set(row['elf1'])
    itens_elf2 = set(row['elf2'])
    itens_elf3 = set(row['elf3'])
    badge = itens_elf1 & itens_elf2 & itens_elf3
    if badge:
        return badge.pop()
    
data['badge'] = data.apply(find_badge, axis=1)

#convert the letter to badge number
def map_item(char):
    p_number = ord(char)
    if 'a' <= char <= 'z':
        return p_number - ord('a') + 1
    elif 'A' <= char <= 'Z':
        return p_number - ord('A') + 27

data['badge_num'] = data['badge'].apply(map_item)

print(data)
print(data['badge_num'].sum())
