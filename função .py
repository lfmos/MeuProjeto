#Demonstração do uso de funções...
def apresentar():
    print(f'meu nome é {MyName}.')
    print(f'minha altura é de {MyHeigh} metros.')
    print(f'minha idade é {MyAge} anos.')
    return
def conferir (x):
    if x >= 18:
        print('vc é maior de idade!')
    else:
        print('ops, menor de idade n pode!')
    return
MyName = (input('digite o sue nome: '))
MyHeigh = float(input('digite a sua altura: '))
MyAge = int(input('digite a sua idade: '))

apresentar()
conferir(MyAge)