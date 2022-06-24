from datetime import date
atual=date.today().year
totmaior=0
totmenor=0
for pessoas in range(1,8):
    nasc=int(input('Digite o ano de nascimento da {}ª pessoa: '.format(pessoas)))
    idade= atual-nasc
    if idade > 21:
        #print('a pessoa tem {} anos e É MAIOR'.format(idade))
        totmaior+=1
    else:
        #print('A pessoa tem {} anos e É MENOR'.format(idade))
        totmenor+=1
print('O total de pessoas maiores é {} e o de menores é {}'.format(totmaior,totmenor))
