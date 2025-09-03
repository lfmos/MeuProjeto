print('Flamengo 2019:')
time = ['1 diego a',
        '18 rafinha',
        '3 rodrigo c',
        '24 mari',
        '21 filipe l',
        '5 arão',
        '15 gerson',
        '14 arrascaeta',
        '7 everton r',
        '27 bruno h',
        '9 gabigol']

print('elenco que começou o jogo contra o river: ')
for jogadores in time: 
    print(jogadores)

print('66 minutos primeira substituição (sai 15 gerson e entra 10 diego)')
time.remove('15 gerson')
time.insert(6, '10 diego')

print('86 minutos primeira substituição (sai 15 gerson e entra 10 diego)')

time.remove('5 arão')
time.insert(5, '11 vitinho')

time.remove('14 arrascaeta')
time.insert(7, '25 piris')

print('Flamengo terminol o jogo com esse elenco ', time)