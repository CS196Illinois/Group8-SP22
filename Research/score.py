#Implementing the Score counter
import pygame
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((800,400))

pygame.display.set_caption("Score Tester")

#pygame setup
# Allows the pygame window to open and close
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            running = False


#Flowers Picked Up
flowers_pickedup = 0

#Score Iteration

# Font & Size (we can change later)
font = pygame.font.Font('freesansbold.ttf', 32)
#Location
textX = 10
textY = 10

#Function for the Score
def show_score(x,y):
    score = font.render("Score:" + str(flowers_pickedup),True,(255,255,255))
    #after it is rendered this shows it on screen
    screen.blit(score, (x, y))

#Actually Showing it
show_score(textX, textY)