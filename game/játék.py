__author__ = 'Korpa Péter, Tamás Péter'

import pygame
import time
import random


def my_draw(amap):
    y = 0
    for layer in amap.array:
        x = 0
        for x, tile in enumerate(layer):
            if tile == 0:
                pygame.draw.rect(display, pygame.Color(
                    0, 0, 0), pygame.Rect(x, y, 10, 10))
            if tile == 1:
                pygame.draw.rect(display, pygame.Color(
                    255, 255, 255), pygame.Rect(x, y, 10, 10))
        y += 1

class Game_Map:
    def __init__(self, x, y, rnd):
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

    def sumnbers(self, i, j):
        sum = 0
        for k in [-1, 0, 1]:
            for n in [-1, 0, 1]:
                sum += self.array[(i+k+self.i) % self.i][(j+n+self.j) % self.j]
        return sum - self.array[i][j]

    def settile(self, x, y, k):
        self.array[x][y] = k


# Init
pygame.init()
WINDOW_SIZE = (800, 800)
x_by_y = (100, 100)
screen = pygame.display.set_mode(WINDOW_SIZE)
display = pygame.Surface(x_by_y)
pygame.display.set_caption("Game of Life")

run = True
# Game loop

mmap = Game_Map(100, 100, False)
newmap = Game_Map(100, 100, False)
while run:
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for i in range(len(mmap.array)):
        for j in range(len(mmap.array)):
            if mmap.array[i][j] == 0:
                if mmap.sumnbers(i, j) == 3:
                    newmap.settile(i, j, 1)
            else:
                if 2 > mmap.sumnbers(i, j) or 3 < mmap.sumnbers(i, j):
                    newmap.settile(i, j, 0)

    my_draw(newmap)
    mmap.array = newmap.array
    screen.blit(pygame.transform.scale(display, WINDOW_SIZE), (0, 0))
    pygame.display.update()
pygame.quit()
