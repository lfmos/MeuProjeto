# De Celsius para Kelvin e Fahrenheit
x = int(input('Digite a temperatura em Celcius:'))

transf = (x * 9/5) + 32
print('Temp em fahrenheit é:', transf, 'F')

transf = x + 273.15
print('Temp em Kelvin é:', transf, 'K')

# De Kelvin para Celsius e Fahrenheit

y = float(input('Digite a temperatura em Kelvin:'))

transf = y - 273.15
print('Temp em Celcius é:', transf, 'C')

transf = (y - 273.15) * 9/5 + 32
print('Temp em fahrenheit é:', transf, 'F')

# De Fahrenheit para Celsius e Kelvin

z = float(input('Digite a temperatura em Fahrenheit:'))

transf = (z - 32) * 5/9
print('Temp em Celcius é:', transf, 'C')

transf = (z - 32) * 5/9 + 273,15
print('Temp em Kelvin é:', transf, 'K')