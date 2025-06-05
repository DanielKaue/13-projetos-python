Cores = {'White':' \033[0;30;47m',
'Invertido':' \033[7;30;47m',
'Bold':' \033[1;30;47m',
}


n1 = float(input('Qual o primeiro número? '))
n2 = float(input('E o segundo? '))
n3 = float(input('E o terceiro? '))

menor = n1
maior = n2

#Verificando quem é menor
if n2<n1 and n2<n3:
    menor=n2
if n3<n1 and n3<n2:
    menor = n3
#Verificando quem é menor

#verificando o maior
if n1>n2 and n1>n3:
    maior = n1

if n3>n2 and n3>n1:
    maior = n3
#verificando o maior

print('O maior é {} e o menor é {}.'.format(maior, menor))