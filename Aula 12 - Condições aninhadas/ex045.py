from time import sleep
import random
print('''\033[1;33mSuas opções:
\033[31m[ 0 ] \033[30mPEDRA
\033[34m[ 1 ] \033[30mPAPEL
\033[36m[ 2 ] \033[30mTESOURA''')
a = 'PEDRA'
b = 'PAPEL'
c = 'TESOURA'
lista = [a, b, c]
computador = random.choice(lista)
play = int(input('\033[37mQual é a sua jogada? '))
if play <= 2:
    print('\033[35mJO')
    sleep(1)
    print('\033[32mKEN')
    sleep(1)
    print('\033[34mPO')
    print('\033[33m=-' * 12)
    print(f'\033[31mComputador jogou {computador}')
    print('\033[34mJogador jogou', end=' ')
    if play == 0:
        print('PEDRA')
    elif play == 1:
        print('PAPEL')
    elif play == 2:
        print('TESOURA')
    print('\033[33m=-' * 12)
    if play == 0 and computador == b:
        print('\033[31mCOMPUTADOR GANHOU')
    elif play == 1 and computador == a:
        print('\033[34mJOGADOR GANHOU')
    elif play == 2 and computador == a:
        print('\033[31mCOMPUTADOR GANHOU')
    elif play == 0 and computador == c:
        print('\033[34mJOGADOR GANHOU')
    elif play == 1 and computador == c:
        print('\033[31mCOMPUTADOR GANHOU')
    elif play == 2 and computador == b:
        print('\033[34mJOGADOR GANHOU')
    elif play == 0 or 1 or 2 == computador:
        print('\033[30mEMPATE')
else:
    print('\033[31mTente novamente\033[m')