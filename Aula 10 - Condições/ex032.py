from datetime import date

ano = int(input('\033[1;33mQue ano quer analisar? \033[1;30mColoque \033[1;36m0 '
                '\033[1;30mpara analisar o ano atual:\033[m '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('\033[1;32mO ano {} é BISSEXTO\033[m'.format(ano))
else:
    print('\033[1;31mO ano {} NÃO É BISSEXTO\033[m'.format(ano))
