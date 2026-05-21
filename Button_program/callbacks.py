''' Description: 
demonstrates three pygame buttons, including callback functions and a callback method '''

# 1 - Import packages
import pygame
from pygame.locals import *
from button_2 import *
import sys

# 2 - Define constants
GRAY = (200, 200, 200)
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 100
FRAMES_PER_SECOND = 30

# Callback function for Button B
def myCallBackFunction():
    print('User pressed Button B, called myCallBackFunction')

# Callback class for Button C
class CallBackTest():
    def __init__(self):
        pass

    def myMethod(self):
        print('User pressed Button C, called myMethod of the CallBackTest object')

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets (images, sounds, etc.)

# 5 - Initialize variables
oCallBackTest = CallBackTest()

oButtonA = SimpleButton(window, (25, 30),
                        'images/buttonAUp.png',
                        'images/buttonADown.png')

oButtonB = SimpleButton(window, (150, 30),
                        'images/buttonBUp.png',
                        'images/buttonBDown.png',
                        callBack=myCallBackFunction)

oButtonC = SimpleButton(window, (275, 30),
                        'images/buttonCUp.png',
                        'images/buttonCDown.png',
                        callBack=oCallBackTest.myMethod)

counter = 0

# 6 - Main loop
while True:

    # 7 - Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if oButtonA.handleEvent(event):
            print('User pressed button A, handled in the main loop')

        oButtonB.handleEvent(event)
        oButtonC.handleEvent(event)

    # 8 - Per-frame updates
    counter += 1

    # 9 - Clear screen
    window.fill(GRAY)

    # 10 - Draw elements
    oButtonA.draw()
    oButtonB.draw()
    oButtonC.draw()

    # 11 - Update display
    pygame.display.update()

    # 12 - Frame rate control
    clock.tick(FRAMES_PER_SECOND)
