n1 = int(input('\033[1;33mDigite um valor= '))
n2 = int(input('\033[34mDigite outro valor= '))
n3 = int(input('\033[31mDigite outro valor= '))
r = n1+n2+n3
print('\033[30mA soma entre os valores \033[33m{}\033[m, \033[1;34m{}\033[m e \033[1;31m{} '
      '\033[30msão iguais \033[32m{}\033[m'.format(n1, n2, n3, r))
