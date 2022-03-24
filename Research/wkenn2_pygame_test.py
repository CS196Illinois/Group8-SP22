import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('This is the Caption')
clock = pygame.time.Clock() # framerate stuff
testFont = pygame.font.Font('Group8-SP22/Research/Test_Files/Test_Font.ttf', 30) # (font type, font size)

#testSurface = pygame.Surface((100,100))
#testSurface.fill('purple')

testSurface = pygame.image.load('Group8-SP22/Research/Test_Files/Small_Mario.png').convert_alpha()
groundSurface = pygame.image.load('Group8-SP22/Research/Test_Files/Ground.png').convert_alpha()

score = str(0)
textSurface = testFont.render('Score: ' + score, True, 'Black') # (text, AA, color)
textRect = textSurface.get_rect(center = (400, 30))

enemySurface = pygame.image.load('Group8-Sp22/Research/Test_Files/Non_Copyright_Enemy.png').convert_alpha()
enemyXPos = 700
enemyRect = enemySurface.get_rect(midbottom = (700, 325))

playerSurface = pygame.image.load('Group8-SP22/Research/Test_Files/Mario_Running.png').convert_alpha()
playerRect = playerSurface.get_rect(midbottom = (100, 325))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
#       if event.type == pygame.MOUSEMOTION:
#           if playerRect.collidepoint(event.pos):
#               print('MOUSEOVER MARIO')

    screen.blit(testSurface,(0,0)) #puts the surface on the display
    screen.blit(groundSurface,(0,325))
    screen.blit(textSurface,(350, 50))

    enemyRect.x -= 4
    if enemyRect.right < 0:
        enemyRect.left = 800
    screen.blit(enemySurface, enemyRect)

    screen.blit(playerSurface, playerRect)

#    pygame.draw.line(screen, "Black", (0,0), (pygame.mouse.get_pos()), 5)

    #if playerRect.colliderect(enemyRect): #returns 0 (no collison) or 1 (collision)
        #print("COLLIDE")

    pygame.display.update() # makes it so we can see what we draw 
                            # on the screen
    clock.tick(60)  # telling the while true loop that this should
                    # not run more than 60 times per second