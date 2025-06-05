import math

Cores = {'White':' \033[0;30;47m',
'Invertido':' \033[7;30;47m',
'Bold':' \033[1;30;47m',
}

n=float(input('Digite um número: '))
print('a parte inteira do número é {}.'.format(math.floor(n)))