'''from random import randint
print('\033[1;33m-=\033[m'*10)
print('\033[1m      JOKENPÔ\033[m')
print('\033[1;33m-=\033[m'*10)
jogador=int(input('Escolha entre (1)PAPEL, (2)PEDRA ou (3)TESOURA:'))
pc=randint(1,3)
if jogador == 1 and pc == 2:
    print('Eu escolhi PEDRA! PARABÉNS VOCÊ GANHOU!')
if jogador == 1 and pc == 3:
    print('Eu escolhi TESOURA! EU GANHEI E VOCÊ PERDEU')
if jogador == pc:
    print('DEU EMPATE')
if jogador == 2 and pc == 1:
    print('Eu escolhi PAPEL! EU GANHEI E VOCÊ PERDEU')
if jogador == 2 and pc == 3:
    print('Eu escolhi TESOURA! PARABÉNS VOCÊ GANHOU!')
if jogador == 3 and pc == 1:
    print('Eu escolhi PAPEL! PARABÉNS VOCÊ GANHOU')
if jogador == 3 and pc == 2:
    print('Eu escolhi PEDRA! EU GANHEI E VOCÊ PERDEU!')'''
r = 'S'
while r == 'S':
    from random import randint
    from time import sleep
    itens = ('Pedra','Papel','Tesoura')
    computador = randint(0,2)
    print('''Suas opções:
    [0] PEDRA
    [1] PAPEL
    [2] TESOURA''')
    jogador=int(input('Qual é a sua jogada? '))
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    print('-='*11)
    print('Computador jogou {}'.format(itens[computador]))
    print('Jogador jogou {}'.format(itens[jogador]))
    print('-='*11)
    if computador == 0:#COMPUTADOR  PEDRA
        if jogador == 0:
            print('EMPATOU!')
        elif jogador == 1:
            print('JOGADOR GANHOU!')
        elif jogador == 2:
            print('COMPUTADOR GANHO!')
        else:
            print('OPÇÃO INVÁLIDA!')
    elif computador == 1:# COMPUTADOR PAPEL
            if jogador == 0:
                print('COMPUTADOR GANHOU!')
            elif jogador == 1:
                print('EMPATOU!')
            elif jogador == 2:
                print('JOGADOR GANHOU!')
            else:
                print('OPÇÃO INVÁLIDA!')
    elif computador == 2:#COMPUTADOR TESOURA
            if jogador == 0:
                print('JOGADOR GANHOU!')
            elif jogador == 1:
                print('COMPUTADOR GANHOU!')
            elif jogador == 2:
                print('EMPATOU!')
            else:
                print('OPÇÃO INVÁLIDA!')
    r=input('Quer jogar novamente? ([S]Sim e [N]Não)').upper()
    if r == 'N':
        print('Obrigado por jogar!')



