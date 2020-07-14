soma = 0
maior = 0
cont = 0
hvelho = ''
for pessoa in range(1, 5):
    print(f'----- {pessoa}ª PESSOA -----')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip()
    soma += idade
    if pessoa == 1 and sexo in 'Mm':
        maior = idade
        hvelho = nome
    else:
        if idade > maior and sexo in 'Mm':
            maior = idade
            hvelho = nome
    if sexo in 'Ff' and idade < 20:
        cont += 1
print(f'A media de idade do grupo é de {soma/4} anos')
print(f'O homem mais velho tem {maior} anos e se chama {hvelho}')
print(f'Ao todo são {cont} mulheres com menos de 20 anos')
