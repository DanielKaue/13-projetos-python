v = float(input('Qual a velocidade do seu carro agora? (Em km): '))

if v>80:
    e= v-80
    p= e*7
    print('Você será multado!')
    print('A multa custará {:.02f}!'.format(p))

else:
    print('Continue assim motorista!')