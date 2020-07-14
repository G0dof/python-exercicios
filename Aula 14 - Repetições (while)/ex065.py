n = cont = soma = média = 0
opção = 'S'
while opção != 'N':
    n = int(input('Digite um número: '))
    cont += 1
    soma += n
    média = soma / cont
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    opção = input('Quer continuar? [S/N]: ').strip().upper()[0]
print(f'Você digitou {cont} números e a média foi {média}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
