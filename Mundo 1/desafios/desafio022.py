Cores = {'White':' \033[0;30;47m',
'Invertido':' \033[7;30;47m',
'Bold':' \033[1;30;47m',
}


nome=str(input('Qual o seu nome?')).strip()
print('O seu nome em maisculo é {}'.format(nome.upper()))
print('O seu nome em minusculo é {}'.format(nome.lower()))
print('Su nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
lista=nome.split()
print('Seu primeiro nome é {}, e possui {} letras'.format(lista[0],len(lista[0])))
