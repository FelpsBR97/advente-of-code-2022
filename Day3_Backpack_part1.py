import pandas as pd

#import data
data = pd.read_csv('input3.txt', header = None)
header = ['all_itens']
data.columns = header

#to slip itens in each pocket
data['left_pocket'] = data['all_itens'].apply(lambda x: x[:len(x) // 2])
data['right_pocket'] = data['all_itens'].apply(lambda x: x[len(x) // 2:])

#find the item how appears on each pocket
def find_iten(row):
    str1 = row['left_pocket']
    str2 = row['right_pocket']
    item = [char1 for char1 in str1 if char1 in str2]
    return item[0]


data['item'] = data.apply(lambda row: find_iten(row), axis=1)

#convert the letter to priority number
def map_item(char):
    p_number = ord(char)
    if 'a' <= char <= 'z':
        return p_number - ord('a') + 1
    elif 'A' <= char <= 'Z':
        return p_number - ord('A') + 27

data['p_number'] = data['item'].apply(map_item)

print(data)
print(data['p_number'].sum())