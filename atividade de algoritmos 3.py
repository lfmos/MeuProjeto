print('digite os valores dos lados do triangulo')

x = int(input())
y = int(input())
z = int(input())

if x == y == z:
    print('equilátero')
elif x == y or x == z or y == z:
    print('isósceles')
else:
    print('escaleno')