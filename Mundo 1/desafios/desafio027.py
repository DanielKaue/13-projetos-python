Cores = {'White':' \033[0;30;47m',
'Invertido':' \033[7;30;47m',
'Bold':' \033[1;30;47m',
}


n=str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('E seu último é {}'.format(nome[len(nome)-1]))
