print('='*32)
print('10 PRIMEIROS TERMOS DE UMA P.A. 2.0')
print('='*32)
primeiro = int(input('Digite o 1° termo: '))
razão = int(input('Digite a razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(' {} ->'.format(termo),end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer ver agora? '))
print('Pogressão finalizada com {} termos'.format(total))
