import math

Cores = {'White':' \033[0;30;47m',
'Invertido':' \033[7;30;47m',
'Bold':' \033[1;30;47m',
}

co=float(input('Qual o comprimento do cateto oposto? '))
ca=float(input('Qual o comprimento do cateto adjacente? '))
hi = math.hypot(co, ca)
print('A hipotenusa é: {:.3f}.'.format(hi))