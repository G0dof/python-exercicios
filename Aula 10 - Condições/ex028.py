import random
from time import sleep
c = random.randint(0, 5)
print('\033[1;33m-=-' * 20)
print('\033[1;34mVou pensar em um número entre 0 a 5. Tente adivinhar...')
print('\033[1;33m-=-' * 20)
eu = int(input('\033[1;30mEm que número eu pensei?: '))
print('\033[1;35mPROCESSANDO...\033[m')
sleep(1)
if eu == c:
    print('\033[1;32mBOA PORRA, ACERTOU!!!\033[m')
else:
    print('\033[1;31mERRRO, SEU INÚTIL!!!\033[m')
print(f'\033[1;4;37mO número era {c}')
