import math
co=float(input('Qual o comprimento do cateto oposto? '))
ca=float(input('Qual o comprimento do cateto adjacente? '))
hi = math.sqrt(co**2 + ca**2)
print('A hipotenusa é: {:.3f}.'.format(hi))