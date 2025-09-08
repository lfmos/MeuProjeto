print('Flamengo 2019:')
time = ['1  Diego A',
        '18 Rafinha',
        '3  Rodrigo C',
        '24 Mari',
        '21 Filipe L',
        '5  Arão',
        '15 Gerson',
        '14 Arrascaeta',
        '7  Everton R',
        '27 Bruno H',
        '9  Gabigol']

print('Elenco que começou o jogo contra o River: ')

print()

for jogadores in time: 
    print(jogadores)

print()

print("66' minutos primeira substituição (sai 15 Gerson e entra 10 Diego)")
time.remove('15 Gerson')
time.insert(6, '10 Diego')

print()

print("86' minutos segunda substituição (sai 5 Arão e entra 11 Diego)")

time.remove('5  Arão')
time.insert(5, '11 Vitinho')

print()

print("94' minutos terceira substituição (sai 14 Arrascaeta e entra 25 Piris)")

time.remove('14 Arrascaeta')
time.insert(7, '25 Piris')

print()

print('Elenco do Flamengo ao término do jogo: ')

print()

for jogadores in time: 
    print(jogadores)