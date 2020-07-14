from datetime import date
ano = int(input('Ano de Nascimento: '))
ano2 = date.today().year
ano3 = ano2 - ano
print(f'O atleta tem {ano3} anos.')
if ano3 <= 9:
    print('Classificação: MIRIM')
elif ano3 <= 14:
    print('Classificação: INFANTIL')
elif ano3 <= 19:
    print('Classificação: JUNIOR')
elif ano3 <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
