''' Description: 
creates a pygame window with
three clickable buttons and prints which button is pressed '''

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
# Create instances of SimpleButton
oButtonA = SimpleButton(window, (25, 30),
                        'images/buttonAUp.png',
                        'images/buttonADown.png')

oButtonB = SimpleButton(window, (150, 30),
                        'images/buttonBUp.png',
                        'images/buttonBDown.png')

oButtonC = SimpleButton(window, (275, 30),
                        'images/buttonCUp.png',
                        'images/buttonCDown.png')

# 6 - Main loop
while True:

    # 7 - Handle events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if oButtonA.handleEvent(event):
            print('User clicked button A.')

        elif oButtonB.handleEvent(event):
            print('User clicked button B.')

        elif oButtonC.handleEvent(event):
            print('User clicked button C.')

    # 8 - Per-frame updates

    # 9 - Clear screen
    window.fill(GRAY)

    # 10 - Draw buttons
    oButtonA.draw()
    oButtonB.draw()
    oButtonC.draw()

    # 11 - Update display
    pygame.display.update()

    # 12 - Frame rate control
    clock.tick(FRAMES_PER_SECOND)
