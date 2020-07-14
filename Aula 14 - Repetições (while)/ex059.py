from time import sleep
n1 = int(input('\033[1;33mPrimeiro valor: '))
n2 = int(input('\033[32mSegundo valor: '))
opção = 0
while opção != 5:
    print('''    \033[30m[1] \033[31mSomar 
    \033[30m[2] \033[33mMultiplicar 
    \033[30m[3] \033[34mMaior
    \033[30m[4] \033[35mNovos Números
    \033[30m[5] \033[36mSair do programa''')
    opção = int(input('\033[33m>>>> \033[30mQual é a sua opção? '))
    if opção == 1:
        soma = n1+n2
        print(f'\033[31mA soma entre {n1} + {n2} é {soma}')
    elif opção == 2:
        mult = n1*n2
        print(f'\033[33mA multiplicação entre {n1} x {n2} é {mult}')
    elif opção == 3:
        lista = [n1, n2]
        maior = max(lista)
        print(f'\033[34mEntre {n1} e {n2} o maior é {maior}')
    elif opção == 4:
        print('\033[35mInforme os números novamente:')
        n1 = int(input('\033[33mPrimeiro valor: '))
        n2 = int(input('\033[32mSegundo valor: '))
    elif opção == 5:
        print('\033[36mFinalizando...')
        sleep(2)
    else:
        print('\033[31mCOMANDO INVÁLIDO, TENTE NOVAMENTE!')
    print('\033[30m=-' * 20)
print('Fim do programa! Volte sempre!\033[m')
