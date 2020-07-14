n = int(input('\033[1;33mDigite um número: '))
nd = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[32m', end='')
        nd += 1
    else:
        print('\033[31m', end='')
    print(f'{c} ', end='')
print('\n\033[O número {} foi divisível {} vezes'.format(n, nd))
if nd == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
