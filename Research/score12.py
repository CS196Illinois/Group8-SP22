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












# ------------------------------------------------------------------------------------------------------------
#score implementation !!
#Colors for use
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
 
# Assign location
scoreX = 3
scoreY = 3
 
# create the display surface object
# of specific dimension..e(X, Y).
#use the variable screen
 
 
# create a font object.
# Remeber: 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
font = pygame.font.Font('freesansbold.ttf', 12)


def show_score(newX, newY):
    score = font.render("Score: " + str(flowers), True, blue)
    screen.blit(score, (newX, newY))
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

#-----------------------------------------------------------------------------------------------
#retry button







