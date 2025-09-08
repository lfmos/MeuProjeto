print('JOGO DO QUADRADO MÁGICO')
print('preencha o vetor com números de um a nove (sem repetir números) e a soma de todas as linhas, colunas e diagonais será igual a quinze.')

a = int(input('numero n1: '))
b = int(input('numero n2: '))
c = int(input('numero n3: '))
d = int(input('numero n4: '))
e = int(input('numero n5: '))
f = int(input('numero n6: '))
g = int(input('numero n7: '))
h = int(input('numero n8: '))
i = int(input('numero n9: '))


quadrado = [[a, b, c], 
           [d, e, f],
           [g, h, i]]

somas = [
    a + b + c,  
    d + e + f,  
    g + h + i,  
    a + d + g,  
    b + e + h,  
    c + f + i,  
    a + e + i,  
    c + e + g   
]

valido = True
for soma in somas:
    if soma != 15:
        valido = False
        break

if valido:
    print('Parabéns! Você fez um quadrado mágico!')
else:
    print('Errado! As somas não dão 15.')

for linha in quadrado:
    print(linha)