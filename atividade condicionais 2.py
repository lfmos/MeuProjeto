primeiro = float(input('nota do primeiro trimestre:'))
segundo = float(input('nota do segundo trimestre:'))
terceiro = float(input(' nota do terceiro trimestre:'))
quarto = float(input('nota do quarto trimestre:'))

media = (primeiro + segundo + terceiro + quarto) * 1/4


print('está sua média geral:', media)

if media < 6:
    print('infelizmente vc n passou')
elif media >= 6:
    print('parabes passou de ano!!!')