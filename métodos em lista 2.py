#Demonstração de métodos em listas...

print('vou almoçar em um restaurante a quilo!')

original = ['arroz', 'feijão', 'batata', 'alface', 'frango']
print('eis, a minha comida: ', original)
#se for colocado entre colchetes não iguala as variantes e sim só as informações contidas
derivada = original [:]
print ('meu amigo irá comer também: ', derivada)

print('vou alterar as opções sem ele ver...')
original.remove('arroz')
original.remove('feijão')
original.remove('alface')
original.append('picanha')
original.append('linguiça')

print('amiguinho, me mostre o que vc vai comer"')
print('claro! dá uma conferida', derivada)

print('meu novo prato sem ele saber', original)