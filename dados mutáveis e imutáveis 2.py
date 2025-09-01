#demonstração de acesso de listas...

print('vou montar a marmita com 5 alimentos!')
marmita = ['feijão', ' arroz', 'legumes', 'salada', 'carne']
print('Eis, a nossa recomendção:', marmita)

resposta = input('Quer montar uma marmita diferente (Sim/Não)?')
if resposta == 'sim':
    for x in range(len(marmita)):
        print(f'Digite o {x+1}o. item do cardápio:')
        marmita[x] = input()
    print('A marmita montada foi:', marmita)
    print('Os três primeiro itens foram:', marmita[0:3])
    print('O ultimo item da marmita foi:', marmita[-1])
else:
    print('Ok. Vc decide...')

print(marmita[:])
print(marmita[2:3])
print(marmita[0:4:2])
print(marmita[-3:-1])