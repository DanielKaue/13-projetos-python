Cores = {'White':' \033[0;30;47m',
'Invertido':' \033[7;30;47m',
'Bold':' \033[1;30;47m',
}


m=int(input('coloque uma metragem: '))
print('Em centimetros resulta em {}, e em milimetros resulta em {}.'.format(m*100, m*1000))