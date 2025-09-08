#demonstração de matrizes em Python...
print('Eis, o teclado númerico do terminal:')
teclado = [[1, 2, 3], 
           [4, 5, 6],
           [7, 8, 9]]

senha = []

print('Digite a sua senha de 4 dígitos...')
for x in range(0, 4):
    senha.append(int(input(f'Digite o dígito{x+1}: ')))

for x in range(0, 3):
    for y in range(0, 3):
        for z in range(0, 4):
            if teclado [x] [y] == senha [z]:
                teclado [x] [y] = 0

print('Eis, a senha digitada: ', senha)
print('Confira, as teclas acionadas:')
for listas in teclado:
    print(listas)