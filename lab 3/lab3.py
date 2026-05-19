# Lab 3

# 1 - Import packages
import pygame, sys, random, pygwidgets

# CatImage class - do not change
class CatImage():
    def __init__(self, window):
        self.window = window  # remember the window, so we can draw later
        self.image = pygame.image.load('cat.png') # note the path
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.maxX = window.width - self.width
        self.maxY = window.height - self.height
        
        # Pick a random starting position
        self.new_position()
        
    def new_position(self):
        self.x = random.randrange(0, self.maxX)
        self.y = random.randrange(0, self.maxY)

    def get_rect(self):
        return self.rect

    def draw(self):
        self.rect = self.window.blit(self.image, (self.x, self.y))

# 2 - Define constants
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_PIXELS_TO_MOVE = 10
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sound(s),  etc.
bounceSound = pygame.mixer.Sound('boing.wav') # note the path

# 5 - Initialize variables
oCat = CatImage(window)
catList = []
catList.append(oCat)  # append the new cat to the list of cats

add_cat = pygwidgets.TextButton(window, (150, 400), 'Add cat', textColor=GREEN)
remove_cat = pygwidgets.TextButton(window, (390, 400), 'Remove Cat', textColor=RED)

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end the program
        if event.type == pygame.QUIT:           
            pygame.quit()  
            sys.exit()

        if add_cat.handleEvent(event):
            newCat = CatImage(window)
            catList.append(newCat)
            if len(catList) == 1:
                remove_cat.enable()

        if remove_cat.handleEvent(event):
            if len(catList) > 0:
                catList.pop()
            if len(catList) == 0:
                remove_cat.disable()
                bounceSound.play()

                
        if event.type == pygame.MOUSEBUTTONDOWN:
            for cat in catList:
                if cat.get_rect().collidepoint(event.pos):
                    cat.new_position()
                    
        #TODO ### See if user clicked on a cat or on a rectangle.

                    
    # 8 - Do any "per frame" actions
    
    #TODO ### Check if any keyboard keys are pressed
    keyPressedTuple = pygame.key.get_pressed()

    if len(catList) > 0:
        lastCat = catList[-1]

    if lastCat:
        if keyPressedTuple[pygame.K_LEFT]:
            lastCat.x = lastCat.x - N_PIXELS_TO_MOVE

        if keyPressedTuple[pygame.K_RIGHT]:
            lastCat.x = lastCat.x + N_PIXELS_TO_MOVE

        if keyPressedTuple[pygame.K_UP]:
            lastCat.y = lastCat.y - N_PIXELS_TO_MOVE

        if keyPressedTuple[pygame.K_DOWN]:
            lastCat.y = lastCat.y + N_PIXELS_TO_MOVE

        if lastCat.x < 0:
            lastCat.x = 0
            bounceSound.play()
            
        if lastCat.x >= lastCat.maxX:
            lastCat.x = lastCat.maxX
            bounceSound.play()
            
        if lastCat.y < 0:
            lastCat.y = 0
            bounceSound.play()

        if lastCat.y >= lastCat.maxY:
            lastCat.y = lastCat.maxY
            bounceSound.play()


    # 9 - Clear the window
    window.fill(WHITE)
    
    # 10 - Draw all window elements
    
    #TODO ### Change so that cats do not cover the rectangles' outlines.

    for oCat in catList:
        oCat.draw()

    add_cat.draw()
    remove_cat.draw()

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
