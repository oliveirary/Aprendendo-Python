valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if r in 'Nn':
        break
valores.sort(reverse=True)
print('-='*20)
print(f'Foram digitados {len(valores)} valores')
print(f'A ordem decrescente é {valores}')
if 5 in valores:
    print('O número 5 está na lista')
else:
    print('O número 5 não esta na lista')
