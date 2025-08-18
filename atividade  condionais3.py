altura = float(input('Digite sua altura:'))
peso = float(input('Digite o seu peso:'))

imc = peso / (altura * altura)
if imc > 25:
    print('Acima do peso ideal')
elif imc < 18:
    print('Abaixo do peso ideal')
else :
    print('O seu peso está OK!')