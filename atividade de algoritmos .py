input('Digite o nome do seu time:')

tabela = int(input('Digite a posiçaõ do sue time na tabela:'))

if tabela == 1:
    print('CAMPEÃO!')
elif tabela <= 6 and tabela >= 2:
    print('vai para a libertadores')
elif tabela <= 12 and tabela <= 7:
    print('vai para sul-americana')
elif tabela >= 16 and tabela <= 20:
    print('seu time está rebaixado')
elif tabela > 20:
    print('Essa posição na classificação não existe!') 
else:
    print('seu time está no meio de tabela')