import math
peso = float(input('Qual o seu peso? (Kg) '))
altura = float(input('Qual a sua altura? (m) '))
imc = peso/(altura**2)
print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal.')
elif 18.5 <= imc < 25:
    print('PARABÉNS! Você está no PESO IDEAL.')
elif 25 <= imc < 30:
    print('Você está ACIMA DO PESO normal.')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE!')
else:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')