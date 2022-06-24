# Faça um programa que leia qualquer ano  diga se ele é BISSEXTO
from datetime import date
ano=int(input('Que ano você quer analizar?(Digite 0 para analizar o ano atual) ' ))
if ano==0:
    ano=date.today().year
if ano%4==0 and ano%100!=0 or ano%400==0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))
