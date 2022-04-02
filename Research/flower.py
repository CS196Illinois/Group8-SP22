# What flower does (General Objectives):
# 1. it has a set size (Saturday) 2. it should appear in a square(Sunday) 3. interate a counter when interacted with(Saturday) 4. location randomized(Sunday)

#Initialized pygame
import pygame

pygame.init()

# Flower Demensions 
screen = pygame.display.set_mode((624, 728))

#Title and Icon
pygame.display.set_caption("Flower Tester")

# Allows the pygame window to open and close
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            running = False

# Interaction Code (Goal: Saturday)


#Locations (Goal: Sunday)
yaxis = 370
xaxis =  480