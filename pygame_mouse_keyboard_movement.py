''' Description: 
creates a pygame program where a ball can be 
moved with arrow keys and repositioned by clicking objects on the screen '''

# 1 - Import packages
import pygame, sys, random

# 2 - Define constants
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
COLOR1 = (0, 0, 0)
COLOR2 = (255, 255, 255)
N_PIXELS_TO_MOVE = 5

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sound(s), etc.
ballImage = pygame.image.load('images/ball.png')

# 5 - Initialize variables
#Set initial ball position
ballX = 50
ballY = 350

#Create rectangle for collision detection
ballRect = pygame.Rect(ballX, ballY, 100, 100)

#Set circle position and size
circlex = 150
circley = 50
circle_rad = 30

#Create rectangle for circle collision detection
circlerect = pygame.Rect(circlex - circle_rad, circley - circle_rad, circle_rad * 2, circle_rad * 2)

# 6 - Main loop
while True:

    # 7 - Handle events
    for event in pygame.event.get():

        #Exit program when window is closed
        if event.type == pygame.QUIT:           
            pygame.quit()  
            sys.exit()

        #Handle mouse clicks
        if event.type == pygame.MOUSEBUTTONDOWN:

            #If ball is clicked, move it to random position
            if ballRect.collidepoint(event.pos):
                ballX = random.randrange(580)
                ballY = random.randrange(380)
                ballRect = pygame.Rect(ballX, ballY, 100, 100)

            #If circle is clicked, move it to random position
            if circlerect.collidepoint(event.pos):
                circlex = random.randrange(490)
                circley = random.randrange(430)
                circlerect = pygame.Rect(circlex - circle_rad, circley - circle_rad, circle_rad * 2, circle_rad * 2)

    # 8 - Per frame updates (keyboard movement)
    keyPressedTuple = pygame.key.get_pressed()

    #Move ball left
    if keyPressedTuple[pygame.K_LEFT]:
        ballX -= N_PIXELS_TO_MOVE

    #Move ball right
    if keyPressedTuple[pygame.K_RIGHT]:
        ballX += N_PIXELS_TO_MOVE

    #Move ball up
    if keyPressedTuple[pygame.K_UP]:
        ballY -= N_PIXELS_TO_MOVE

    #Move ball down
    if keyPressedTuple[pygame.K_DOWN]:
        ballY += N_PIXELS_TO_MOVE

    #Update ball rectangle position
    ballRect = pygame.Rect(ballX, ballY, 100, 100)

    #Keep ball inside screen boundaries
    if ballX < 0:
        ballX = 0
    if ballX + 100 >= WINDOW_WIDTH:
        ballX = WINDOW_WIDTH - 100
    if ballY < 0:
        ballY = 0
    if ballY + 100 >= WINDOW_HEIGHT:
        ballY = WINDOW_HEIGHT - 100

    # 9 - Clear screen
    window.fill(COLOR2)

    # 10 - Draw shapes and image
    circlerect = pygame.draw.circle(window, COLOR1, (circlex, circley), circle_rad, 0)
    pygame.draw.rect(window, COLOR1, (400, 300, 100, 100), 3)
    window.blit(ballImage, (ballX, ballY))

    # 11 - Update display
    pygame.display.update()

    # 12 - Control frame rate
    clock.tick(FRAMES_PER_SECOND)
