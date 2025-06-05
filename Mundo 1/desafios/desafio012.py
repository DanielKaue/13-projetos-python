Cores = {'White':' \033[0;30;47m',
'Invertido':' \033[7;30;47m',
'Bold':' \033[1;30;47m',
}


p=float(input('Qual o preço desse produto? '))
d=float(input('Quanto de desconto deseja saber? '))
v1=(p/100)*d
v2=p-v1
print('Com {}% de desconto, o valor será de {:.2f} '.format(d, v2))
