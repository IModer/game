__author__ = 'Korpa Péter, Tamás Péter'

import pygame


#Init
pygame.init()
WINDOW_SIZE = (800,800)
x_by_y = (100,100)
screen = pygame.display.set_mode(WINDOW_SIZE)
display = pygame.Surface(x_by_y)
pygame.display.set_caption("Game of Life")

#Pálya

my_game_map = []
for x in range(x_by_y[0]):
    my_game_map.append([])
    for y in range(x_by_y[1]):
        my_game_map[x].append(0)

run = True
#Game loop
while run:
    #Kilépés

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #Pálya betöltése
    y = 0
    for layer in my_game_map:
        x = 0
        for tile in layer:
            if tile == 0:
                pygame.draw.rect(display, pygame.Color(0,0,0), pygame.Rect(x,y,10,10))
            if tile == 1:
                pygame.draw.rect(display, pygame.Color(255,255,255), pygame.Rect(x,y,10,10))
            x += 1
        y += 1

    
 
    screen.blit(pygame.transform.scale(display,WINDOW_SIZE),(0,0))
    pygame.display.update()
pygame.quit()
