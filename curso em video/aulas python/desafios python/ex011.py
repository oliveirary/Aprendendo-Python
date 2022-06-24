print('Quantos latas de tinta da pra te pintar?')
larg=float(input('Qual a largura da parede?'))
alt=float(input('Qual a altura da parede?'))
area=larg*alt
#print('Você precisa de {} latas de tinta'.format(area/desafios python))
print('Sua parede tem a dimenção de {}x{} e a sua área é de {:.2f}m²'.format(larg,alt,area))
tinta=area/2
print('Para pintar a sua parede você precisará de {:.2f} litros de tinta'.format(tinta))

