n = (int(input('\033[1;30mDigite um valor= ')))
x2 = n * 2
x3 = n * 3
r = n ** (1 / 2)
print('\033[33mNúmero= {} \n\033[31mDobro= {} \n\033[32mTriplo= {} \n\033[34mRaiz Quadrada= {:.2f}\033[m'.format(n, x2,
                                                                                                                 x3, r))
