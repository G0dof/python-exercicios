V = float(input('\033[1;30mQual a velocidade do carro?\033[m '))
if V > 80:
    m = 7*(V-80)
    print('\033[1;31mMULTADO! Você excedeu o limite de velocidade que é 80Km/h[m')
    print(f'\033[1;31mVocê deve pagar uma multa de \033[1;33mR${m:.2f}')

print('\033[1;32mTenha um bom dia! Dirija com segurança!\033[m')
