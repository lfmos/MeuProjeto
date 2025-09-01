def nome(n):
    if not n:
        print('Preciso saber o seu nome!')    

    else:
        print(f'Olá,', n,'.')


def cidade(c):
    if c == 'rj' or c == 'rio de janeiro' or c == 'Rio de Janeiro':
        print('seja bem vindo a cidade maravilhosa!')
    elif not c:
        print('Digite o nome do lugar...')
    else:
        print('seja bem vindo a', c)
    
print('Digite o seu nome: ')
n = input()

print('Digite sua cidade: ')
c = input()

nome(n)
cidade(c)