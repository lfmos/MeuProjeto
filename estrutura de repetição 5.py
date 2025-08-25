#demonstração do uso de estrutura repetitiva...

numero = 1
while numero >= 0:
    print('digite um número negativo para sair:')
    numero = int(input())
    continue
    print('este texto não sera exibido! mas')
else:
    print('O número digitado foi:', numero)

#mesmo com o break ou continue o texto tracejado n vai ser executado... mas com o continue vai conseguir executar o else
