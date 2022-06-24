sexo=str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]
while sexo not in "MmFf":
    sexo=str(input('Dados inválidos! Por favor informe novamente seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))


