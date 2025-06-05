from math import sqrt
from math import ceil
n=int(input('digite um numero: '))
r=sqrt(n)
print('A raiz de {} é igual a {} (arredondando para cima).'.format(n, ceil(r)))