# 1 - Import packages
import pygame, sys, random

# Ball class 
class Ball():
    def __init__(self, window):
        self.window = window  # remember the window, so we can draw later
        self.image = pygame.image.load('images/ball.png')

        # A rect is made up of [x, y, width, height]
        ballRect = self.image.get_rect()
        self.width = ballRect.width
        self.height = ballRect.height
        self.maxWidth = window.width - self.width
        self.maxHeight = window.height - self.height
        
        # Pick a random starting position 
        self.x = random.randrange(0, self.maxWidth)
        self.y = random.randrange(0, self.maxHeight)
        
    def change_position(self):
        self.x = random.randrange(0, self.maxWidth)
        self.y = random.randrange(0, self.maxHeight)

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

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

# 4 - Load assets: image(s), sound(s),  etc.
boing = pygame.mixer.Sound('sounds/boing.wav')
  # The image is now being retrieved in the Ball class
  
# 5 - Initialize variables
oBall = Ball(window)
ballList = []
ballList.append(oBall)  # append the first ball to the list of balls   

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end the program
        if event.type == pygame.QUIT:           
            pygame.quit()  
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            for ball in ballList:
                if ball.get_rect().collidepoint(event.pos):
                    ball.change_position()
            if rectangleRect.collidepoint(event.pos):
                new_ball = Ball(window)
                ballList.append(new_ball)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                if background_color == WHITE:
                    background_color = RED
                else:
                    background_color = WHITE

            if event.key == pygame.K_p:
                if len(ballList) > 0:
                    ballList.pop()
                else:
                    boing.play()


        

    # 8 - Do any "per frame" actions
  
    # 9 - Clear the window
    window.fill(background_color)
    
    # 10 - Draw all window elements
    for ball in ballList:
        ball.draw()

    rectangleRect = pygame.draw.rect(window, BLACK, (400, 300, 100, 50), 3) # 3 pixel edge
    
    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait

