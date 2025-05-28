s1=float(input('Seu sálario atual é de: '))
ap=float(input('O aumento prometido é de: '))
a=(s1/100)*ap
print('Seu aumento será de {}'.format(a))
v=s1+a
print('Seu novo salário é {:.2f}!'.format(v))