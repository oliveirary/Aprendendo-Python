from random import randint
computador = randint(0,10)
print('Sou seu computador e pensei  em um número entre 0 a 10')
print('Será que você adivinha qual é?')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez!')
        elif jogador > computador:
            print('Menos... Tente mais uma vez!')
print('Acertou com {} tentativas! PARABÉNS!'.format(palpite))
