 # generate diamond-like illumination using manhattan distance based on location of mc
# prelim

import math
import pygame
from pygame.locals import *
import sys
import random

pygame.init()

colorWHITE = (255,255,255)
colorBLACK = (0, 0, 0)
colorGRAY = (121, 121, 121)
colorBLACK2 = (0, 0, 0)
colorBLACK1 = (0, 0, 0)
colorBLACK0 = (0, 0, 0)


maze_dim = (7, 7)
cell = 52
width = 50
size = (maze_dim[0] * cell, maze_dim[1] * cell)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("lighting")

gameQuit = False

# starting position on maze, top left square is: padding + 0.5 * (block len - character len)
move_x = 2
move_y = 2

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
        loc_mc = (move_x//52, move_y//52)

    # create a black square for every cell on the board except at a certain cell

    screen.fill(colorWHITE)

    cell_loc = []

    # populate coordinates in separate loop
    
    for x in range(0, size[0]//width):
        for y in range(0, size[1]//width):
            cell_loc.append((x,y))

    # print(cell_loc)

    # draw rectangles

    for item in cell_loc:
        x = item[0]
        y = item[1]
        dx = abs(loc_mc[0]-x)
        dy = abs(loc_mc[1]-y)
        distance = math.sqrt(dx*dx + dy*dy)
        opacity = int((255.0 * (distance) / 3))
        if (opacity > 255):
            opacity = 255
        color = (0, 0, 0)
        rect = pygame.Surface((51, 51))
        rect.set_alpha(opacity)
        rect.fill(color)
        screen.blit(rect, (x * 52,y * 52))

        # alt method: manhattan lighting

        # if distance > 2.0:
        #     rect = pygame.Surface((51, 51))
        #     rect.set_alpha(255)
        #     rect.fill(color)
        #     screen.blit(rect, (x * 52,y * 52))
        # if distance == 2:
        #     rect = pygame.Surface((51, 51))
        #     rect.set_alpha(170)
        #     rect.fill(color)
        #     screen.blit(rect, (x * 52,y * 52))
        # if distance == 1:
        #     rect = pygame.Surface((51, 51))
        #     rect.set_alpha(85)
        #     rect.fill(color)
        #     screen.blit(rect, (x * 52,y * 52))
        # if distance == 0:
        #     rect = pygame.Surface((51, 51))
        #     rect.set_alpha(0)
        #     rect.fill(color)
        #     screen.blit(rect, (x * 52,y * 52))

    # make MC
    # pygame.draw.rect(screen, colorGRAY, [move_x, move_y, 40, 40])

    pygame.display.update()