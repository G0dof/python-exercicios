nx = int(input('\033[1;33mDigite um número para ver sua tabuada: '))
for c in range(1, 11):
    print(f'\033[30m{nx} x {c} \033[33m= \033[34m{nx*c} ')
