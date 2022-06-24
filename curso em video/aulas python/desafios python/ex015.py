km=float(input('Quantos kilometros o carro rodou?'))
dia=(int(input('Quantos dias o carro ficou alugado?')))
p=(60*dia)+(0.15*km)
print('Você deverá pagar R${:.2f} pelo carro alugado!'.format(p))
