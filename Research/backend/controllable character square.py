import pygame
from pygame.locals import *
import sys
import random

pygame.init()

colorWHITE = (255,255,255)
colorBLACK = (0, 0, 0)
colorRED = (255, 0, 0)

# window dimensions
gameWindow = pygame.display.set_mode((500,500))

pygame.display.set_caption('animated character template')

gameQuit = False
# starting position on maze, use rand import here
move_x = 300
move_y = 300

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
                move_x -= 60
            if event.key == pygame.K_RIGHT:
                move_x += 60
            if event.key == pygame.K_UP:
                move_y -= 60
            if event.key == pygame.K_DOWN:
                move_y += 60

    # make window white
    gameWindow.fill(colorWHITE)

    # make black rectangle object
    pygame.draw.rect(gameWindow, colorBLACK, [move_x, move_y, 50, 50])

    pygame.display.update()            