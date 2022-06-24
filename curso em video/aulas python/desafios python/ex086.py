lista = [[], [], []]
for i in range(3):
    for j in range(3):
        lista[i].append(int(input(f'Digite um valor [{i},{j}]:')))
print('='*50)
for x in range(len(lista)):
    for y in range(len(lista)):
         print(f'[{lista[x][y]}]', end='')
    print('')
