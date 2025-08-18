# Demonstrção do uso da condicional match/casa...

print('1. excelente')
print('2. bom')
print('3. regular')
print('4. ruim')
print('5. pessimo')
print('digite o número referente ao estado da chuteira:')
estado = int(input())

match estado:
    case 1:
        print('perfeita! vou pagar 500 reais ')
    case 2:
        print(' bom! Vou pagar 200 reais')
    case 3:
        print('mais o menos, mas ainda vou querer pago 150 reais')
    case 4:
        print('Foi mal, mas to suave!')
    case 5:
        print('Não quero não, joga isso fora pf')
    case _:
        print('Marcou errado heim')
