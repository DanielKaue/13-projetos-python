Cores = {'White':' \033[0;30;47m',
'Invertido':' \033[7;30;47m',
'Bold':' \033[1;30;47m',
}


d = int(input('quantos dias alugados: '))
k = float(input('quantos kilometros foram rodados: '))
v = (60*d)+(0.15*k)
print('O valor será de R${:.2f}'.format(v))