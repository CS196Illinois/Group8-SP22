from operator import truediv
import random
import pygame
import sys
pygame.init()

WHITE = (255,255,255)
GREY = (20,20,20)
BLACK = (0,0,0)
PURPLE = (100,0,100)
RED = (255,0,0)

size = (701,701)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Maze Generator")

done = False

clock = pygame.time.Clock()

width = 50
cols = int(size[0] / width)
rows = int(size[1] / width)

stack = []

class Cell():
    def __init__(self,x,y):
        global width
        self.x = x * width
        self.y = y * width
        
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
            pygame.draw.rect(screen,WHITE,(self.x,self.y,width,width))
        
            if self.walls[0]:
                pygame.draw.line(screen,BLACK,(self.x,self.y),((self.x + width),self.y),1) # top
            if self.walls[1]:
                pygame.draw.line(screen,BLACK,((self.x + width),self.y),((self.x + width),(self.y + width)),1) # right
            if self.walls[2]:
                pygame.draw.line(screen,BLACK,((self.x + width),(self.y + width)),(self.x,(self.y + width)),1) # bottom
            if self.walls[3]:
                pygame.draw.line(screen,BLACK,(self.x,(self.y + width)),(self.x,self.y),1) # left
    
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
    
    screen.fill(GREY)
    
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
        print("FULL")
        done = True
        
        for y in range(rows):
            grid.append([])
            for x in range(cols):
                grid[y].append(Cell(x,y))
        
        current_cell = grid[0][0]
        next_cell = 0

    pygame.display.flip()

#-------------------------------------------------------------------------------------

colorWHITE = (255,255,255)
colorBLACK = (0, 0, 0)
colorGRAY = (121, 121, 121)

pygame.display.set_caption('Maze Game')

gameQuit = False

move_count = 0

# character starting position on maze
move_x = 5
move_y = 5

# "pick-up" locations

pickup1_x = (50 * random.randint(0, 13)) + 15
pickup1_y = (50 * random.randint(0, 13)) + 15

pickup2_x = (50 * random.randint(0, 13)) + 15
pickup2_y = (50 * random.randint(0, 13)) + 15

pickup3_x = (50 * random.randint(0, 13)) + 15
pickup3_y = (50 * random.randint(0, 13)) + 15

pickup4_x = (50 * random.randint(0, 13)) + 15
pickup4_y = (50 * random.randint(0, 13)) + 15

 # HERE ____----------------------
    
    
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
            if event.key == pygame.K_LEFT and screen.get_at((move_x - 5, move_y)) == colorWHITE: #tests if theres a wall to the left of the rect
                pygame.draw.rect(screen, colorWHITE, [move_x, move_y, 41, 41])
                move_x -= 50
                move_count += 1
            if event.key == pygame.K_RIGHT and screen.get_at((move_x + 45, move_y)) == colorWHITE:   
                pygame.draw.rect(screen, colorWHITE, [move_x, move_y, 41, 41]) 
                move_x += 50
                move_count += 1
            if event.key == pygame.K_UP and screen.get_at((move_x, move_y - 5)) == colorWHITE:
                pygame.draw.rect(screen, colorWHITE, [move_x, move_y, 41, 41])
                move_y -= 50
                move_count += 1
            if event.key == pygame.K_DOWN and screen.get_at((move_x, move_y + 45)) == colorWHITE:
                pygame.draw.rect(screen, colorWHITE, [move_x, move_y, 41, 41])
                move_y += 50
                move_count += 1

    # make gray rectangle object + flower objects
    pygame.draw.rect(screen, colorGRAY, [move_x, move_y, 41, 41])

    pygame.draw.rect(screen, 'Blue', [(pickup1_x), (pickup1_y), 20, 20])
    pygame.draw.rect(screen, 'Red', [(pickup2_x), (pickup2_y), 20, 20])
    pygame.draw.rect(screen, 'Red', [(pickup3_x), (pickup3_y), 20, 20])
    pygame.draw.rect(screen, 'Red', [(pickup4_x), (pickup4_y), 20, 20]) 
    

    pygame.display.flip()           