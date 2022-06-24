listagem = ('Lapís',1.5,
            'Caneta',2.0,
            'Cola',3.5,
            'Tesoura',4.5,
            'Compasso',7.0)
print('-'*37)
print(f'{"LISTA DE PREÇOS":^37}')
print('-'*37)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}',end='')
    else:
        print(f'R${listagem[pos]:>.2f}')
print('-'*37)
