import random
a1=input('Qual o nome do primeiro aluno? ')
a2=input('E do segundo? ')
a3=input('E do terceiro? ')
a4=input('E do quarto? ')
lista=[a1, a2, a3, a4]
r=random.choice(lista)
print(r)