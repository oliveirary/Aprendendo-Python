preco=(float(input('Qual é o preço do produto? R$')))
cond=str(input('No DINHEIRO ou no CHEQUE ou CARTÃO?')).upper()
if cond == 'CARTÃO':
    VP = str(input('Qual é a condição? VISTA OU PARCELADO?')).upper()
    if VP == 'VISTA':
        des = preco - (preco * 5 / 100)
        print('O valor total a ser pago é R${} com desconto de 5%'.format(des))
    if VP == 'PARCELADO':
        parc=int(input('Será parcelado em quantas vezes?'))
        if parc == 2:
            print('O valor total a ser pago é R${}'.format(preco))
        if parc >= 3:
            prest = preco * 20 / 100 + preco
            print('O valor total a ser pago é R${}'.format(prest))
if cond == 'DINHEIRO' or 'CHEQUE':
    des=preco-(preco*10/100)
    print('O valor do produto é R${} com desconto de 10%'.format(des))


