nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média = (nota1+nota2)/2
print(f'Sua média é {média:.1f}')
if média >= 6:
    print('O aluno está APROVADO.')
elif 6 > média >= 5:
    print('O aluno está em RECUPERAÇÃO')
else:
    print('O aluno está REPROVADO')
