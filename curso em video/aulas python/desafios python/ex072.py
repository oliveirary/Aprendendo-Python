num = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze',
       'doze','treze','catorze','quinze','dezeseis','dezesete','desoito','dezenove','vinte')
while True:
    usuario = int(input('Dígite um número entre 0 e 20: '))
    if 0 <= usuario <= 20:
        print(f'Você digitou o número {num[usuario]}')
        esc = str(input('Quer digitar de novo?[S/N]')).strip().upper()[0]
        if esc == 'Ss':
            print('OK')
        else:
            break
    else:
        print('Tente novamente')
