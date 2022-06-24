while True:
    print('*='*20)
    num = int(input('Você quer ver a tabuada de qual valor? '))
    print('*=' * 20)
    if num < 0:
        print('OBRIGADO!')
        break
    for c in range(1,11):
        res = num * c
        print(f'{num}X{c}={res}')