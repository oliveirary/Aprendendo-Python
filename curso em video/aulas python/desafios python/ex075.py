num = (int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')))
print(f'O número 9 aparece {num.count(9)} vez(es)')
if 3 in num:
    print(f'O número 3 aparece na {num.index(3)+1}ª posição')
else:
    print('O número 3 não foi digitado!')
print('Os números pares são: ',end='')
for n in num:
    if n % 2 == 0:
        print(n, end='')

