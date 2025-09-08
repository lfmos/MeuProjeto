print('responder entre  (a,b,c,d,e)')

gabarito = ['b', 'c', 'a', 'e', 'd']

primeira = input('primeira pergunta: ')
segunda = input('segunda pergunta: ')
terceira = input('terceira pergunta: ')
quarta = input('quarta pergunta: ')
quinta = input('quinta pergunta: ')

acertos = 0
erros = 0

print()

if primeira == gabarito[0]:
    print('acertou')
    acertos += 1
else:
    print('errou')
    erros += 1

if segunda == gabarito[1]:
    print('acertou')
    acertos += 1
else:
    print('errou')
    erros += 1

if terceira == gabarito[2]:
    print('acertou')
    acertos += 1
else:
    print('errou')
    erros += 1

if quarta ==  gabarito[3]:
    print('acertou')
    acertos += 1
else:
    print('errou')
    erros += 1

if quinta == gabarito[4]:
    print('acertou')
    acertos += 1
else:
    print('errou')
    erros += 1

print(f'\nVocê acertou {acertos} perguntas.')
print(f'Você errou {erros} perguntas.')

print()

if acertos >= 3:
    print('Você está acima da média!')
else:
    print('Precisa estudar mais...')