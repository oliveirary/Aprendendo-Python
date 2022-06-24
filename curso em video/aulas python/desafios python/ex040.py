n1=float(input('Qual a primeira nota? '))
n2=float(input('Qual a segunda nota? '))
m=(n1+n2)/2
print('Tirando {} e {} a média do aluno é {}'.format(n1,n2,m))
if m >= 7.0:
    print('\033[1;32mVOCÊ FOI APROVADO!\033[m')
elif m <= 5.0:
    print('\033[1;31mVOCÊ FOI REPROVADO!\033[m')
else:
    6.9 > m < 5.0
    print('Você esta de RECUPERAÇÃO!')
