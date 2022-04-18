import pygame
from pygame.locals import *

pygame.init()

screen_width = 864
screen_height = 936

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Score')






pygame.quit()

#Display surface


# Everything ^ is just making the window
# Score code :
flowers_pickedup = 0

# Define Font
font = pygame.font.Font('freeansbold.ttf', 32)

# Define Color
white = (255, 255, 255)
blue = (0, 0, 128)
# X and Y
scoreX = 10
scoreY = 10


score = font.render("Score :" + str(flowers_pickedup), True, (white))
screen.blit(score, (scoreX, scoreY))
textRect = score.get_rect()
textRect.center = (scoreX // 2, scoreY // 2)




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




