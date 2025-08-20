print('o serviço já foi prestado?') 
resposta = input('sim ou não?')

if not resposta:
    print('preciso saber se o serviço já foi prestado!')
elif resposta == 'não':
    print('não tem como vc dar a nota')
elif resposta == 'sim':
    print('uma nota para o serviço de 1-5')

