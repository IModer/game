__author__ = 'Korpa Péter, Tamás Péter'

import pygame
import time
import random

def my_draw(amap):
    y = 0
    for layer in amap.array:
        x = 0
        for tile in layer:
            if tile == 0:
                pygame.draw.rect(display, pygame.Color(0,0,0), pygame.Rect(x,y,10,10))
            if tile == 1:
                pygame.draw.rect(display, pygame.Color(255,255,255), pygame.Rect(x,y,10,10))
            x += 1
        y += 1

class Game_Map:
    def __init__(self,x,y,rnd):    
        
        self.array = []
        self.i = x
        self.j = y
        num = 0
        for i in range(self.i):
            self.array.append([])
            for j in range(self.j):
                if rnd:
                    num = int(random.random()*2)
                self.array[i].append(num)
    
    def sumnbers(self,i,j):
        sum = 0
        if i == 0 or j == 0 or i >= self.i-1 or j >= self.j-1:
            return 0

        for k in [-1,0,1]:
            for n in [-1,0,1]:
                sum += self.array[i+k][j+n]
        return (sum - self.array[i][j])
    
    def settile(self,x,y,k):
        self.array[x][y] = k

#Init
pygame.init()
WINDOW_SIZE = (800,800)
x_by_y = (100,100)
screen = pygame.display.set_mode(WINDOW_SIZE)
display = pygame.Surface(x_by_y)
pygame.display.set_caption("Game of Life")

run = True
#Game loop

mmap = Game_Map(100,100,True)
newmap = Game_Map(100,100,False)
while run:
    time.sleep(1.5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for i in range(len(mmap.array)):
        for j in range(len(mmap.array)):
            if mmap.array[i][j] == 0:
                if mmap.sumnbers(i,j) == 3:
                    newmap.settile(i,j,1)
            else:
                if 2 > mmap.sumnbers(i,j) or 3 < mmap.sumnbers(i,j):
                    newmap.settile(i,j,0)

    mmap.array = newmap.array
    my_draw(newmap)
    screen.blit(pygame.transform.scale(display,WINDOW_SIZE),(0,0))
    pygame.display.update()
pygame.quit()
