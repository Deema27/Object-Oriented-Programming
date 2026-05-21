''' Description: 
Creates multiple Ball objects and updates/draws them each frame
so they bounce independently on the screen. '''

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import random
from Ball import *  # bring in the Ball class code

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_BALLS = 3

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()  

# 4 - Load assets: image(s), sounds, etc.

# 5 - Initialize variables
ballList = []

# Create multiple Ball objects
for oBall in range(0, N_BALLS):
    # Each iteration creates a new Ball instance
    oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
    ballList.append(oBall)

# 6 - Main loop
while True:
    
    # 7 - Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()          

    # 8 - Update all balls each frame
    for oBall in ballList:
        oBall.update()  # update movement/position of each Ball

    # 9 - Clear screen
    window.fill(BLACK)
    
    # 10 - Draw all balls
    for oBall in ballList:
        oBall.draw()

    # 11 - Refresh display
    pygame.display.update()

    # 12 - Control frame rate
    clock.tick(FRAMES_PER_SECOND)
