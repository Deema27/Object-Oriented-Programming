''' Description: 
creates a pygame program with multiple balls that 
can be moved, added, or removed using mouse clicks and keyboard input '''

# 1 - Import packages
import pygame, sys, random

#Ball class handles individual ball objects
class Ball():
    def __init__(self, window):
        self.window = window  # store window reference for drawing
        self.image = pygame.image.load('images/ball.png')

        #Get image dimensions for positioning and collision detection
        ballRect = self.image.get_rect()
        self.width = ballRect.width
        self.height = ballRect.height

        #Set movement boundaries based on window size
        self.maxWidth = window.width - self.width
        self.maxHeight = window.height - self.height
        
        #Set random starting position
        self.x = random.randrange(0, self.maxWidth)
        self.y = random.randrange(0, self.maxHeight)
        
    #Move ball to a new random position
    def change_position(self):
        self.x = random.randrange(0, self.maxWidth)
        self.y = random.randrange(0, self.maxHeight)

    #Return rectangle for collision detection
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    #Draw ball on screen
    def draw(self):
        self.window.blit(self.image, (self.x, self.y))


# 2 - Define constants
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
background_color = WHITE

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets
boing = pygame.mixer.Sound('sounds/boing.wav')

# 5 - Initialize variables
oBall = Ball(window)
ballList = []
ballList.append(oBall)  # start with one ball in the list   

# 6 - Main loop
while True:

    # 7 - Handle events
    for event in pygame.event.get():

        #Exit program
        if event.type == pygame.QUIT:           
            pygame.quit()  
            sys.exit()
            
        #Mouse click interaction
        if event.type == pygame.MOUSEBUTTONDOWN:

            #Move ball if clicked
            for ball in ballList:
                if ball.get_rect().collidepoint(event.pos):
                    ball.change_position()

            #Add new ball if rectangle clicked
            if rectangleRect.collidepoint(event.pos):
                new_ball = Ball(window)
                ballList.append(new_ball)

        #Keyboard input
        if event.type == pygame.KEYDOWN:

            #Toggle background color
            if event.key == pygame.K_c:
                if background_color == WHITE:
                    background_color = RED
                else:
                    background_color = WHITE

            #Remove ball or play sound if empty
            if event.key == pygame.K_p:
                if len(ballList) > 0:
                    ballList.pop()
                else:
                    boing.play()

    # 9 - Clear screen
    window.fill(background_color)
    
    # 10 - Draw balls
    for ball in ballList:
        ball.draw()

    #Draw clickable rectangle button
    rectangleRect = pygame.draw.rect(window, BLACK, (400, 300, 100, 50), 3)
    
    # 11 - Update display
    pygame.display.update()

    # 12 - Control frame rate
    clock.tick(FRAMES_PER_SECOND)

