#Par ou impar

x = int(input('Digite o seu número: '))
y = int(input('Digite o outro número: '))

w = x + y

if w % 2 == 0:
    print(f'{w} é par')
    print('usuário wins')
else:
    print(f'{w} é impar')
    print('computador wins')