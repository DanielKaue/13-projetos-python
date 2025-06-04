d = float(input('Qual a distância em km? '))

if d<=200:
    p1= d*0.50
    print('A viagem custará {:.2f}!'.format(p1))
else:
   p2 = d*0.45
   print('A viagem custará {:.2f}!'.format(p2))