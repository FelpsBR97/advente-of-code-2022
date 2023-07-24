#For this problem I'm gonna import the input11.txt "manually" because have 8 monkeys and gonna save time
#but on the other hand is not a scalable solution if we have like 100 monkeys

def MONKEYS():
    return [
        {
            'itens': [89, 84, 88, 78, 70],
            'op': lambda n: n * 5,
            'test': lambda n: 7 if n % 7 else 6,
        },
        {
            'itens': [76, 62, 61, 54, 69, 60, 85],
            'op': lambda n: n + 1,
            'test': lambda n: 6 if n % 17 else 0,
        },
        {
            'itens': [83, 89, 53],
            'op': lambda n: n + 8,
            'test': lambda n: 3 if n % 11 else 5,
        },
        {
            'itens': [95, 94, 85, 57],
            'op': lambda n: n + 4,
            'test': lambda n: 1 if n % 13 else 0,
        },
        {
            'itens': [82, 98],
            'op': lambda n: n + 7,
            'test': lambda n: 2 if n % 19 else 5,
        },
        {
            'itens': [69],
            'op': lambda n: n + 2,
            'test': lambda n: 3 if n % 2 else 1,
        },
        {
            'itens': [82, 70, 58, 87, 59, 99, 92, 65],
            'op': lambda n: n * 11,
            'test': lambda n: 4 if n % 5 else 7,
        },
        {
            'itens': [91, 53, 96, 98, 68, 82],
            'op': lambda n: n * n,
            'test': lambda n: 2 if n % 3 else 4,
        },
    ]
    

def KeepAwaySimulation(n_rounds ,wl_factor):
    monkeys = MONKEYS()
    inspections = [0] * len(monkeys)
    for round in range(n_rounds):
        for i, m in enumerate(monkeys):
            for item in m['itens']:
                inspections[i] += 1
                item = m['op'](item)
                item = wl_factor(item)
                monkeys[m['test'](item)]['itens'].append(item)
            m['itens'] = []
    answer = sorted(inspections)[-2] * sorted(inspections)[-1]
    return answer

# ---- part 1 ----
answer_part1 = KeepAwaySimulation(20, lambda n: n // 3)
print('\nAnswer for part 1: ', answer_part1)

# ---- part 2 ----
answer_part2 = KeepAwaySimulation(10000, lambda n: n % (7*17*11*13*19*2*5*3))
print('\nAnswer for part 2: ', answer_part2, '\n')