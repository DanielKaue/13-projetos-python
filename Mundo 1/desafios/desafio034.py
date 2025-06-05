Cores = {'White':' \033[0;30;47m',
'Invertido':' \033[7;30;47m',
'Bold':' \033[1;30;47m',
}


s = float(input('Qual o seu sálario? '))

if s>1250:
    print('O seu aumento será de 10%!')
    a1= (s/100)*10
    sf1= a1+s
    print('Seu novo sálario é {:.02f}!'.format(sf1))

else:
    print('O seu aumento será de 15%!')
    a2= (s/100)*15
    sf2= a2+s
    print('Seu novo sálario é {:0.2f}!'.format(sf2))