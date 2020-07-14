from random import randint
cont = 0
computador = randint(1, 10)
n = 0
jogador = 'P'
print('\033[1;33m=-'*15)
print('\033[30mVAMOS JOGAR PAR OU ÍMPAR')
print('\033[33m=-'*15)
while True:
    n = int(input('\033[34mDiga um valor: '))
    jogador = input('Par ou Ímpar? \033[30m[P/I]\033[34m: ').upper().strip()
    soma = computador+n
    tipo = ' '
    print('\033[1;33m-'*45)
    print(f'\033[30mVocê jogou {n} e o computador {computador}. Total de {soma}', end=' ')
    if (soma%2) == 0:
        print('\033[32mDEU PAR')
    else:
        print('\033[31mDEU íMPAR')
    print('\033[1;33m-'*45)
    if (soma%2) == 0 and jogador in 'Pp':
        print('\033[32mVocê VENCEU!')
        cont += 1
    elif (soma%2) != 0 and jogador in 'Ii':
        print('\033[32mVocê VENCEU!')
        cont += 1
    else:
        print('\033[31mVocê PERDEU!')
        break
    print('\033[30mVamos jogar novamente...')
print('\033[1;33m=-'*15)
print(f'\033[31mGAME OVER! Você venceu \033[36m{cont} \033[31mvezes.')