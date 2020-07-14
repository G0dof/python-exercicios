preço = float(input('Qual o preço?: '))
porc = 5 % preço
dsnt1 = porc/100*preço
dsnt2 = preço-dsnt1
print('O desconto será de {:.2f} reais'.format(dsnt2))



