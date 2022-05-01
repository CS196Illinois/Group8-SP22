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






        
    while len(fl_set) < fl_num:
        # add first flower
        coord_fl = ((50 * random.randint(0, rows - 1)) + 15, (50 * random.randint(0, cols - 1)) + 15)
        if coord_fl not in fl_set and coord_fl != (15, 15):
            fl_set.append(coord_fl)

stack = []

class Cell():
    def __init__(self,x,y):
        global width
        self.x = x * width
        self.y = y * width
        # rand select floor texture in class
        self.floor_texture = random.randint(0, 5)
        
        self.visited = False
        self.current = False
        
        self.walls = [True,True,True,True] # top , right , bottom , left
        
        # neighbors
        self.neighbors = []
        
        self.top = 0
        self.right = 0
        self.bottom = 0
        self.left = 0
        
        self.next_cell = 0
    
    def draw(self):
        if self.visited:
            #pygame.draw.rect(screen,colorBG,(self.x,self.y,width,width))
            screen.blit(bg_set[self.floor_texture], (self.x, self.y))
            if self.walls[0]:
                pygame.draw.line(screen,wall_color,(self.x,self.y),((self.x + width),self.y),wall_thickness) # top
            if self.walls[1]:
                pygame.draw.line(screen,wall_color,((self.x + width),self.y),((self.x + width),(self.y + width)),wall_thickness) # right
            if self.walls[2]:
                pygame.draw.line(screen,wall_color,((self.x + width),(self.y + width)),(self.x,(self.y + width)),wall_thickness) # bottom
            if self.walls[3]:
                pygame.draw.line(screen,wall_color,(self.x,(self.y + width)),(self.x,self.y),wall_thickness) # left
    
    def checkNeighbors(self):
        #print("Top; y: " + str(int(self.y / width)) + ", y - 1: " + str(int(self.y / width) - 1))
        if int(self.y / width) - 1 >= 0:
            self.top = grid[int(self.y / width) - 1][int(self.x / width)]
        #print("Right; x: " + str(int(self.x / width)) + ", x + 1: " + str(int(self.x / width) + 1))
        if int(self.x / width) + 1 <= cols - 1:
            self.right = grid[int(self.y / width)][int(self.x / width) + 1]
        #print("Bottom; y: " + str(int(self.y / width)) + ", y + 1: " + str(int(self.y / width) + 1))
        if int(self.y / width) + 1 <= rows - 1:
            self.bottom = grid[int(self.y / width) + 1][int(self.x / width)]
        #print("Left; x: " + str(int(self.x / width)) + ", x - 1: " + str(int(self.x / width) - 1))
        if int(self.x / width) - 1 >= 0:
            self.left = grid[int(self.y / width)][int(self.x / width) - 1]
        #print("--------------------")
        
        if self.top != 0:
            if self.top.visited == False:
                self.neighbors.append(self.top)
        if self.right != 0:
            if self.right.visited == False:
                self.neighbors.append(self.right)
        if self.bottom != 0:
            if self.bottom.visited == False:
                self.neighbors.append(self.bottom)
        if self.left != 0:
            if self.left.visited == False:
                self.neighbors.append(self.left)
        
        if len(self.neighbors) > 0:
            self.next_cell = self.neighbors[random.randrange(0,len(self.neighbors))]
            return self.next_cell
        else:
            return False

def removeWalls(current_cell,next_cell):
    x = int(current_cell.x / width) - int(next_cell.x / width)
    y = int(current_cell.y / width) - int(next_cell.y / width)
    if x == -1: # right of current
        current_cell.walls[1] = False
        next_cell.walls[3] = False
    elif x == 1: # left of current
        current_cell.walls[3] = False
        next_cell.walls[1] = False
    elif y == -1: # bottom of current
        current_cell.walls[2] = False
        next_cell.walls[0] = False
    elif y == 1: # top of current
        current_cell.walls[0] = False
        next_cell.walls[2] = False

grid = []

for y in range(rows):
    grid.append([])
    for x in range(cols):
        grid[y].append(Cell(x,y))

current_cell = grid[0][0]
next_cell = 0

# -------- Maze Generator Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
            sys.exit()
    
    current_cell.visited = True
    current_cell.current = True
    
    for y in range(rows):
        for x in range(cols):
            grid[y][x].draw()
    
    next_cell = current_cell.checkNeighbors()
    
    if next_cell != False:
        current_cell.neighbors = []
        
        stack.append(current_cell)
        
        removeWalls(current_cell,next_cell)
        
        current_cell.current = False
        
        current_cell = next_cell
    
    elif len(stack) > 0:
        current_cell.current = False
        current_cell = stack.pop()
        
    elif len(stack) == 0:
        #print("FULL")
        done = True
        
        for y in range(rows):
            grid.append([])
            for x in range(cols):
                grid[y].append(Cell(x,y))
        
        current_cell = grid[0][0]
        next_cell = 0

    pygame.display.flip()

