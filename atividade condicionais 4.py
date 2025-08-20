input('Digite o nome do filme que deseja avaliar:')

print('1 pessimo')
print('2 ruim')
print('3 razoavel')
print('4 bom')
print('5 otimo')
nota = int(input())

match nota:
    case 5:
        print('Obrigado pela nota ')
    case 4:
        print('Obrigado pela nota')
    case 3:
        print('Obrigado pela nota')
    case 2:
        print('Porque uma nota tão ruim, pode me dizer o pq?')
        input()
        print('Agradecemos por avaliação!')
    case 1:
        print('Porque uma nota tão ruim, pode me dizer o pq?')
        input()
        print('Agradecemos por avaliação!')
    case _:
        print('Opção não encontrada')