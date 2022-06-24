while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: ')).strip().upper()[0]
    next = str(input('Quer cadastrar mais?[S/N] ')).strip().upper()[0]
    cpes18 = chome = cmul20 = 0
    if idade > 18:
        cpes18+=1
    elif idade < 20:
        if sexo == 'F':
            cmul20+=1
    elif sexo == 'M':
        chome+=1
    if next == 'N':
        print(f'Ao total temos {cpes18} com mais de 18 anos.')
        print(f'Foram {chome} homens cadastrados.')
        print(f'E temos {cmul20} mulheres com menos de 20 anos.')
        break

