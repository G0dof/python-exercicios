print('{:=^40}'.format('LOJAS PEDROCA'))
preço = int(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] á vista dinheiro/cheque
[ 2 ] á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção > 4 or opção <1:
    print('TENTE NOVAMENTE!')
elif opção == 1:
    dsct1 = preço-(preço*10/100)
    print(f'Sua compra de R${preço} vai custar RS{dsct1:.2f} no final.')
elif opção == 2:
    dsct2 = preço-(preço*5/100)
    print(f'Sua compra de R${preço} vai custar R${dsct2:.2f} no final.')
elif opção == 3:
    parcela = preço/2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f}')
    print(f'Sua compra de RS{preço} vai custar RS{preço}')
elif opção == 4:
    total = preço+(preço*20/100)
    parcela2 = int(input('Quantas parcelas? '))
    juros = total/parcela2
    print(f'Sua compra será parcelada em {parcela2}x de RS{juros:.2f}')
    print(f'Sua compra de RS{preço} vai custar R${total:.2f}')

