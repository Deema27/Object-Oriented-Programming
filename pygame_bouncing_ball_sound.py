''' Description: 
creates a simple pygame animation where an image (ball) moves 
around the screen and bounces off walls with sound effects '''

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import random

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_PIXELS_PER_FRAME = 3

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
 
# 4 - Load assets: image(s), sound(s), etc.
ballImage = pygame.image.load('images/ball.png')
bounceSound = pygame.mixer.Sound('sounds/boing.wav')
pygame.mixer.music.load('sounds/background.mp3')
pygame.mixer.music.play(-1, 0.0)

# 5 - Initialize variables
#Get rectangle for positioning and movement of ball
ballRect = ballImage.get_rect()

#Set max boundaries so ball stays inside window
MAX_WIDTH = WINDOW_WIDTH - ballRect.width
MAX_HEIGHT = WINDOW_HEIGHT - ballRect.height

#Set random starting position for ball
ballRect.left = random.randrange(MAX_WIDTH)
ballRect.top = random.randrange(MAX_HEIGHT)

#Set movement speed in x and y directions
xSpeed = N_PIXELS_PER_FRAME
ySpeed = N_PIXELS_PER_FRAME
 
# 6 - Loop forever (main game loop)
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():

        #Exit game when window is closed
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # 8 - Update game state each frame

    #Check collision with left/right walls and reverse x direction
    if (ballRect.left < 0) or (ballRect.right >= WINDOW_WIDTH):
        xSpeed = -xSpeed
        bounceSound.play()

    #Check collision with top/bottom walls and reverse y direction
    if (ballRect.top < 0) or (ballRect.bottom >= WINDOW_HEIGHT):
        ySpeed = -ySpeed
        bounceSound.play()

    #Move ball based on current speed
    ballRect.left = ballRect.left + xSpeed
    ballRect.top = ballRect.top + ySpeed

    # 9 - Clear screen
    window.fill(BLACK)
    
    # 10 - Draw ball
    window.blit(ballImage, ballRect)

    # 11 - Update display
    pygame.display.update()

    # 12 - Control frame rate
    clock.tick(FRAMES_PER_SECOND)
