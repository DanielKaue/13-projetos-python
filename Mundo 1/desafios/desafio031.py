Cores = {'White':' \033[0;30;47m',
'Invertido':' \033[7;30;47m',
'Bold':' \033[1;30;47m',
}

d= float(input('Qual a distância em km? '))

if d<=200:
    p1= d*0.50
    print('A viagem custará {:.2f}!'.format(p1))
else:
   p2 = d*0.45
   print('A viagem custará {:.2f}!'.format(p2))