Cores = {'White':' \033[0;30;47m',
'Invertido':' \033[7;30;47m',
'Bold':' \033[1;30;47m',
}


n1=int(input('Escolha um número: '))
print('O dobro do seu número é {}, o triplo é {}, e a raiz quadrada é {}!'.format(n1*2, n1*3, n1**(1/2)))