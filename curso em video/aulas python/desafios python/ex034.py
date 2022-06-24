#faça um programa que leia o salario do funcionario e calcule o valor do aumento!
#para salarios a cima de 1200 reais aumento de 10% e para inferiores aumento de 15%
print('\033[1;33m-=\033[m'*20)
print('\033[1m          REAJUSTADOR DE SALÁRIO\033[m')
print('\033[1;33m-=\033[m'*20)
salario=float(input('De quanto é o salário que vai ser reajustado?'))
if salario>1200:
    print('O reajuste para o seu salário é R${}'.format(salario*10/100+salario))
else:
    print('O reajuste para o seu salário é R${}'.format(salario*15/100+salario))
print('\033[1;33m-=\033[m'*20)
print('\033[1;35m         WORK HARD & PLAY HARD!!!')
print('\033[1;33m-=\033[m'*20)