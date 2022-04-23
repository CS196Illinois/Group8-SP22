import pygame
from pygame.locals import *
import math

pygame.init()

screen_width = 400
screen_height = 400

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Score')






pygame.quit()

#Display surface


# Everything ^ is just making the window
# Score code :
flowers_pickedup = 0

# Define Font does not work here but works in score.py 
font = pygame.font.Font('freesansbold.ttf', 32)

# Define Color
white = (255, 255, 255)
blue = (0, 0, 128)
# X and Y
scoreX = 10
scoreY = 10


score = font.render("Score :" + str(flowers_pickedup), True, (white))
screen.blit(score, (scoreX, scoreY))
textRect = score.get_rect()
textRect.center = (200, 200)




run = True
while True:
    screen.fill(blue)
    screen.blit(score, textRect)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()




