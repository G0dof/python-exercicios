m = int(input('\033[1;30mDiga um valor em metros= '))
c = m*100
mi = m*1000
print('\033[33mMetros = {}m \n\033[31mCentímetros= {}cm \n\033[34mMilímetros= {}mm\033[m'.format(m, c, mi))
