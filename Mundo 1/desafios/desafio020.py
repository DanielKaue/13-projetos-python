import random

Cores = {'White':' \033[0;30;47m',
'Invertido':' \033[7;30;47m',
'Bold':' \033[1;30;47m',
}

a1=input('Qual o nome do primeiro aluno? ')
a2=input('E do segundo? ')
a3=input('E do terceiro? ')
a4=input('E do quarto? ')
lista=[a1, a2, a3, a4]
random.shuffle(lista)
print('1º- {}, \n2º- {}, \n3º- {}, \n4º- {}, '.format(lista[0], lista[1], lista[2], lista[3] ))
