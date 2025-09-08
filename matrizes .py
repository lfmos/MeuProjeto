#demonstração de matrizes em Python...
tabuada = []

for x in range (1, 11):
    linhas = []
    for y in range (1, 11):
        linhas.append(x*y)
    tabuada.append(linhas)

for tabela in tabuada:
    print(tabela)