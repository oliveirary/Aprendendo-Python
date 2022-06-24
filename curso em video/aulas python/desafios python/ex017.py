import math
cat1=float(input('Digite o comprimento do cateto oposto:'))
cat2=float(input('Digite o comprimento do cateto adjacente'))
'''hipo=(cat1**2+cat2**2)**(1/2)
print('A porra da hipotenusa é igual a: {:.2}'.format(hipo))'''
hip=math.hypot(cat1,cat2)
print('A porra da hipotenusa é {:.2f}'.format(hip))
