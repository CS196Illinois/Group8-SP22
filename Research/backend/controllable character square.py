import pygame
from pygame.locals import *
import sys
import random

pygame.init()

colorWHITE = (255,255,255)
colorBLACK = (0, 0, 0)
colorGRAY = (121, 121, 121)

# window dimensions
# formula x dimension: block size * number of blocks + gap size * (# of blocks + 1) + symmetrical padding of even # * blocks
gameWindow = pygame.display.set_mode((624,728))

pygame.display.set_caption('animated character template')

gameQuit = False
# starting position on maze, top left square is: padding + 0.5 * (block len - character len)
move_x = 109
move_y = 109

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

    # make window white
    gameWindow.fill(colorBLACK)
    for y in range(2, 12):
        for x in range(2, 10):
            rect = pygame.Rect(x * 52, y * 52, 50, 50)
            pygame.draw.rect(gameWindow, colorWHITE, rect)

    # make black rectangle object
    pygame.draw.rect(gameWindow, colorGRAY, [move_x, move_y, 40, 40])

    pygame.display.update()            