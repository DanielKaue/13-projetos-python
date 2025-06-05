import random
import emoji

Cores = {'White':' \033[0;30;47m',
'Invertido':' \033[7;30;47m',
'Bold':' \033[1;30;47m',
}

n = random.randint(0, 5)

v=int(input('Tente adivinhar que número estou pensando! Dica: Ele está entre 0 a 5!😏: '))

if v == n:
    print('Você acertou! 🫡🥳')

else:
    print('Errou!😜, tente novamente!')

print('O número será alterado, mas pode se manter como esse! é aleatório!😝')