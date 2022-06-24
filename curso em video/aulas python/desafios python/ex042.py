print('-='*20)
print('Analizador de Triângulos')
print('-='*20)
r1=float(input('Primeiro seguimento: '))
r2=float(input('Segundo seguimento: '))
r3=float(input('Terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r3:
    print('Esses seguimentos PODEM formar um triângulo')
    if r1 == r2 == r3:
        print('Esse triângulo é EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('Esse triângulo é ESCALENO')
    else:
        print('Esse triângulo é ISÓSCELES')
else:
    print('Esses seguimentos NÃO PODEM formar um triângulo')

