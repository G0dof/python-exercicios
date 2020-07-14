n = 0
cont = 1
while True:
    print('-' * 35)
    n = int(input('Qual valor você deseja ver na tabuada? '))
    print('-'*35)
    if n <= 0:
        break
    for c in range(1, 11):
        mult = n*c
        print(f'{n} x {c} = {mult}')
print('TABUADA ENCERRADA. Volte sempre!')
