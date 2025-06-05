Cores = {'White':' \033[0;30;47m',
'Invertido':' \033[7;30;47m',
'Bold':' \033[1;30;47m',
}


n = int(input('Escreva um número INTEIRO: '))

if n % 2 == 0:
    print('Seu número é par!')

else:
    print('Seu número é ímpar!')