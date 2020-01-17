import pygame
pygame.init()
pygame.display.set_mode((800,800))
pygame.display.set_caption('Boti a mester')
screen = pygame.image.load('H.png')
boti = pygame.image.load('boti.png')
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = false
    pygame.display.update()

pygame.quit()