print('==Analisador de triângulos==')

r1 = float(input('Qual o comprimento do primeira segmento? '))
r2 = float(input('E do segunda? '))
r3 = float(input('E do terceira?'))

if r1<r2+r3 and  r2<r1+r3 and r3<r1+r2:
    print('Um triângulo pode ser feito!')

else:
    print('Um triângulo não pode ser feito...')