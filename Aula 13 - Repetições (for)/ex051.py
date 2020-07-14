s = 0
print('=' * 25)
print('   10 TERMOS DE UMA PA     ')
print('=' * 25)
termo = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = termo+(10-1)*r
for c in range(termo, d+r, r):
    print(f'{c}', end='➡ ')
print('ACABOU')
