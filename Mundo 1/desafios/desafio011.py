Cores = {'White':' \033[0;30;47m',
'Invertido':' \033[7;30;47m',
'Bold':' \033[1;30;47m',
}


l=int(input('Qual a largura da sua parede? '))
c=int(input('Qual o comprimento da sua parede? '))
a=(l*c)
p=(2*l+2*c)
t=(a/2)
print('O perímetro da sua parede é {:.3f}, a área é {:.3f}, e a quantidade necessária de tinta para pintar será de {:.3f}.'.format(p, a, t))