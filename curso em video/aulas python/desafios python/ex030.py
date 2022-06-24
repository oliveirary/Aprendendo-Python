#Escreva um programa que leia o numero que o usuario digitar e diga se é PAR OU IMPAR!
num=int(input('Me diga um número: '))
res=num%2
if res == 0:
    print('O número {} é \033[1;32mPAR\033[m!'.format(num))
else:
    print('O número {} é \033[1;31mIMPAR\033[m!'.format(num))
