 # generate diamond-like illumination using manhattan distance based on location of mc
# prelim

import pygame
from pygame.locals import *
import sys
import random

pygame.init()

colorWHITE = (255,255,255)
colorBLACK = (0, 0, 0)
colorGRAY = (121, 121, 121)

size = (701,701)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Maze base")

gameQuit = False

width = 50

# starting position on maze, top left square is: padding + 0.5 * (block len - character len)
move_x = 109
move_y = 109

location = (move_x, move_y)

# game loop

while not gameQuit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameQuit = True
            pygame.quit()
            sys.exit()

            # player press q or press esq = quit event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        # movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_x -= 52
            if event.key == pygame.K_RIGHT:
                move_x += 52
            if event.key == pygame.K_UP:
                move_y -= 52
            if event.key == pygame.K_DOWN:
                move_y += 52

    # check and update location of mc:


    # create a black square for every cell on the board except at a certain cell

    screen.fill(colorWHITE)

    for x in range(0, size[0]//width):
        for y in range(0, size[1]//width):
            loc_dark100 = ()
            rect = pygame.Rect(x * 52, y * 52, 51, 51)
            pygame.draw.rect(screen, colorBLACK, rect)

    pygame.display.update()