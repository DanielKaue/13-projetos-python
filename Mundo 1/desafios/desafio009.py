Cores = {'White':' \033[0;30;47m',
'Invertido':' \033[7;30;47m',
'Bold':' \033[1;30;47m',
}


n=int(input('Escolha um número e descubra sua tabuada: '))
print('{}*1={}, '
'\n {}*2={} , ' 
'\n {}*3={} , ' 
'\n {}*4={} , ' 
'\n {}*5={} , ' 
'\n {}*6={} , ' 
'\n {}*7={} , ' 
'\n {}*8={} , ' 
'\n {}*9={} ,' 
'\n {}*10={} ,'.format(n, n*1, n, n*2, n, n*3, n, n*4, n, n*5, n, n*6, n, n*7, n, n*8, n, n*9, n, n*10))