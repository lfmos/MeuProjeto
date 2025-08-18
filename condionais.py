#Demonstração do uso de if...
print('Digite a sua idade:')
idade = int(input())

if idade <18:
    print('Vc não é maior de idade!')
    print('Não poderá realizar operações bancárias!')

elif idade >= 65:
    print('Public')
    print('Poderemos oferecer suporte técnico...')

else: 
    print('vc é maior de idade.')
    print('Portanto, podaderá realizar a operação.')
print('Obrigado')