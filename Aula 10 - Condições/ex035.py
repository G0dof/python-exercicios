print('\033[1;33m-=' * 20)
print('\033[1;30mANALISADOR DE TRIÂNGULOS')
print('\033[1;33m-=' * 20)
a = float(input('\033[1;31mPrimeira reta: '))
b = float(input('\033[1;36mSegunda reta: '))
c = float(input('\033[1;32mTerceira reta:\033[m '))
if a+b > c and b+c > a and c+a > b:
    print('As retas \033[1;33mSE JUNTAM\033[m')
else:
    print('As retas \033[1;31mNÃO SE JUNTAM\033[m')
