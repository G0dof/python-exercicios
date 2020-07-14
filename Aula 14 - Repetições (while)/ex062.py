print('Gerador de PA')
print('=-' * 9)
first = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = first
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} ➡ ', end='')
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quandos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados')