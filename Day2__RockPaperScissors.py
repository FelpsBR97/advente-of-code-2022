import pandas as pd

dados = pd.read_csv('input2.txt', delimiter=' ', header = None)

header = ['Opponent','You']

dados.columns = header

def condition_1(row):
    if row['Opponent'] == 'A' and row['You'] == 'X':
     return 4
    elif row['Opponent'] == 'A' and row['You'] == 'Y':
     return 8
    elif row['Opponent'] == 'A' and row['You'] == 'Z':
     return 3
    elif row['Opponent'] == 'B' and row['You'] == 'X':
     return 1
    elif row['Opponent'] == 'B' and row['You'] == 'Y':
     return 5
    elif row['Opponent'] == 'B' and row['You'] == 'Z':
     return 9
    elif row['Opponent'] == 'C' and row['You'] == 'X':
     return 7
    elif row['Opponent'] == 'C' and row['You'] == 'Y':
     return 2
    else:
     return 6
    
def condition_2(row):
    if row['Opponent'] == 'A' and row['You'] == 'X':
     return 3
    elif row['Opponent'] == 'A' and row['You'] == 'Y':
     return 4
    elif row['Opponent'] == 'A' and row['You'] == 'Z':
     return 8
    elif row['Opponent'] == 'B' and row['You'] == 'X':
     return 1
    elif row['Opponent'] == 'B' and row['You'] == 'Y':
     return 5
    elif row['Opponent'] == 'B' and row['You'] == 'Z':
     return 9
    elif row['Opponent'] == 'C' and row['You'] == 'X':
     return 2
    elif row['Opponent'] == 'C' and row['You'] == 'Y':
     return 6
    else:
     return 7

dados['points(part1)'] = dados.apply(condition_1, axis=1)
dados['points(part2)'] = dados.apply(condition_2, axis=1)

TotalPoints_1 = dados['points(part1)'].sum()
TotalPoints_2 = dados['points(part2)'].sum()


print('Total Points(part 1):', TotalPoints_1, '\nTotal Points(part 2):', TotalPoints_2)