a = int(input('Qual o ano? '))

if a % 4 == 0:
    print('O ano {} é bissexto!'.format(a))

else:
    print('O ano {} não é um ano bissexto!'.format(a))