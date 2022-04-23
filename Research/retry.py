#testing for implementing a retry option
#set ups
import pygame
from pygame.locals import *

pygame.init()

screen_width = 864
screen_height = 936
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Retry Tests')


#So general goal is to have button that when interacted with will restart the game
#So this should be the image of the button
button_img = pygame.image.load('')



#Making a class
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    #drawing it
    def draw(self):
        #get mouse position
        pos = pygame.mouse.get_pos()
        action = False
        #check if mouse is over the button
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True:
        #draw button
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action

#create restart button instance
button = Button(screen_width // 2 - 50, screen_height//2 - 100, button_img)


#function to reset game
def reset_game():
    #put variables here

#check for game over and reset
if game_over == True:
    if button.draw() == True:
        game_over == False
        reset_game()
