#Set Up This can display the score when (all this needs is to be put into the main file then just switch score to interaction data )
import pygame
from pygame.locals import *
import math

pygame.init()
 
#Colors for use
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
 
# Assign location
scoreX = 400
scoreY = 400
 
# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((scoreX, scoreY))
 
# Pygame window name
pygame.display.set_caption('Score')
 
# create a font object.
# Remeber: 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
font = pygame.font.Font('freesansbold.ttf', 32)
#score change this when you integrate to maze 
flowers = 0

#Trying out updating methods
for x in range(0, 5):
    flowers = 1 + flowers

# create a text surface object,
text = font.render('Score:' + str(flowers), True, green, blue)
 
# I think you need the rectangle if you want the text to show up without this step it hasn't worked !
# create a rectangular object for the
# text surface object
textRect = text.get_rect()
 
# set the center of the rectangular object.
textRect.center = (200, 200)
 
# Sets up window
while True:
 
    # completely fill the surface object
    # with white color
    display_surface.fill(white)
 
    # copying the text surface object
    # to the display surface object
    # at the center
    display_surface.blit(text, textRect)
 
    for event in pygame.event.get():
 
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT:
 
            # deactivates the pygame library
            pygame.quit()
 
            # quit the program.
            quit()
 
        # Draws the surface object to the screen.
        pygame.display.update()
