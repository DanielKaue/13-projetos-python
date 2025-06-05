Cores = {'White':' \033[0;30;47m',
'Invertido':' \033[7;30;47m',
'Bold':' \033[1;30;47m',
}


c=float(input('Coloque um valor em graus ºC: '))
f=9*c/5+32
print('A temperatura {}ºC corresponde á {}ºF'.format(c, f))