'''Escreve um programa que leia a velocidade de um carro
se ele ultrapassar 80km/h escreva uma mensagem para ele dizendo que ele foi multado
e a multa custa 7 reais por km acima da velocidade!'''

vel=float(input('Qual foi a velocidade que o carro passou?'))
multa=(vel-80)*7
if vel <=80:
    print('\033[1;32mParabéns!\033[m Pode seguir viagem!')
else:
    print('Você foi multado no valor de R${}'.format(multa))
print('DIRIJA COM SEGURANÇA')
