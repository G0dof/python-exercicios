v = int(input('\033[1;32mValor da casa: \033[33mR$'))
s = int(input('\033[35mSalário do comprador: \033[33mR$'))
a = int(input('\033[36mQuantos anos de financiamento? \033[m'))
pm = v/(12*a)
p = s*0.3
print(f'\033[30mPara pagar uma casa de R${v} em {a} anos, a prestação será de R${pm}\033[m')
if pm <= p:
    print('\033[1;34mEMPRÉSTIMO ACEITO\033[m')
else:
    print('\033[1;31mEMPRÉSTIMO NEGADO\033[m')
