n1 = int(input('\033[1;33mPrimeiro valor: '))
n2 = int(input('\033[1;36mSegundo Valor: '))
n3 = int(input('\033[1;32mTerceiro valor:\033[m '))
#MENOR
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
#MAIOR
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'\033[1;34mO maior número é {maior}')
print(f'\033[1;31mO menor número é {menor}\033[m')

