#Demonstração de operadores lógicos em condicionais...
print('o que vc vai fazer amanhã de manhã?')
print('dormir / estudar / planejar')
manha = input()
print('o que vc vai fazer amanhã de tarde?')
print('jogar / treinar / trabalhar')
tarde = input()

if not manha or not tarde:
    print('vc precisa dizer o que vai fazer!')
else:
    if manha == 'dormir'or tarde == 'jogar':
        print('vc está desperdiçando o seu dia!')
    elif manha == 'estudar' or tarde == 'treinar':
        print('que bom! vc irá se aperfeiçoar!')
    elif manha == ' planejar' and tarde == 'trabalhar':
        print('Para trabalhar melhor, devo planejar!')
    else:
        print('não coombinamos estas ações...')
    
print('tenha um bom dia!')