n = cont = soma = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    soma += n
    if n == 999:
        soma -= 999
        cont -= 1
    cont += 1
print(f'Você digitou {cont} números e a soma entre eles foi {soma}')
