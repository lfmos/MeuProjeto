#feito pelo professor...
opcao = 999
series = []; servicos = []; temporadas = []

while opcao != 0:
    print('escolha a operação: ')
    print('1. cadastrar / 2. exibir / 3. editar / 4. excluir')
    opcao = int(input('Digite 0 para sair: '))

    if opcao == 1:
        serie = input('Digite o nome da série: ')
        servico = input('Digite o nome do serviço: ')
        temporada = input('Digite a temporada que já assistiu: ')
        series.append(serie); servicos.append(servico); temporadas.append(temporada)

    print(series, servicos, temporadas)