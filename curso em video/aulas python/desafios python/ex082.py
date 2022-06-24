valores = []
pares = []
impares = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resp in 'Nn':
        break
print(f'A lista completa é {valores}')
for p in valores:
    if p % 2 ==0:
        pares.append(p)
    else:
        impares.append(p)
print(f'os pares são {pares}')
print(f'os impares são {impares}')
