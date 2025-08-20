print('pedra, papel ou tesoura')
um = input()
print('pedra, papel ou tesoura')
dois = input()

if not um or not dois:
    print('precisa falar oq vc quer para jogar!')
else:
    if um == 'papel' and dois == 'pedra':
        print('1 ganhou')
    elif um == 'papel' and dois == 'tesoura':
        print('2 ganhou')
    elif um == 'papel' and dois == 'papel':
        print('empate')
    elif um == 'pedra' and dois == 'pedra':
        print('empate')
    elif um == 'pedra' and dois == 'papel':
        print('2 ganhou')
    elif um == 'pedra' and dois == 'tesoura':
        print('1 ganhou')
    elif um == 'tesoura' and dois == 'pedra':
        print('2 ganhou')
    elif um == 'tesoura' and dois == 'papel':
        print('1 ganhou')
    elif um == 'tesoura' and dois == 'tesoura':
        print('empate')
    