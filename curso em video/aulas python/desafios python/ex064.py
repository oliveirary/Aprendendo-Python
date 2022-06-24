num = cont = soma = 0
num = int(input('Digite um numero para somar: [999 para parar] '))
while num != 999:
    soma += num
    cont +=1
    num = int(input('Digite um numero para somar: [999 para parar] '))
print('Você digitou {} e a soma é {}'.format(cont,soma))

