numeros = []
while True:
    n = int(input('Digite um número: '))
    if n not in numeros:
        numeros.append(n)
        print('Número adicionado com sucesso!')
    else:
        print('Valor duplicado! Não irei adiciona-lo.')
    r = str(input('Quer continuar? [S/N]'))
    if r in 'Nn':
        break
numeros.sort()
print('-='*20)
print(f'A ordem crescente dos números é: {numeros}')
print('-='*20)