# Faça um programa que leia 3 numeros e diga qual é o menor e qual é o maior
a = int(input('Digite o 1° número: '))
b = int(input('Digite o 2° número: '))
c = int(input('Digite o 3° número: '))
#Verificando o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#Verificando o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('o número MENOR é {}'.format(menor))
print('o número MAIOR é {}'.format(maior))
