import emoji

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2

if (m<7):
    print('Você reprovou, que pena!😬')

else:
    print('Você passou! parabéns pela nota {:.1f}!🤩🤩🤩'.format(m))

if (m==10):
    print('Que notão! aprendeu com quem? Alberto Eistênio? 😅!')