Cores = {'White':' \033[0;30;47m',
'Invertido':' \033[7;30;47m',
'Bold':' \033[1;30;47m',
}


nome= str(input('Qual seu nome?')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))