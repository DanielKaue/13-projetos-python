p=float(input('Qual o preço desse produto? '))
d=float(input('Quanto de desconto deseja saber? '))
v1=(p/100)*d
v2=p-v1
print('Com {}% de desconto, o valor será de {:.2f} '.format(d, v2))
