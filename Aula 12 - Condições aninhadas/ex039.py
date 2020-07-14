from datetime import date
ano = int(input('Ano de nascimento: '))
ano2 = date.today().year
ano3 = ano2 - ano
print(f'Quem nasceu em {ano} tem {ano3} anos em {ano2}')
if ano3 < 18:
    print(f'Ainda faltam {18-ano3} anos para o alistamento')
elif ano3 > 18:
    print(f'Você já deveria ter se alistado há {ano3-18} anos')
    print(f'Seu alistamento foi em {ano+18}')
elif ano3 == 18:
    print(f'Você tem que se alistar IMEDIATAMENTE!')
