d = int(input('Quantos dias você utilizou o carro? '))
km = int(input('Quantos kilômetros você percorreu? '))
pago = (d*60) + (km*0.15)
print('O total a pagar é de R${:.2f}'.format(pago))

