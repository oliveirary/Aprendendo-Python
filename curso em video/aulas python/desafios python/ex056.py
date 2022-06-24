somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
nummulher = 0
for p in range(1,5):
    print('-------{}ª PESSOA--------'.format(p))
    nome = str(input('Nome da {}ª pessoa: '.format(p))).strip()
    idade = int(input('Idade da {}ª pessoa:'.format(p)))
    sexo = str(input('Sexo[M/F] da  {}ª pessoa: '.format(p))).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        nummulher += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho é o {} e ele tem {} anos'.format(nomevelho,maioridadehomem))
print('No grupo tem {} mulheres a baixo de 20 anos'.format(nummulher))
