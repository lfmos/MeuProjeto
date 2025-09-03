print('responder entre  (a,b,c,d,e)')

gabarito = ['b', 'c', 'a', 'e', 'd']

primeira = input('primeira pergunta: ')
segunda = input('segunda pergunta: ')
terceira = input('terceira pergunta: ')
quarta = input('quarta pergunta: ')
quinta = input('quinta pergunta: ')

if primeira == gabarito[0]:
    print('acertou a primeira!')
else:
    print('errou a primeira')

if segunda == gabarito[1]:
    print('acertou a segunda')
else:
    print('errou a segunda')

if terceira == gabarito[2]:
    print('acertou a terceira')
else:
    print('errou a terceira')

if quarta ==  gabarito[3]:
    print('acertou a quarta')
else:
    print('errou a quarta')

if quinta == gabarito[4]:
    print('acertou a quinta')
else:
    print('errou a quinta')