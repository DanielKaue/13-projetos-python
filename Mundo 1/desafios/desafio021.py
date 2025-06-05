import pygame

Cores = {'White':' \033[0;30;47m',
'Invertido':' \033[7;30;47m',
'Bold':' \033[1;30;47m',
}

pygame.mixer.music.load('Nome do arquivo')
pygame.mixer.music.play()
pygame.event.wait