res = 'S'
quant = soma = maior = menor = media = 0
while res in 'Ss':
    num = int(input('Digite um numero: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    res= str(input('Quer continuar[S/N]: '))
media = soma / quant
print(f'Você digitou {quant} números e a média entre eles é {media:.1f}!')
# print('Você digitou {} números e a média entre eles é {:.1f}!'.format(quant,media))
print(f'E o maior número é {maior}, o menor {menor}')


