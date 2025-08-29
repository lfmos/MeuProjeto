#demonstração de estrutura repetitiva...
contador = 0; senha = ''
while senha != '1234':
    print('Digite a senha:')
    senha = input()

    if senha == '1234':
        print('senha correta!')
        break
    else:
        print('senha errada...')
    contador += 1
    if contador == 3:
        print('3 tentativas excedidas!')
        break