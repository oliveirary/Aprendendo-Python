from datetime import date
atual= date.today().year
nasc=int(input('Que ano você nasceu? '))
anos= atual - nasc
categoria = 'X'
if anos<= 9:
    categoria = 'MIRIM'
elif anos <= 14:
    categoria = 'INFANTIL'
elif anos <= 19:
    categoria = 'JUNIOR'
elif anos <= 20:
    categoria = 'SENIOR'
elif anos > 25:
    categoria = 'MASTER'
print('O atleta tem {} anos e está na categoria: {}'.format(anos,categoria))
