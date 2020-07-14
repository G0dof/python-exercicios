import random
bot = random.randint(0, 10)
cont = 0
jogador = 0
print('\033[1;34mSou seu computador...')
print('\033[30mAcabei de pensar em um número entre 0 a 10.')
print('\033[32mSerá que você consegue adivinhar qual foi? ')
while jogador != bot:
    cont += 1
    jogador = int(input('\033[33mQual o seu palpite? '))
    if jogador > 10:
        print('\033[31;40mTente Novamente\033[m')
    else:
        if jogador > bot:
            print('\033[1;31mMenos... Tente novamente')
        else:
            if jogador < bot:
                print('\033[35mMais... Tente novamente')
if cont == 1:
    print('\033[32mCAGOUUUUUU!!!!!!!')
elif cont <= 5:
    print('\033[36mTu é foda mano. Parabéns!')
elif cont > 5:
    print('\033[31mVocê é fraco, lhe falta sorte.')
print(f'\033[30mAcertou com \033[33m{cont} \033[30mtentativas.\033[m')
