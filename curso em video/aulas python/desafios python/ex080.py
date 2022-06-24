valores = []
for c in range(0,5):
    n = (int(input('Dígite um valor: ')))
    if c == 0 or n > valores[-1]:
        valores.append(n)
        print(f'Adiconado ao final da lista')
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                print(f'Adicionado na lista na posiçãp {pos}')
                break
            pos += 1
print('-='*20)
print(f'Os valores digitados em ordem foram {valores}')
print('-='*20)
