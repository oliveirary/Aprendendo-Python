while True:
    from random import randint
    print('*='*20)
    print('VAMOS JOGAR PAR OU IMPAR')
    print('*='*20)
    num = int(input('Escolha um número: '))
    jogador = str(input('Você escolhe PAR ou IMPAR?[P/I] ')).upper().strip()[0]
    computador = randint(0,20)
    resp = (computador + num)%2
    soma= num + computador
    cont = 0
    if resp == 0:
        print('-'*20)
        print(f'Você jogou {num} e o computador {computador} e a soma deu: PAR')
        print('-' * 20)
        if jogador == 'P':
            cont+=1
            print('VOCÊ VENCEU!')
        elif jogador == 'I':
            print('VOCÊ PERDEU')
            print('=' *20)
            print(f'GAME OVER! Você venceu {cont} vezes.')
            print('=' * 20)
            break
    else:
        print('-' * 20)
        print(f'Você jogou {num} e o computador {computador} e a soma deu: IMPAR')
        print('-' * 20)
        if jogador == 'I':
            cont+=1
            print('VOCÊ VENCEU!')
        elif jogador == 'P':
            print('VOCÊ PERDEU')
            print('='*20)
            print(f'GAME OVER! Você venceu {cont} vezes.')
            print('=' *20)
            break
