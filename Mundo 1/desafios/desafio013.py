Cores = {'White':' \033[0;30;47m',
'Invertido':' \033[7;30;47m',
'Bold':' \033[1;30;47m',
}


s1=float(input('Seu sálario atual é de: '))
ap=float(input('O aumento prometido é de: '))
a=(s1/100)*ap
print('Seu aumento será de {}'.format(a))
v=s1+a
print('Seu novo salário é {:.2f}!'.format(v))