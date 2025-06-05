Cores = {'White':' \033[0;30;47m',
'Invertido':' \033[7;30;47m',
'Bold':' \033[1;30;47m',
}


nome = str(input('Digite uma frase: ')).strip()
print('A letra A aparece {} vezes na frase {}'.format(nome.upper().count('A'),nome))
print('A primeira letra A aparece pela na posição {}'.format(nome.upper().find('A')+1))
print( 'A última letra A apareceu na posição {}'.format(nome.upper().rfind('A')+1))