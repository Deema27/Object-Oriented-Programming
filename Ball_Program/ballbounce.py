''' Description: 
Demonstrates a single Ball object moving and bouncing
inside a pygame window. '''

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
       
# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()  

# 4 - Load assets: image(s), sounds, etc.

# 5 - Initialize variables
oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)

# 6 - Main loop
while True:
    
    # 7 - Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()          

    # 8 - Update ball each frame
    oBall.update()

    # 9 - Clear screen
    window.fill(BLACK)
    
    # 10 - Draw ball
    oBall.draw()

    # 11 - Update display
    pygame.display.update()

    # 12 - Frame rate control
    clock.tick(FRAMES_PER_SECOND)

