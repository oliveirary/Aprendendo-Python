unica = [[],[]]
for n in range(1,8):
    unica.append(int(input(f'Digite o {n}° valor:')))
    if n %2 == 0:
        unica[0].append(n)
    else:
        unica[1].append(n)
unica[0].sort()
unica[1].sort()
print('-='*20)
print(f'Os números pares foram: {unica[0]}')
print(f'Os números impares foram: {unica[1]}')
print(unica)