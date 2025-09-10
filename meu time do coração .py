#desafi de condicionais

naturalidade = input('qual é a sua naturalidade? ')

if naturalidade == 'carioca':
    carioca = input('qual é o seu time? ')
    match carioca:
        case 'flamengo':
            print('maior')
        case 'vasco':
            print('pior ainda')
        case 'fluminense':
            print('lixo')
        case 'botafogo':
            print('lixo')
        case _:
            print('esse time n tem aq n!')
elif naturalidade == 'paulista':
    paulista = input('qual é o seu time? ')
    match paulista:
        case 'sp':
            print('lixo')
        case 'palmeiras':
            print('lixo')
        case 'santos':
            print('lixo')
        case 'corinthians':
            print('lixo')
        case _:
            print('esse time n tem aq n!')
elif naturalidade == 'gaucho':
    gaucho = input('qual é o seu time? ')
    match gaucho:
        case 'inter':
            print('podre')
        case 'gremio':
            print('podre')
        case _:
            print('esse time n tem aq n!')

else:
    print('n mora, se esconde!')