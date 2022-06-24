func = 0
n1=int(input('Digite o 1° número: '))
n2=int(input('Digite o 2° número: '))
while func != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair''')
    func=int(input('Digite o que deseja fazer: '))

    if func == 1:
        s = n1 + n2
        print('A soma de {} com {} é {}!'.format(n1,n2,s))
    elif func == 2:
        m = n1 * n2
        print('A multiplicação entre {} e {} é {}!'.format(n1,n2,m))
    elif func == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior número entre {} e {} é {}'.format(n1,n2,maior))
    elif func == 4:
        print('Digite os novos números: ')
        n1=int(input('Primeiro número:'))
        n2=int(input('Segundo número: '))
    elif func == 5:
        print('Finalizando!...')
    else:
        print('Opção inválida tente novamente!')
    print('*='*20)
print('Fim do Programa!')