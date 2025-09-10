#desafio de listas

hbo=[]; net=[]; sky=[]
plataforma = input('Digite a plataforma: ')

if plataforma == 'hbo':
    filme = input('digite o nome dos filmes que deseja adicionar: ')
    hbo.append (filme)
    print(f'filmes que já foram vistos{hbo}')
elif plataforma == 'net':
    filme = input('digite o nome dos filmes que deseja adicionar: ')
    net.append (filme)
    print(f'filmes que já foram vistos{net}')
elif plataforma == 'sky':
    filme = input('digite o nome dos filmes que deseja adicionar: ')
    sky.append (filme)
    print(f'filmes que já foram vistos {sky}')
else:
    print('algo deu errado tente mais tarde!')