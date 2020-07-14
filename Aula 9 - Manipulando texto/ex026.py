frase = str(input('Digite uma frase: ')).strip().upper()
print(f'Sua frase contém {frase.count("A")} letras A')
print(f'A primeira letram A está na posição {frase.find("A")+1}')
print(f'A última letra A está na posição {frase.rfind("A")+1}')

