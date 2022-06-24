print('-='*20)
print('Analizador de Triângulos')
print('-='*20)
r1=float(input('Primeiro seguimento: '))
r2=float(input('Segundo seguimento: '))
r3=float(input('Terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r3:
    print('Esses seguimentos PODEM formar um triângulo')
else:
    print('Esses seguimentos NÃO PODEM formar um triângulo')