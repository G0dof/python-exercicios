d = float(input('Qual a distância em Km de sua viagem? '))
if d <= 200:
    preço1 = 0.5*d
    print(f'Você pagará R${preço1:.2f} em sua passagem')
else:
    preço2 = 0.45*d
    print(f'Você pagará R${preço2:.2f} em sua passagem')
