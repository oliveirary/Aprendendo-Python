from random import randint
from time import sleep
sorteio = []
print('-='*10)
print('JOGOS DA MEGA SENA')
print('-='*10)
jogos = int(input('Quantos jogos quer que eu sorteie? '))
print(f'{"=-"*5}SORTEANDO OS NÚMEROS{"-="*5}',end='')
for c in range(0,jogos):
    for x in range(0,6):
        y = randint(0,60)
        if y not in sorteio:
            sorteio.append(y)
        else:
            y= randint(0,60)
            sorteio.append(y)
    sorteio.sort()
    sleep(1)
    print(f'\nJogo {c+1}: {sorteio}', end='')
    sorteio.clear()
print(f'\n{"-="*7}BOA SORTE!{"-="*7}',end='')
