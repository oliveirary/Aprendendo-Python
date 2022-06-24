print('='*32)
print('10 PRIMEIROS TERMOS DE UMA P.A. 2.0')
print('='*32)
primeiro = int(input('Digite o 1° termo: '))
razão = int(input('Digite a razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(' {} ->'.format(termo),end='')
    termo += razão
    cont += 1
print('FIM')