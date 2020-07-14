print('Gerador de PA')
print('=-' * 9)
first = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = first
cont = 1
while cont <= 10:
    print(f'{termo} ➡ ', end='')
    termo += r
    cont += 1
print('FIM')
