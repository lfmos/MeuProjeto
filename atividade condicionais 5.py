print('1. domingo')
print('2. segunda')
print('3. terça')
print('4. quarta')
print('5. quinta')
print('6. sexta')
print('7. sabado')
print('dia de hoje:')
presente = int(input())

match presente:
    case 1:
        print('ir para a igreja')
    case 2:
        print('hoje tem curso')
    case 3:
        print('ir ver a namorada')
    case 4:
        print('curso e jogo do flamengo')
    case 5:
        print('ir para a igreja')
    case 6:
        print('day off')
    case 7:
        print('day off')
    case _:
        print('opção sem resposta')
