n = int(input('\033[1;33mDigite um número: \033[m'))
if (n % 2) == 0:
    print(f'\033[1;34mO número {n} é par\033[m')
else:
    print(f'\033[1;31mO número {n} é ímpar\033[m')
