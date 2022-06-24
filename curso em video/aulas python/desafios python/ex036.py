#Escreva um programa para calcular o emprestimo bancario para compra de uma casa.
#O programa vai perguntar, o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal sabendo que ela não deverá exceder 30% do salário do comprador.
#ou então o emprestimo será negado.

casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o salário do comprador? '))
anos = int(input('De quantos anos será o empréstimo? '))
prestacao = casa/(anos*12)
minimo = salario * 30 /100
print('Para pagar uma casa de R${} em {} anos'.format(casa,anos))
print('A prestação será de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('O emprestimo foi CONCEDIDO')
else:
    print('O emprestimo foi NEGADO!')




'''casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o salário do comprador? '))
anos = int(input('De quantos anos será o empréstimo? '))
parcelas = anos*12
prest = casa / parcelas
if prest > salario*30/100:
    print('O emprestimo com prestações de R${:.2f} foi NEGADO'.format(prest))
else:
    print('O emprestimo foi APROVADO no valor de R${:.2f} por mês!'.format(prest))'''





