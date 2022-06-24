'''Desenvolva um programa que pergunte a distancia de uma viagem em km
e calcule o preço da passagem, cobrando R$0,50 até 200 km e R$0,45 para viagens mais longas
dist=int(input('A viagem tem quantos km? '))
if dist <=200:
    print('A passagem custará: R${}'.format(dist*0.50))
else:
    print('A passagem custará: R${}'.format(dist*0.45))
print('Boa Viagem!')'''

print('\033[1;34m-=\033[m'*15)
print('\033[1;33mCALCULADOR DE PASSAGENS!\033[m')
print('\033[1;34m-=\033[m'*15)
dist=int(input('A viagem tem quantos km? '))
if dist <=200:
    preco=dist*0.50
else:
    preco=dist*0.45
print('A passagem custará R${}'.format(preco))
print('\033[1;33mBOA VIAGEM!\033[m')
