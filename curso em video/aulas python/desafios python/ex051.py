print('='*32)
print('10 PRIMEIROS TERMOS DE UMA P.A.')
print('='*32)
primeiro=int(input('Digite o 1° termo: '))
razão=int(input('Digite a razão: '))
decimo=primeiro+(10-1)*razão
for c in range(primeiro,decimo+razão,razão):
    print(c,end=' -> ')
print('FIM')
