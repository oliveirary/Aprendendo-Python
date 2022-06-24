'''Escreva um programa qu faça o computador (pensar) em um nuémero
e faça o usuario advinhar esse numero escolhido pelo computador
o programa deverá dizer se o usuario perdeu ou ganhou'''
'''from random import choice
n1=0
n2=1
n3=2
n4=3
n5=4
n6=5
num=[n1,n2,n3,n4,n5,n6]
z=choice(num)
print('Vamos jogar! Adivinhe o número em que eu estou pensando!')
x=int(input('Digite um numero de 0 a 5: '))
if x==z:
    print('Eu escolhi {}! PARABÉNS! Você ganhou!'.format(z))
else:
    print('Eu escolhi {}!VOCÊ PERDEU! TENTE DE NOVO!'.format(z))'''
from random import randint
from time import sleep
z=randint(0,5)
print('-=-'*20)
print('\033[1;32mVamos jogar! Adivinhe o número em que eu estou pensando!\033[m')
print('-=-'*20)
x=int(input('Digite um numero de 0 a 5: '))
print('PROCESSANDO')
sleep(2)
if x==z:
    print('Eu escolhi {}! \033[32mPARABÉNS! \033[1:30mVocê ganhou!'.format(z))
else:
    print('Eu escolhi {}!\033[31mVOCÊ PERDEU!\033[1:30m TENTE DE NOVO!'.format(z))