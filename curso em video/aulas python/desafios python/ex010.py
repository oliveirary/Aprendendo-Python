print('Conversor de Real para Dolar')
real=float(input('Quantos reais você quer converter? R$'))
#print('Você tem:{:.2f}dolares'.format(real/3.27))
dolar=real/3.27
print('Com R${:.2f} você pode comprar U${:.2f}'.format(real,dolar))
