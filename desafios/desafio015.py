d = int(input('quantos dias alugados: '))
k = float(input('quantos kilometros foram rodados: '))
v = (60*d)+(0.15*k)
print('O valor será de R${:.2f}'.format(v))