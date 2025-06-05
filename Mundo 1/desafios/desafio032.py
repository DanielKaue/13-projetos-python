Cores = {'White':' \033[0;30;47m',
'Invertido':' \033[7;30;47m',
'Bold':' \033[1;30;47m',
}


a = int(input('Qual o ano? '))

if a % 4 == 0:
    print('O ano {} é bissexto!'.format(a))

else:
    print('O ano {} não é um ano bissexto!'.format(a))