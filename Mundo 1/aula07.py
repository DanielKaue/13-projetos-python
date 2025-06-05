n1=int(input('um valor:'))
n2=int(input('outro valor:'))
s=n1+n2
m=n1*n2
d=n1/n2
e=n1**n2
di=n1//n2
re=n1%n2
su=n1-n2
print('A soma resulta em {}, \nA multiplicação resulta em {}, \nA Divisão resulta em {:.3f}, \nA potenciação resulta em {}, \nA soma parte inteira da divisão é {}, \nO resto da divisão é {}, \nA subtração resulta em {}.'.format(s, m, d, e, di, re, su))