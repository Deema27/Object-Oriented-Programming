''' Description: 
Demonstrates interaction between a moving Ball object,
a text display counter, and a clickable restart button. '''

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import random
from Ball import *  # bring in the Ball class code
from text_class import *
from button import *

# 2 - Define constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
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
oFrameCountLabel = SimpleText(window, (60, 20), 
                             'Program has run through this many loops: ', WHITE)
oFrameCountDisplay = SimpleText(window, (500, 20), '', WHITE)
oRestartButton = SimpleButton(window, (280, 60), 
                      'images/restartUp.png', 'images/restartDown.png')
frameCounter = 0

# 6 - Game loop
while True:
    
    # 7 - Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        # Reset frame counter when restart button is clicked
        if oRestartButton.handleEvent(event):
            frameCounter = 0

    # 8 - Update game state each frame
    oBall.update()  # update ball movement
    frameCounter += 1  # increment loop counter
    oFrameCountDisplay.setValue(str(frameCounter))  # update displayed text

    # 9 - Clear screen
    window.fill(BLACK)
    
    # 10 - Draw everything
    oBall.draw()
    oFrameCountLabel.draw()
    oFrameCountDisplay.draw()
    oRestartButton.draw()

    # 11 - Update display
    pygame.display.update()

    # 12 - Frame rate control
    clock.tick(FRAMES_PER_SECOND)
