import random
import emoji

n = random.randint(0, 5)

v=int(input('Tente adivinhar que número estou pensando! Dica: Ele está entre 0 a 5!😏: '))

if v == n:
    print('Você acertou! 🫡🥳')

else:
    print('Errou!😜, tente novamente!')

print('O número será alterado, mas pode se manter como esse! é aleatório!😝')