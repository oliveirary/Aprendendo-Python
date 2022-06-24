frase=str(input('Digite a frase: ')).upper().strip()
palavras=frase.split()
junto=''.join(palavras)
inverso=junto[::-1]
#inverso=''
'''for letra in range(len(junto)-1,-1,-1):
    inverso+=junto[letra]'''
print('O inverso de {} é {}'.format(junto,inverso))
if inverso == junto:
    print('Temos um PALINDRÔMO')
else:
    print('A frase digitada NÃO FORMA um PALINDRÔMO')
