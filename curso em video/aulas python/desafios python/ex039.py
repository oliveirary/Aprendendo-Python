idade=int(input('Jovem quantos anos você tem? '))
if idade < 18:
    x = 18 - idade
    print('Você ainda terá que se alistar! Faltam {} anos!'.format(x))
elif idade > 18:
    x = idade - 18
    print('Já passou da hora de se alistar! Se passaram {} anos'.format(x))
else:
    idade == 18
    print('Esta na hora de se ESCALAR MONTANHAS! ANDAR DE HELICOPTEROS! QUEIMAR COISAS!...')
    print('\033[1;32mALISTE-SE \033[1;34mJÁ!\033[m')
