executado = input('o serviço foi executado (sim/não)')
if executado == 'não':
    reclamar = input('Descreva a sua reclamação: ')
    nota = 0
elif executado == 'sim':
    nota = int(input('Digite sua nota (1 a 5):'))
    if nota == 1:
        print('muito ruim')
    elif nota == 2:
        print('ruim')
    elif nota == 3:
        print('razoavel')
    elif nota == 4:
        print('bom')
    elif nota == 5:
        print('otimo')
    else:
        print('o numero digitado está errado...')
else:
    print('não foi digitado sim ou não...')
    