print('Digite a sua idade:')
def idade ():
    if x >= 18:
        print('temos algumas opções de carros:')
        print('ferrari')
        print('mustang')
        print('lamborghini')
    elif x < 18: 
        print('temos alguns desenhos para serem escolhidos: ')
        print('carros')
        print('formigas')
        print('marte precisa de mães')

x = int(input())
idade(x)