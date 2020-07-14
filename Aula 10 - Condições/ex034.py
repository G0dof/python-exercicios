s = float(input('Digite o valor do seu sálario: '))
if s >= 1250:
    print(f'Com o aumento seu salário será {s * 10 / 100 + s:.2f}')
else:
    print(f'Com o aumento seu salário será {s * 15 / 100 + s:.2f}')
