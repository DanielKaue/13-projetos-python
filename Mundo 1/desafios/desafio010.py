Cores = {'White':' \033[0;30;47m',
'Invertido':' \033[7;30;47m',
'Bold':' \033[1;30;47m',
}


r=int(input(('quantos reais você tem na sua carteira: ')))
d = round(r / 3.27, 2)
print('você tem aproximadamente {} em doláres.'.format(d))