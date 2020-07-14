from datetime import date
cont1 = 0
cont2 = 0
soma = 0
atual = date.today().year
for ano in range(1, 8):
    ano1 = int(input(f'Em que ano a {ano}ª pessoa nasceu? '))
    if atual - ano1 >= 18:
        cont1 += 1
    elif atual - ano1 < 18:
        cont2 += 1
print(f'Ao todo tivemos {cont1} pessoas maiores de idade')
print(f'E também tivemos {cont2} pessoas menores de idade')