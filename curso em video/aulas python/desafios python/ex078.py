'''valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c,v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei ao final da lista')'''
#maior = 0
#menor = 0
lista = []
for cont in range(0,5):
    lista.append(int(input(f'Digite um valor na posição {cont}:')))
    '''if c == 0:
        maior = menor = lista[c]
    else
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]'''
print('-='*20)
print(f'Você digitou os valores {lista}')
print(f'O maior valor é {max(lista)} na posição ',end='')
for i, v in enumerate(lista):
    if v == max(lista):
        print(f'{i}...')
print(f'O menor valor é {min(lista)} na posição',end='')
for i,v in enumerate(lista):
    if v == min(lista):
        print(f'{i}...')

