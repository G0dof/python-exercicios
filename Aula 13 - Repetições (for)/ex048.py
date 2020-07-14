soma = 0
cont = 0
for c in range(1, 500+1, 2):
    if c % 3 == 0:
        soma = soma + c #ou soma += c
        cont = cont + 1 #ou cont += 1
print(f'A soma de todos os {cont} valores solicitados é {soma}')
