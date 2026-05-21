''' Description: 
creates a simple pygame window with a 
clickable button that prints a message when clicked '''

# 1 - Import packages
import pygame
from pygame.locals import *
from button import *
import sys

# 2 - Define constants
GRAY = (200, 200, 200)
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 100
FRAMES_PER_SECOND = 30

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets (images, sounds, etc.)

# 5 - Initialize variables
oButton = SimpleButton(window, (150, 30),
                        'images/buttonUp.png',
                        'images/buttonDown.png')

# 6 - Main loop
while True:

    # 7 - Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if oButton.handleEvent(event):
            print('User has clicked the button.')

    # 8 - Per-frame updates

    # 9 - Clear screen
    window.fill(GRAY)

    # 10 - Draw elements
    oButton.draw()

    # 11 - Update display
    pygame.display.update()

