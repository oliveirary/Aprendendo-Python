a=int(input('Digite o 1° número: '))
b=int(input('Digite o 2° número: '))
if a == b:
    print('Não existe número maior, os dois são iguais')
elif a > b:
    print('O número {} é maior'.format(a))
else:
    print('o número {} é o maior'.format(b))
