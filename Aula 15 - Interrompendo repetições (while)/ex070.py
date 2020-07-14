print('-'*31)
print(f'{"LOJA SUPER RADICORI":^31}')
print('-'*31)
barato = ' '
cont = total = menor = milcont = 0
while True:
    produto = ' '
    produto = input('Nome do produto: ')
    preço = float(input('Preço: RS'))
    total += preço
    if preço > 1000:
        milcont += 1
    cont += 1
    opção = ' '
    if cont == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    opção = input('Quer continuar? [S/N] ').strip().upper()
    if opção in 'N':
        break
print(f'{" FIM DO PROGRAMA ":-^31}')
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {milcont} produtos custando mais de RS1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
