Cores = {'White':' \033[m',
'Invertido':' \033[7;30;47m',
'Bold':' \033[1;30;47m',
}

Primeiro=float(input('primeiro número'))
Segundo=float(input('segundo número'))
s=Primeiro+Segundo
print('A soma entre {}{}{}, E {}{}{},, resultará em {}{}{},'.format(Cores['Bold'],Primeiro,Cores['White'],Cores['Bold'] ,Segundo, Cores['White'], Cores['Invertido'], s, Cores['White'
                                                                                                                                                                               ]))
