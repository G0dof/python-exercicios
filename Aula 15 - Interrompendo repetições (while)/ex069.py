idade = contidade = contmasc = contfem = 0
while True:
    print('=-'*15)
    print('CADASTRE UMA PESSOA')
    print('=-' * 15)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]: ')).strip().upper()[0]
    print('--'*15)
    opção = ' '
    while opção not in 'SN':
        opção = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opção in 'Nn':
        break
    if idade >= 18:
        contidade += 1
    if sexo in 'Mm':
        contmasc += 1
    if sexo in 'Ff' and idade < 20:
        contfem += 1
print(f'Total de pessoas com mais de 18 anos: {contidade}')
print(f'Ao todo temos {contmasc} homens cadastrados')
print(f'E temos {contfem} mulheres com menos de 20 anos')
