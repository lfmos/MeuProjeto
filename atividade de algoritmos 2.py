x = int(input('Digite o valor de X:'))
y = int(input('Digite o valor de Y:'))
z = int(input('Digite o valor de Z:'))

if x > y > z:
    print('Os numeros estão em ordem decrescente.')
elif z > y > x:
    print('Os numeros estão em ordem crescente')
else:
    print('eles estão misturados')