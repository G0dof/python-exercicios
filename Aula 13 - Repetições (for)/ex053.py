frase = input('Digite uma frase: ').upper().replace(' ', '')
inverso = frase[::-1]
print(f'O inverso de {frase} é {inverso}')
if frase == inverso:
    print('Temos um palídromo!')
else:
    print('NÃO temos um palídromo')