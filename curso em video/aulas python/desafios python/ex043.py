peso=float(input('Qual é o seu peso? '))
altura=float(input('Qual é sua altura? '))
imc= peso/(altura*altura)
if imc < 18.5:
    print('Seu IMC é {:.1f} e você está ABAIXO do peso ideal!'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC é {:.1f} e você esta no PESO IDEAL!'.format(imc))
elif 25 <= imc < 30:
    print('Seu IMC é {:.1f} e você esta com SOBREPESO!'.format(imc))
elif 30 <= imc < 40:
    print('Seu IMC é {:.1f} e você esta com OBESIDADE!'.format(imc))
else:
    imc > 40
    print('Seu IMC é {:.1f} e você esta com OBESIDADE MÓRBIDA!'.format(imc))
