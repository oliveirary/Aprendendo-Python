from math import sin, cos , tan, radians
angulo=float(input('Digite um ângulo: '))
seno=sin(radians(angulo))
print('O seno de {} é igual a {:.2f}'.format(angulo,seno))
coseno=cos(radians(angulo))
print('O cosseno de {} é igual a {:.2f}'.format(angulo,coseno))
tang=tan(radians(angulo))
print('A tangente de {} é igual a {:.2f}'.format(angulo,tang))

