print('posição que joga?')

posições = input()

if not posições:
    print('preciso saber onde joga')
else:
    if posições == 'goleiro' or posições == 'zagueiro' or posições == 'lateral':
        print('defensor')
    elif posições == 'ala' or posições ==  'volante' or posições == 'meia':
        print('meio campo')
    elif posições == 'atacante' or posições == 'sa':
        print('ataque')
    else: 
        print('deve ser reserva')
        