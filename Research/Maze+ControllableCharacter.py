from operator import truediv
import random
import pygame
import sys
import math
pygame.init()

#import sprites
bg_sprite1 = pygame.image.load("Research/sprites/grass floor 1.png")
bg_sprite2 = pygame.image.load("Research/sprites/grass floor 2.png")
bg_sprite3 = pygame.image.load("Research/sprites/grass floor 3.png")
bg_sprite4 = pygame.image.load("Research/sprites/grass floor 4.png")
bg_sprite5 = pygame.image.load("Research/sprites/grass floor 5.png")
bg_sprite6 = pygame.image.load("Research/sprites/grass floor 6.png")

bg_set = [bg_sprite1, bg_sprite2, bg_sprite3, bg_sprite4, bg_sprite5, bg_sprite6]
mc_sprite_up = pygame.image.load("Research/sprites/mc sprite up.png")
mc_sprite_down = pygame.image.load("Research/sprites/mc sprite down.png")
mc_sprite_left = pygame.image.load("Research/sprites/mc sprite left.png")
mc_sprite_right = pygame.image.load("Research/sprites/mc sprite right.png")
mc_set = [mc_sprite_up, mc_sprite_down, mc_sprite_left, mc_sprite_right]

fl_sprite = pygame.image.load("Research/sprites/flower sprite.png")

#starting position sprite facing down
dir = 4

WHITE = (255,255,255)
GREY = (20,20,20)
BLACK = (0,0,0)
PURPLE = (100,0,100)
RED = (255,0,0)

colorWHITE = (255,255,255)
colorBLACK = (0, 0, 0)
colorGRAY = (121, 121, 121)
colorBG = (222, 211, 184)
light = (9, 134, 148)

# maze properties

maze_dim = (7, 7)
cell = 50
width = 50
size = (maze_dim[0] * cell, maze_dim[1] * cell)

wall_thickness = 3
wall_color = (1, 138, 65)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Maze Generator")

done = False

#clock = pygame.time.Clock()

cols = maze_dim[0]
rows = maze_dim[1]

# initiate set of flowers

fl_num = 4
fl_set = []

# generate flower coordinates

while len(fl_set) < fl_num:
    # add first flower
    coord_fl = ((50 * random.randint(0, rows - 1)) + 15, (50 * random.randint(0, cols - 1)) + 15)
    if coord_fl not in fl_set and coord_fl != (15, 15):
        fl_set.append(coord_fl)

print(fl_set)

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

#-------------------------------------------------------------------------------------

pygame.display.set_caption('Maze Game')

gameQuit = False
gameWon = False

getOne = False
getTwo = False
getThree = False
getFour = False

move_count = 0

# character starting position on maze
move_x = 5
move_y = 5

location = (move_x, move_y)
    
# game loop

while not gameQuit:
    # check and update location of mc:
    loc_mc = (move_x//50, move_y//50)

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
            if event.key == pygame.K_LEFT: #tests if theres a wall to the left of the rect
                dir = 1
                if grid[loc_mc[1]][loc_mc[0]].walls[3] == False:
                    move_x -= 50
                    move_count += 1
            if event.key == pygame.K_RIGHT:
                dir = 2
                if grid[loc_mc[1]][loc_mc[0]].walls[1] == False:
                    move_x += 50
                    move_count += 1
            if event.key == pygame.K_UP:
                dir = 3
                if grid[loc_mc[1]][loc_mc[0]].walls[0] == False:
                    move_y -= 50
                    move_count += 1
            if event.key == pygame.K_DOWN:
                dir = 4
                if grid[loc_mc[1]][loc_mc[0]].walls[2] == False:
                    move_y += 50
                    move_count += 1

    
    screen.fill(colorBG)
    for y in range(rows):
        for x in range(cols):
            grid[y][x].draw()

    # create a black square for every cell on the board except at a certain cell

    cell_loc = []

    # populate coordinates in separate loop

    for x in range(0, size[0]//width):
        for y in range(0, size[1]//width):
            cell_loc.append((x,y))

    # print(cell_loc)

    # draw rectangles

    for item in cell_loc:
        x = item[0]
        y = item[1]
        dx = abs(loc_mc[0]-x)
        dy = abs(loc_mc[1]-y)
        distance = math.sqrt(dx*dx + dy*dy)
        opacity = int((255.0 * (distance) / 3))
        if (opacity > 255):
            opacity = 255
        color = (1, 126, 133)
        rect = pygame.Surface((50, 50))
        rect.set_alpha(opacity)
        rect.fill(light)
        screen.blit(rect, (x * 50,y * 50))

    # blit mc sprite based on key input
    if (dir == 1) :
        screen.blit(mc_sprite_left, [move_x, move_y])
    if (dir == 2) :
        screen.blit(mc_sprite_right, [move_x, move_y])
    if (dir == 3) :
        screen.blit(mc_sprite_up, [move_x, move_y])
    if (dir == 4) :
        screen.blit(mc_sprite_down, [move_x, move_y])

    # test if flowers were picked up
    if fl_set[0][0] - move_x == 10 and fl_set[0][1] - move_y == 10 and getOne == False:
        print("GOT 1/4!")
        getOne = True
    if fl_set[1][0] - move_x == 10 and fl_set[1][1] - move_y == 10 and getTwo == False:
        print("GOT 2/4!")
        getTwo = True
    if fl_set[2][0] - move_x == 10 and fl_set[2][1] - move_y == 10 and getThree == False:
        print("GOT 3/4!")
        getThree = True
    if fl_set[3][0] - move_x == 10 and fl_set[3][1] - move_y == 10 and getFour == False:
        print("GOT 4/4!")
        getFour = True

    # If flowers were not picked up, draw the flowers
    if getOne == False:
        screen.blit(fl_sprite, fl_set[0])
    if getTwo == False:
        screen.blit(fl_sprite, fl_set[1])
    if getThree == False:
        screen.blit(fl_sprite, fl_set[2])
    if getFour == False:
        screen.blit(fl_sprite, fl_set[3])

    if getOne == True and getTwo == True and getThree == True and getFour == True and gameWon == False:
        gameWon == True
        print("YOU WON! Final step count: " + str(move_count))
        exit()
        
    pygame.display.flip()           