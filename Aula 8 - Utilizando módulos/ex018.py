import math
A = float(input("Digite o ângulo: "))
rad = (math.radians(A))
sen = (math.sin(rad))
cos = (math.cos(rad))
tan = (math.tan(rad))
print('O ângulo de {} tem o SENO de {:.2f}'.format(A, sen))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(A, cos))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(A, tan))
