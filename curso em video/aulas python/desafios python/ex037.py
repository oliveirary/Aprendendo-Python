#Escreva um programa que leia um número inteiro qualquer e peça para o usuario escolher qual será
#a base de conversão; -1 para binario, -2 para octal e -3 para hexadecimal
num=int(input('Digite o número a ser convertido: '))
conv=int(input('Digite 1 para binário, 2 para octal e 3 para hexadecimal: '))
res = 'x'
if conv == 1:
    num = bin(num)
    res = 'binário'
elif conv == 2:
    num = oct(num)
    res = 'octal'
else:
    conv == 3
    num = hex(num)
    res = 'hexadecimal'
print('O número em {} é {}: '.format(res,num[2:]))
