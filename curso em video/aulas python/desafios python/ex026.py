frase=str(input('Digite uma frase:')).strip().upper()
print('A letra (A) aparece:{} vezes na frase'.format(frase.count('A')))
print('A primeira vez que a letra (A) aparece é em: {}'.format(frase.find('A')+1))
print('A ultima vez que a letra (A) aparece é em: {}'.format(frase.rfind('A')+1))
