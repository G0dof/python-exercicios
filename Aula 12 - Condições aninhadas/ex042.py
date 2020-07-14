a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento :'))
c = float(input('Terceiro segmento: '))
if a+b > c and b+c > a and c+a > b:
    if a != b != c:
        print('Os segmentos SE JUNTAM e formam um triângulo ESCALENO')
    if a == b == c:
        print('Os segmentos SE JUNTAM e formam um triângulo EQUILÁTERO')
    if b or a == b or a != c:
        print('Os segmentos SE JUNTAM e formam um triângulo ISÓSCELES')
else:
    print('Os segmentos NÃO SE JUNTAM')
