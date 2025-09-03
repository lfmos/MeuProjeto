#Demonstração de métodos em listas...

inss = ['maria', 'manoel', 'josé', 'isabela']
print('eis, a fila do inss: ', inss)

novo = input('insira mais uma pessoa: ')
inss.append(novo)
print('conferir a nova lista: ', inss)

print('vou tirar a ultima pessoa desta lista...')
especial = inss.pop()

print('agora, vou colocá-la na frente de todos!')
inss.insert(0, especial)
print('conferindo a lista: ', inss)

print('maria não gostou e reclamou...')
inss.remove('maria')
print('e agora, ela saiu "pê da vida"', inss)

print('para não ter mais reclamação, vamos atender...')
inss.sort()
print('... em ordem alfabética: ', inss)

print('onde está esta nova pessoa chamada', especial, '?')
print('ela agora ficou na posição', inss.index(especial) + 1, '!')