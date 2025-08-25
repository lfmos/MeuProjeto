conta = float(input('Digite o saldo da sua conta:'))
produto = int(input('Digite o valor do produto qu vc deseja:'))

if conta >= produto:
    print('vc pode comprar este produto.')

elif conta < produto:
    print('vc n tem saldo na conta para fazer esta compra.')