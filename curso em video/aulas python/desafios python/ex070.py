totmil = total = menor = cont = 0
barato = ''
while True:
    produto =  str(input('Produto: '))
    preco = float(input('Preço: '))
    cont += 1
    total += preco
    if preco > 1000:
        totmil +=1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor =  preco
            barato = produto
    resp = str(input('Quer continuar:[S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O valor total das compras é R${total:.2f}')
print(f'Na lista de compras existem {totmil} produtos acima de R$ 1000.')
print(f'O produto mais barato é {barato} e custa {menor}')
