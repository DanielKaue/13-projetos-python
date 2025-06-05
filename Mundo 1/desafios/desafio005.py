Cores = {'White':' \033[0;30;47m',
'Invertido':' \033[7;30;47m',
'Bold':' \033[1;30;47m',
}


n1=int(input('Escolha um número: '))
print('Seu número é {}, \n Seu antecessor é {}, \n e seu sucessor é {},'.format(n1,n1-1,n1+1))
