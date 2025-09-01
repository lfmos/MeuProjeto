#Par ou impar
import random
def resposta(w):
    if w % 2 == 0:
        print(f'{w} é par')
        print('usuário wins')
    else:
        print(f'{w} é impar')
        print('computador wins')

x = random.randint(0, 10)
y = int(input('Digite um número: '))
w = x + y
resposta(w)